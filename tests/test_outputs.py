from typing import List
from pathlib import Path
from datetime import date
from unittest import TestCase, mock

from jinja2.exceptions import TemplateError

from resume.exceptions import ResumeGeneratorError
from resume.outputs import HtmlResumeOutput, JsonResumeOutput
from resume.schemas import (
    Resume,
    ResumeBasics,
    ResumeMetadata,
    ResumeBasicsLocation,
    ResumeMetadataLanguage,
)


__all__: List[str] = []


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
    ),
    metadata=ResumeMetadata(
        language=ResumeMetadataLanguage(
            name="English",
            language_code="en",
        ),
        updated=date(year=1991, month=8, day=24),
    ),
)


class JsonResumeOutputTest(TestCase):
    """JsonResumeOutput tests."""

    def test__generate(self) -> None:
        """_generate method must return resume in JSON format."""
        output = JsonResumeOutput(resume=TEST_RESUME).generate()
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


class HtmlResumeOutputTest(TestCase):
    """HtmlResumeOutput tests."""

    def test__generate(self) -> None:
        """_generate method must return resume in HTML format."""
        output = HtmlResumeOutput(resume=TEST_RESUME).generate()
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

    def test__generate__error__rendering(self) -> None:
        """_generate method must return resume in HTML format (resume rendering error case)."""
        with mock.patch(  # noqa: SIM117
            target="jinja2.environment.Template.render", side_effect=TemplateError()
        ):
            with self.assertRaises(expected_exception=ResumeGeneratorError):
                HtmlResumeOutput(resume=TEST_RESUME).generate()
        with mock.patch(  # noqa: SIM117
            target="jinja2.environment.Environment.__init__",
            side_effect=TemplateError(),
        ):
            with self.assertRaises(expected_exception=ResumeGeneratorError):
                HtmlResumeOutput(resume=TEST_RESUME).generate()
        with mock.patch(  # noqa: SIM117
            target="jinja2.environment.Environment.get_template",
            side_effect=TemplateError(),
        ):
            with self.assertRaises(expected_exception=ResumeGeneratorError):
                HtmlResumeOutput(resume=TEST_RESUME).generate()
