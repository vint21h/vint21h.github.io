from datetime import date
from typing import List
from unittest import TestCase, mock

from resume.exceptions import (
    IncorrectResumePathError,
    IncorrectResumePathFormatError,
    NotResumeError,
)
from resume.schemas import (
    BaseResume,
    ResumeBasics,
    ResumeBasicsLocation,
    ResumeBasicsMetadata,
    ResumeBasicsMetadataLanguage,
)
from resume.utils import (
    CliOptions,
    CliOptionsFormat,
    get_options,
    get_resume,
    get_version,
)

__all__: List[str] = ["GetVersionTest", "GetOptionsTest", "GetResumeTest"]


TEST_RESUME = BaseResume(
    basics=ResumeBasics(
        name="John Doe",
        label="Python/Django developer",
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


class GetVersionTest(TestCase):
    """get_version tests."""

    PYPROJECT_TOML_MOCK__REGULAR: str = """
    [project]
    version = "0.0.0"
    """
    PYPROJECT_TOML_MOCK__NO_VERSION: str = """
    [project]
    """

    @mock.patch(
        target="resume.utils.Path",
        new=mock.mock_open(read_data=PYPROJECT_TOML_MOCK__REGULAR),
        create=True,
    )
    def test_get_version(self) -> None:
        """get_version must return resume version."""
        version = get_version()

        self.assertIsInstance(
            obj=version,
            cls=str,
        )
        self.assertEqual(
            first=version,
            second="0.0.0",
        )

    @mock.patch(
        target="resume.utils.Path",
        new=mock.mock_open(read_data=PYPROJECT_TOML_MOCK__NO_VERSION),
        create=True,
    )
    def test_get_version__no_version(self) -> None:
        """get_version must return resume version (bad schema case)."""
        self.assertIsNone(
            obj=get_version(),
        )

    def test_get_version__no_version__no_file(self) -> None:
        """get_version must return resume version (no file case)."""
        with mock.patch(target="resume.utils.Path", side_effect=FileNotFoundError()):
            self.assertIsNone(
                obj=get_version(),
            )

    def test_get_version__no_version__no_permissions(self) -> None:
        """get_version must return resume version (permission denied case)."""
        with mock.patch(target="resume.utils.Path", side_effect=PermissionError()):
            self.assertIsNone(
                obj=get_version(),
            )


class GetOptionsTest(TestCase):
    """get_options tests."""

    @mock.patch("sys.argv", ["__main__.py", "-f", "json", "-r", "my.RESUME"])
    def test_get_version(self) -> None:
        """get_options must return CliOptions dataclass instance with corresponding properties."""
        options = get_options()

        self.assertIsInstance(
            obj=options,
            cls=CliOptions,
        )
        self.assertEqual(
            first=options.format,
            second=CliOptionsFormat.json,
        )


class GetResumeTest(TestCase):
    """get_resume tests."""

    def test_get_resume(self) -> None:
        """get_resume must return resume variable loaded from supplied module path."""
        resume = get_resume(path=f"{__name__}:TEST_RESUME")

        self.assertIsInstance(
            obj=resume,
            cls=BaseResume,
        )

    def test_get_resume__not_resume(self) -> None:
        """get_resume must return resume variable loaded from supplied module path (not a resume case)."""
        with self.assertRaises(
            expected_exception=NotResumeError,
        ):
            get_resume(path=f"{__name__}:TEST_RESUME__NOT_RESUME")

    def test_get_resume__bad_resume_path_format(self) -> None:
        """get_resume must return resume variable loaded from supplied module path (bad resume path format case)."""
        with self.assertRaises(
            expected_exception=IncorrectResumePathFormatError,
        ):
            get_resume(path="TEST_RESUME")

    def test_get_resume__bad_resume_path(self) -> None:
        """get_resume must return resume variable loaded from supplied module path (bad resume path case)."""
        with self.assertRaises(
            expected_exception=IncorrectResumePathError,
        ):
            get_resume(path="tests:TEST_RESUME")
