from typing import List


__all__: List[str] = [
    "NotResumeError",
    "IncorrectResumePathFormatError",
    "IncorrectResumePathError",
    "ResumeGeneratorError",
    "ResumeGeneratorOptionsError",
    "BaseResumeError",
]


class BaseResumeError(Exception):
    """Base resume error exception."""

    ...


class NotResumeError(BaseResumeError):
    """Resume variable is not inherited from 'Resume' class error exception."""

    ...


class IncorrectResumePathFormatError(BaseResumeError):
    """Bad resume variable path format error exception."""

    ...


class IncorrectResumePathError(BaseResumeError):
    """Bad resume variable path error exception."""

    ...


class ResumeGeneratorError(BaseResumeError):
    """Resume generator error exception."""

    ...


class ResumeGeneratorOptionsError(BaseResumeError):
    """Resume generator CLI options error exception."""

    ...
