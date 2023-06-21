from argparse import ArgumentParser
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import List, Optional

import toml

from resume.constants import RESUME_PYPROJECT_PATH

__all__: List[str] = ["get_options", "get_version"]


class CliOptionsFormat(Enum):
    """Output format CLI option choices."""

    json = "json"
    html = "html"
    python = "python"


@dataclass
class CliOptions:
    """Resume CLI options representation."""

    format: CliOptionsFormat  # noqa: A003
    output: Optional[str] = None


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
        "-o",
        "--output",
        action="store",
        dest="output",
        type=str,
        required=False,
        metavar="OUTPUT",
        help="output file path",
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
