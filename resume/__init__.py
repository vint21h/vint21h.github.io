import sys
from typing import List

from rich import print as rprint

from resume.utils import get_output, get_resume, get_options
from resume.exceptions import (
    NotResumeError,
    IncorrectResumePathError,
    IncorrectResumePathFormatError,
)


__all__: List[str] = ["main"]


# TODO (@vint21h): implement it!!1
def main() -> None:
    """Resume CLI."""
    try:
        options = get_options()
        resume = get_resume(path=options.resume)
        output = get_output(resume=resume, format_=options.format)
    except (
        NotResumeError,
        IncorrectResumePathFormatError,
        IncorrectResumePathError,
    ) as error:
        sys.stderr.write(f"Something happened wrong :(. {error}\n")
        sys.exit(2)

    rprint(output)
