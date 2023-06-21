from typing import List

from rich import print as rprint

from resume.constants import JSON_DUMPS_KWARGS
from resume.schemas import BaseResume
from resume.utils import get_options

__all__: List[str] = ["main"]


def main(resume: BaseResume) -> None:
    """
    Resume CLI.

    :param resume: resume instance
    :type resume: BaseResume
    """
    options = get_options()
    rprint(resume)
    rprint(resume.json(**JSON_DUMPS_KWARGS))
    rprint(options)
