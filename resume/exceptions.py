from typing import List

__all__: List[str] = [
    "NotResumeError",
    "IncorrectResumePathFormatError",
    "IncorrectResumePathError",
]


class NotResumeError(Exception):
    """Resume variable is not inherited from 'BaseResume' class error exception."""

    def __init__(self, resume: object) -> None:
        """
        Exception constructor.

        :param resume: resume variable instance
        :type resume: object
        """
        self.resume = resume
        self.message = f"{resume} is not an instance of 'BaseResume'."
        super().__init__(self.message)


class IncorrectResumePathFormatError(Exception):
    """Bad resume variable path format error exception."""

    def __init__(self, resume: str, error: Exception) -> None:
        """
        Exception constructor.

        :param resume: resume variable path
        :type resume: str
        :param error: high level exception
        :type error: Exception
        """
        self.resume = resume
        self.message = f"Incorrect resume variable path: {resume}. Should by in format: 'module:variable', for example: 'my.RESUME'. {error}"
        super().__init__(self.message)


class IncorrectResumePathError(Exception):
    """Bad resume variable path error exception."""

    def __init__(self, resume: str, error: Exception) -> None:
        """
        Exception constructor.

        :param resume: resume variable path
        :type resume: str
        :param error: high level exception
        :type error: Exception
        """
        self.resume = resume
        self.message = f"Incorrect resume variable path: {resume}. {error}"
        super().__init__(self.message)
