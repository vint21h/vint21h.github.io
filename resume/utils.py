from enum import Enum
from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional
from argparse import ArgumentParser
from importlib import import_module

import toml

from resume.schemas import BaseResume
from resume.constants import RESUME_PYPROJECT_PATH
from resume.exceptions import (
    NotResumeError,
    IncorrectResumePathError,
    IncorrectResumePathFormatError,
)


__all__: List[str] = ["get_options", "get_version", "get_resume"]


class CliOptionsFormat(Enum):
    """Output format CLI option choices."""

    json = "json"
    html = "html"


@dataclass
class CliOptions:
    """Resume CLI options representation."""

    format: CliOptionsFormat  # noqa: A003
    resume: str


def get_options() -> CliOptions:
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
        dest="format",
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


def get_version() -> Optional[str]:
    """
    Get resume version.

    :return: resume version
    :rtype: Optional[str]
    """
    try:
        file_ = Path(RESUME_PYPROJECT_PATH)
    except (FileNotFoundError, PermissionError):
        return None

    return toml.load(f=file_).get("project", {}).get("version")


def get_resume(path: str) -> BaseResume:
    """
    Loads resume variable from supplied module path.

    :param path: resume variable path
    :type path: str
    :return: resume variable
    :rtype: BaseResume
    :raises NotResumeError: in case when variable is not inherited from 'BaseResume class'
    :raises IncorrectResumePathError: in case of wrong module/variable path
    :raises IncorrectResumePathFormatError: in case of bad resume variable path format
    """
    try:
        module, variable = path.strip(" ").split(":")
    except ValueError as error:
        raise IncorrectResumePathFormatError(resume=path, error=error) from error

    try:  # noqa: TRY101
        resume = import_module(name=module).__getattribute__(variable)
    except (ModuleNotFoundError, AttributeError) as error:
        raise IncorrectResumePathError(resume=path, error=error) from error

    if not isinstance(resume, BaseResume):
        raise NotResumeError(resume=resume)

    return resume
