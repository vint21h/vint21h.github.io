from io import StringIO
from typing import List
from pathlib import Path
from datetime import date
from unittest import TestCase, mock

from contextlib2 import redirect_stderr, redirect_stdout

from resume.generators import (
    Options,
    OptionsFormat,
    ResumeGenerator,
    ResumeGeneratorCli,
)
from resume.schemas import (
    Resume,
    ResumeBasics,
    ResumeBasicsLocation,
    ResumeBasicsMetadata,
    ResumeBasicsMetadataLanguage,
)
from resume.exceptions import (
    NotResumeError,
    BaseResumeError,
    IncorrectResumePathError,
    ResumeGeneratorOptionsError,
    IncorrectResumePathFormatError,
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
        options = Options(
            format_=OptionsFormat.json,
            resume=f"{__file__}:TEST_RESUME",
        )
        generator = ResumeGenerator(options=options)

        self.assertIsInstance(
            obj=generator._options,
            cls=Options,
        )
        self.assertEqual(
            first=generator._options.format_,
            second=OptionsFormat.json,
        )

    def test__get_resume_path(self) -> None:
        """_get_resume_path method must return resume module name and variable name from path."""
        options = Options(
            format_=OptionsFormat.json,
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
        options = Options(
            format_=OptionsFormat.json,
            resume="TEST_RESUME",
        )
        generator = ResumeGenerator(options=options)

        with self.assertRaises(expected_exception=IncorrectResumePathFormatError):
            generator._get_resume_path(path=generator._options.resume)

    def test__get_resume(self) -> None:
        """_get_resume method must return resume variable from supplied module path."""
        options = Options(
            format_=OptionsFormat.json,
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
        options = Options(
            format_=OptionsFormat.json,
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
        options = Options(
            format_=OptionsFormat.json,
            resume=f"{__name__}:TEST_RESUME__NOT_RESUME",
        )
        generator = ResumeGenerator(options=options)
        module, variable = generator._get_resume_path(path=generator._options.resume)

        with self.assertRaises(
            expected_exception=NotResumeError,
        ):
            generator._get_resume(module=module, variable=variable)

    def test__generate__html(self) -> None:
        """_generate method must return resume in specified format (HTML case)."""
        options = Options(
            format_=OptionsFormat.html,
            resume=f"{__name__}:TEST_RESUME",
        )
        output = ResumeGenerator(options=options)._generate()
        fixture = Path(__file__).parent.joinpath("fixtures", "output.html")
        expected = fixture.open().read()

        self.assertIsInstance(
            obj=output,
            cls=str,
        )
        self.assertEqual(
            first=output,
            second=expected.strip(),
        )

    def test__generate__json(self) -> None:
        """_generate method must return resume in specified format (JSON case)."""
        options = Options(
            format_=OptionsFormat.json,
            resume=f"{__name__}:TEST_RESUME",
        )
        output = ResumeGenerator(options=options)._generate()
        fixture = Path(__file__).parent.joinpath("fixtures", "output.json")
        expected = fixture.open().read()

        self.assertIsInstance(
            obj=output,
            cls=str,
        )
        self.assertEqual(
            first=output,
            second=expected.strip(),
        )

    def test__generate__error__options(self) -> None:
        """_generate method must return resume in specified format (options error case)."""
        options = Options(
            format_=OptionsFormat.json,
            resume=f"{__name__}:TEST_RESUME",
        )
        ResumeGenerator._OUTPUTS = {}

        with self.assertRaises(expected_exception=ResumeGeneratorOptionsError):
            ResumeGenerator(options=options)._generate()

    def test_generate__html(self) -> None:
        """'generate' method must return resume in specified format (HTML case)."""
        options = Options(
            format_=OptionsFormat.html,
            resume=f"{__name__}:TEST_RESUME",
        )
        output = ResumeGenerator(options=options).generate()
        fixture = Path(__file__).parent.joinpath("fixtures", "output.html")
        expected = fixture.open().read()

        self.assertIsInstance(
            obj=output,
            cls=str,
        )
        self.assertEqual(
            first=output,
            second=expected.strip(),
        )

    def test_generate__json(self) -> None:
        """'generate' method must return resume in specified format (JSON case)."""
        options = Options(
            format_=OptionsFormat.json,
            resume=f"{__name__}:TEST_RESUME",
        )
        output = ResumeGenerator(options=options).generate()
        fixture = Path(__file__).parent.joinpath("fixtures", "output.json")
        expected = fixture.open().read()

        self.assertIsInstance(
            obj=output,
            cls=str,
        )
        self.assertEqual(
            first=output,
            second=expected.strip(),
        )


class ResumeGeneratorCliTest(TestCase):
    """ResumeGeneratorCli tests."""

    @mock.patch(
        "sys.argv", ["__main__.py", "-f", "json", "-r", f"{__name__}:TEST_RESUME"]
    )
    def test___init__(self) -> None:
        """__init__ method must set up options."""
        generator = ResumeGeneratorCli()

        self.assertIsInstance(
            obj=generator._options,
            cls=Options,
        )
        self.assertEqual(
            first=generator._options.format_,
            second=OptionsFormat.json,
        )

    @mock.patch(
        "sys.argv", ["__main__.py", "-f", "json", "-r", f"{__name__}:TEST_RESUME"]
    )
    def test__get_options(self) -> None:
        """_get_options method must return Options dataclass instance with corresponding properties."""
        generator = ResumeGeneratorCli()
        options = generator._get_options()

        self.assertIsInstance(
            obj=options,
            cls=Options,
        )
        self.assertEqual(
            first=options.format_,
            second=OptionsFormat.json,
        )

    @mock.patch(
        "sys.argv", ["__main__.py", "-f", "json", "-r", f"{__name__}:TEST_RESUME"]
    )
    def test__generate__json(self) -> None:
        """_generate method must pretty print resume in specified format (JSON case)."""
        fixture = Path(__file__).parent.joinpath("fixtures", "output.json")
        expected = fixture.open().read()
        output = StringIO()

        with redirect_stdout(output):
            ResumeGeneratorCli()._generate()

        self.assertIsInstance(
            obj=output.getvalue(),
            cls=str,
        )
        self.assertEqual(
            first=output.getvalue().strip(),
            second=expected.strip(),
        )

    @mock.patch(
        "sys.argv", ["__main__.py", "-f", "html", "-r", f"{__name__}:TEST_RESUME"]
    )
    def test__generate__html(self) -> None:
        """_generate method must pretty print resume in specified format (HTML case)."""
        fixture = Path(__file__).parent.joinpath("fixtures", "output.html")
        expected = fixture.open().read()
        output = StringIO()

        with redirect_stdout(output):
            ResumeGeneratorCli()._generate()

        self.assertIsInstance(
            obj=output.getvalue(),
            cls=str,
        )
        self.assertEqual(
            first=output.getvalue().strip(),
            second=expected.strip(),
        )

    @mock.patch(
        "sys.argv", ["__main__.py", "-f", "json", "-r", f"{__name__}:TEST_RESUME"]
    )
    def test__generate__error(self) -> None:
        """_generate method must pretty print resume in specified format (error case)."""
        output = StringIO()

        with mock.patch(
            target="resume.generators.ResumeGenerator.generate",
            side_effect=BaseResumeError(),
        ):
            with self.assertRaises(
                expected_exception=SystemExit
            ) as excinfo, redirect_stderr(output):
                ResumeGeneratorCli()._generate()

            self.assertTupleEqual(tuple1=excinfo.exception.code, tuple2=(2,))

    @mock.patch(
        "sys.argv", ["__main__.py", "-f", "json", "-r", f"{__name__}:TEST_RESUME"]
    )
    def test_generate__json(self) -> None:
        """'generate' method must pretty print resume in specified format (JSON case)."""
        fixture = Path(__file__).parent.joinpath("fixtures", "output.json")
        expected = fixture.open().read()
        output = StringIO()

        with redirect_stdout(output):
            ResumeGeneratorCli().generate()

        self.assertIsInstance(
            obj=output.getvalue(),
            cls=str,
        )
        self.assertEqual(
            first=output.getvalue().strip(),
            second=expected.strip(),
        )

    @mock.patch(
        "sys.argv", ["__main__.py", "-f", "html", "-r", f"{__name__}:TEST_RESUME"]
    )
    def test_generate__html(self) -> None:
        """'generate' method must pretty print resume in specified format (HTML case)."""
        fixture = Path(__file__).parent.joinpath("fixtures", "output.html")
        expected = fixture.open().read()
        output = StringIO()

        with redirect_stdout(output):
            ResumeGeneratorCli().generate()

        self.assertIsInstance(
            obj=output.getvalue(),
            cls=str,
        )
        self.assertEqual(
            first=output.getvalue().strip(),
            second=expected.strip(),
        )
