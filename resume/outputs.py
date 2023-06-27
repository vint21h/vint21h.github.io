from typing import List
from abc import ABC, abstractmethod

from bs4 import BeautifulSoup
from jinja2.loaders import PackageLoader
from jinja2.environment import Environment
from jinja2.utils import select_autoescape
from jinja2.exceptions import TemplateError

from resume.schemas import Resume
from resume.exceptions import ResumeGeneratorError
from resume.constants import (
    HTML_YEAR_FORMAT,
    JSON_DUMPS_KWARGS,
    HTML_TEMPLATE_NAME,
    JSON_EXCLUDE_FIELDS,
    HTML_MONTH_YEAR_FORMAT,
    HTML_TEMPLATES_PACKAGE,
    HTML_DAY_MONTH_YEAR_FORMAT,
)


__all__: List[str] = ["HtmlResumeOutput", "JsonResumeOutput"]


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
        ...  # pragma: no cover


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
                loader=PackageLoader(package_name=HTML_TEMPLATES_PACKAGE),
                autoescape=select_autoescape(),
            )
            template = jinja.get_template(name=HTML_TEMPLATE_NAME)
            output = template.render(
                RESUME=self.resume,
                HTML_MONTH_YEAR_FORMAT=HTML_MONTH_YEAR_FORMAT,
                HTML_DAY_MONTH_YEAR_FORMAT=HTML_DAY_MONTH_YEAR_FORMAT,
                HTML_YEAR_FORMAT=HTML_YEAR_FORMAT,
            )
            # prettify HTML
            document = BeautifulSoup(markup=output, features="html.parser")
            output = document.prettify(formatter="html5")
        except TemplateError as error:
            raise ResumeGeneratorError(
                f"A problem occurred during generating output for: {self.resume}. {error}"
            ) from error

        return output
