from typing import List

from rich import print as rprint

from resume.utils import get_resume, get_options
from resume.constants import JSON_DUMPS_KWARGS, JSON_EXCLUDE_FIELDS


__all__: List[str] = ["main"]


# TODO (@vint21h): implement it!!1
def main() -> None:
    """Resume CLI."""
    options = get_options()
    resume = get_resume(path=options.resume)

    # rprint(resume)
    rprint(resume.json(exclude=JSON_EXCLUDE_FIELDS, **JSON_DUMPS_KWARGS))
    # rprint(options)
