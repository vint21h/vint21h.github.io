import sys
from enum import Enum
from abc import ABC, abstractmethod
from argparse import ArgumentParser
from importlib import import_module
from typing import List, Final, Tuple

from pydantic import BaseModel
from rich import print as rprint
from jinja2.loaders import PackageLoader
from jinja2.environment import Environment
from jinja2.utils import select_autoescape
from jinja2.exceptions import TemplateError

from resume.schemas import Resume
from resume.utils import get_version
from resume.constants import (
    HTML_YEAR_FORMAT,
    JSON_DUMPS_KWARGS,
    JSON_EXCLUDE_FIELDS,
    HTML_MONTH_YEAR_FORMAT,
    HTML_DAY_MONTH_YEAR_FORMAT,
)
from resume.exceptions import (
    NotResumeError,
    ResumeGeneratorError,
    IncorrectResumePathError,
    ResumeGeneratorOptionsError,
    IncorrectResumePathFormatError,
)


__all__: List[str] = ["ResumeGenerator", "ResumeGeneratorCli"]


class CliOptionsFormat(Enum):
    """Output format CLI option choices."""

    json = "json"
    html = "html"


class CliOptions(BaseModel):
    """Resume CLI options representation."""

    format_: CliOptionsFormat
    resume: str


class BaseResumeOutput(ABC):
    """Base resume output generator."""

    resume: Resume

    def __init__(self, resume: Resume) -> None:
        """
        Set up some properties.

        :param resume: resume instance
        :type resume: Resume
        """
        self.resume = resume

    def generate(self) -> str:
        """
        Generate resume in specified format.

        :return: resume in specified format
        :rtype: str
        """
        return self._generate()

    @abstractmethod
    def _generate(self) -> str:
        """
        Generate resume in specified format.

        :return: resume in specified format
        :rtype: str
        """
        ...


class JsonResumeOutput(BaseResumeOutput):
    """JSON resume output generator."""

    def _generate(self) -> str:
        """
        Generate resume in JSON format.

        :return: resume in JSON format
        :rtype: str
        """
        return self.resume.json(
            exclude=JSON_EXCLUDE_FIELDS, by_alias=True, **JSON_DUMPS_KWARGS
        )


class HtmlResumeOutput(BaseResumeOutput):
    """HTML resume output generator."""

    def _generate(self) -> str:
        """
        Generate resume in HTML format.

        :return: resume in HTML format
        :rtype: str
        :raises ResumeGeneratorError: in case something go wrong during resume rendering
        """
        try:
            jinja = Environment(
                loader=PackageLoader("resume"), autoescape=select_autoescape()
            )
            template = jinja.get_template("resume.html.jinja")
            output = template.render(
                RESUME=self.resume,
                HTML_MONTH_YEAR_FORMAT=HTML_MONTH_YEAR_FORMAT,
                HTML_DAY_MONTH_YEAR_FORMAT=HTML_DAY_MONTH_YEAR_FORMAT,
                HTML_YEAR_FORMAT=HTML_YEAR_FORMAT,
            )
        except TemplateError as error:
            raise ResumeGeneratorError(
                f"A problem occurred during generating output for: {self.resume}. {error}"
            ) from error

        return output


class ResumeGenerator:
    """Resume output generator."""

    _options: CliOptions
    _OUTPUTS: Final = {
        CliOptionsFormat.json: JsonResumeOutput,
        CliOptionsFormat.html: HtmlResumeOutput,
    }

    def __init__(self, options: CliOptions) -> None:
        """
        Set up options.

        :param options: CLI options
        :type options: CliOptions
        """
        self._options = options

    def generate(self) -> str:
        """
        Generate resume in specified format.

        :return: resume in specified format
        :rtype: str
        """
        return self._generate()

    def _generate(self) -> str:
        """
        Generate resume in specified format.

        :return: resume in specified format
        :rtype: str
        :raises ResumeGeneratorOptionsError: in case when specified format output generator does not exist
        """
        module, variable = self._get_resume_path(self._options.resume)
        resume = self._get_resume(module=module, variable=variable)
        try:
            output = self._OUTPUTS[self._options.format_](resume=resume)
        except KeyError as error:
            raise ResumeGeneratorOptionsError(
                f"'{self._options.format_}' output generator does not exist."
            ) from error

        return output.generate()

    @staticmethod
    def _get_resume_path(path: str) -> Tuple[str, str]:
        """
        Get resume module name and variable name from path.

        :param path: resume variable path
        :type path: str
        :return: resume module name and variable name
        :rtype: Tuple[str, str]
        :raises IncorrectResumePathFormatError: in case of bad resume variable path format
        """
        try:
            module, variable = path.strip(" ").split(":")
        except ValueError as error:
            raise IncorrectResumePathFormatError(
                f"Incorrect resume variable path: {path}. Should be in format: 'module:variable', for example: 'my:RESUME'. {error}"
            ) from error

        return module, variable

    @staticmethod
    def _get_resume(module: str, variable: str) -> Resume:
        """
        Loads resume variable from supplied module path.

        :param module: resume module name
        :type module: str
        :param variable: resume variable name
        :type variable: str
        :return: resume variable
        :rtype: Resume
        :raises NotResumeError: in case when variable is not inherited from 'Resume class'
        :raises IncorrectResumePathError: in case of wrong module/variable path
        """
        try:
            resume = import_module(name=module).__getattribute__(variable)
        except (ModuleNotFoundError, AttributeError) as error:
            raise IncorrectResumePathError(
                f"Incorrect resume variable path. {error}"
            ) from error

        if not isinstance(resume, Resume):
            raise NotResumeError(f"{resume} is not an instance of 'Resume'.")

        return resume


class ResumeGeneratorCli:
    """Resume output generator CLI."""

    _options: CliOptions

    def __init__(self) -> None:
        """Set up options."""
        self._options = self._get_options()

    def generate(self) -> None:
        """Generate resume in specified format and write it pretty formatted in to stdout."""
        self._generate()

    def _generate(self) -> None:
        """Generate resume in specified format and write it pretty formatted in to stdout."""
        try:
            generator = ResumeGenerator(options=self._options)
            output = generator.generate()
        except (
            NotResumeError,
            IncorrectResumePathFormatError,
            IncorrectResumePathError,
            ResumeGeneratorOptionsError,
            ResumeGeneratorError,
        ) as error:
            sys.stderr.write(f"Something happened wrong :(. {error}\n")
            sys.exit(2)

        rprint(output)

    @staticmethod
    def _get_options() -> CliOptions:
        """
        Parse commandline options arguments.

        :return: parsed command line arguments
        :rtype: CliOptions
        """
        parser = ArgumentParser(description="Resume as Python code")
        parser.add_argument(
            "-f",
            "--format",
            action="store",
            dest="format_",
            type=CliOptionsFormat,
            required=True,
            metavar="FORMAT",
            help=f"output format ({', '.join([fmt.value for fmt in CliOptionsFormat])})",
        )
        parser.add_argument(
            "-r",
            "--resume",
            action="store",
            dest="resume",
            type=str,
            required=True,
            metavar="RESUME",
            help="resume class module:variable path, for example 'my:RESUME'",
        )
        parser.add_argument(
            "-v",
            "--version",
            action="version",
            version=get_version(),
        )
        options = parser.parse_args()

        return CliOptions(**vars(options))
