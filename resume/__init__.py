import sys
from typing import List

from rich import print as rprint

from resume.generators import ResumeGenerator
from resume.exceptions import (
    NotResumeError,
    ResumeGeneratorError,
    IncorrectResumePathError,
    ResumeGeneratorOptionsError,
    IncorrectResumePathFormatError,
)


__all__: List[str] = ["main"]


def main() -> None:
    """Resume CLI."""
    try:
        generator = ResumeGenerator()
        output = generator.generate()
    except (
        NotResumeError,
        IncorrectResumePathFormatError,
        IncorrectResumePathError,
        ResumeGeneratorOptionsError,
        ResumeGeneratorError,
    ) as error:
        sys.stderr.write(f"Something happened wrong :(. {error}\n")
        sys.exit(2)

    rprint(output)
