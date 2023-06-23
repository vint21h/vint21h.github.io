from typing import List
from datetime import date
from unittest import TestCase, mock

from resume.generators import (
    CliOptions,
    ResumeGenerator,
    CliOptionsFormat,
    ResumeGeneratorCli,
)
from resume.exceptions import (
    NotResumeError,
    IncorrectResumePathError,
    IncorrectResumePathFormatError,
)
from resume.schemas import (
    Resume,
    ResumeBasics,
    ResumeBasicsLocation,
    ResumeBasicsMetadata,
    ResumeBasicsMetadataLanguage,
)


__all__: List[str] = ["ResumeGeneratorTest", "ResumeGeneratorCliTest"]


TEST_RESUME = Resume(
    basics=ResumeBasics(
        name="John Doe",
        label="Python developer",
        email="john.doe@example.com",
        linkedin="https://www.linkedin.com/in/john.doe/",
        site="https://www.example.com/",
        location=ResumeBasicsLocation(
            name="United States of America",
            country_code="US",
        ),
        metadata=ResumeBasicsMetadata(
            language=ResumeBasicsMetadataLanguage(
                name="English",
                language_code="en",
            ),
            updated=date(year=1991, month=8, day=24),
        ),
    )
)
TEST_RESUME__NOT_RESUME = object()


class ResumeGeneratorTest(TestCase):
    """ResumeGenerator tests."""

    def test___init__(self) -> None:
        """__init__ method must set up options."""
        options = CliOptions(
            format_=CliOptionsFormat.json,
            resume="my:RESUME",
        )
        generator = ResumeGenerator(options=options)

        self.assertIsInstance(
            obj=generator._options,
            cls=CliOptions,
        )
        self.assertEqual(
            first=generator._options.format_,
            second=CliOptionsFormat.json,
        )

    def test__get_resume_path(self) -> None:
        """_get_resume_path method must return resume module name and variable name from path."""
        options = CliOptions(
            format_=CliOptionsFormat.json,
            resume="my:RESUME",
        )
        generator = ResumeGenerator(options=options)
        module, variable = generator._get_resume_path(path=generator._options.resume)

        self.assertEqual(
            first=module,
            second="my",
        )
        self.assertEqual(
            first=variable,
            second="RESUME",
        )

    def test__get_resume_path__error__bad_format(self) -> None:
        """_get_resume_path method must return resume module name and variable name from path (bad resume variable path format case)."""
        options = CliOptions(
            format_=CliOptionsFormat.json,
            resume="TEST_RESUME",
        )
        generator = ResumeGenerator(options=options)

        with self.assertRaises(expected_exception=IncorrectResumePathFormatError):
            generator._get_resume_path(path=generator._options.resume)

    def test__get_resume(self) -> None:
        """_get_resume method must return resume variable from supplied module path."""
        options = CliOptions(
            format_=CliOptionsFormat.json,
            resume=f"{__name__}:TEST_RESUME",
        )
        generator = ResumeGenerator(options=options)
        module, variable = generator._get_resume_path(path=generator._options.resume)

        self.assertIsInstance(
            obj=generator._get_resume(module=module, variable=variable),
            cls=Resume,
        )

    def test__get_resume__error__bad_path(self) -> None:
        """_get_resume method must return resume variable from supplied module path (bad resume path case)."""
        options = CliOptions(
            format_=CliOptionsFormat.json,
            resume="tests:TEST_RESUME",
        )
        generator = ResumeGenerator(options=options)
        module, variable = generator._get_resume_path(path=generator._options.resume)

        with self.assertRaises(
            expected_exception=IncorrectResumePathError,
        ):
            generator._get_resume(module=module, variable=variable)

    def test__get_resume__error__not_resume(self) -> None:
        """_get_resume method must return resume variable from supplied module path (not a resume case)."""
        options = CliOptions(
            format_=CliOptionsFormat.json,
            resume=f"{__name__}:TEST_RESUME__NOT_RESUME",
        )
        generator = ResumeGenerator(options=options)
        module, variable = generator._get_resume_path(path=generator._options.resume)

        with self.assertRaises(
            expected_exception=NotResumeError,
        ):
            generator._get_resume(module=module, variable=variable)


class ResumeGeneratorCliTest(TestCase):
    """ResumeGeneratorCli tests."""

    @mock.patch("sys.argv", ["__main__.py", "-f", "json", "-r", "my:RESUME"])
    def test___init__(self) -> None:
        """__init__ method must set up options."""
        generator = ResumeGeneratorCli()

        self.assertIsInstance(
            obj=generator._options,
            cls=CliOptions,
        )
        self.assertEqual(
            first=generator._options.format_,
            second=CliOptionsFormat.json,
        )

    @mock.patch("sys.argv", ["__main__.py", "-f", "json", "-r", "my:RESUME"])
    def test__get_options(self) -> None:
        """_get_options method must return CliOptions dataclass instance with corresponding properties."""
        generator = ResumeGeneratorCli()
        options = generator._get_options()

        self.assertIsInstance(
            obj=options,
            cls=CliOptions,
        )
        self.assertEqual(
            first=options.format_,
            second=CliOptionsFormat.json,
        )
