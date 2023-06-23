from pathlib import Path
from typing import List, Optional

import toml

from resume.constants import RESUME_PYPROJECT_PATH


__all__: List[str] = ["get_version"]


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
