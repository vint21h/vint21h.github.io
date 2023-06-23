from typing import List


__all__: List[str] = [
    "NotResumeError",
    "IncorrectResumePathFormatError",
    "IncorrectResumePathError",
    "ResumeGeneratorError",
    "ResumeGeneratorOptionsError",
]


class NotResumeError(Exception):
    """Resume variable is not inherited from 'Resume' class error exception."""

    ...


class IncorrectResumePathFormatError(Exception):
    """Bad resume variable path format error exception."""

    ...


class IncorrectResumePathError(Exception):
    """Bad resume variable path error exception."""

    ...


class ResumeGeneratorError(Exception):
    """Resume generator error exception."""

    ...


class ResumeGeneratorOptionsError(Exception):
    """Resume generator CLI options error exception."""

    ...
