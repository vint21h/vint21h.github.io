from typing import List
from unittest import TestCase, mock

from resume.utils import get_version


__all__: List[str] = ["GetVersionTest"]


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
        """'get_version' function must return resume version."""
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
    def test_get_version___error__no_version(self) -> None:
        """'get_version' function must return resume version (bad schema case)."""
        self.assertIsNone(
            obj=get_version(),
        )

    def test_get_version__error__no_version__no_file(self) -> None:
        """'get_version' function must return resume version (no file case)."""
        with mock.patch(target="resume.utils.Path", side_effect=FileNotFoundError()):
            self.assertIsNone(
                obj=get_version(),
            )

    def test_get_version__error__no_version__no_permissions(self) -> None:
        """'get_version' function must return resume version (permission denied case)."""
        with mock.patch(target="resume.utils.Path", side_effect=PermissionError()):
            self.assertIsNone(
                obj=get_version(),
            )
