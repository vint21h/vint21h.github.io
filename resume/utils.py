from enum import Enum
from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional

import toml

from resume.constants import RESUME_PYPROJECT_PATH


__all__: List[str] = ["get_version"]


class CliOptionsFormat(Enum):
    """Output format CLI option choices."""

    json = "json"
    html = "html"


@dataclass
class CliOptions:
    """Resume CLI options representation."""

    format: CliOptionsFormat  # noqa: A003
    resume: str


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
