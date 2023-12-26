from typing import Any, Dict, List, Final


__all__: List[str] = [
    "RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__COMPANY",
    "RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__OPENSOURCE",
    "RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__FREELANCE",
    "RESUME_PYPROJECT_PATH",
    "JSON_DUMPS_KWARGS",
    "JSON_EXCLUDE_FIELDS",
    "HTML_MONTH_YEAR_FORMAT",
    "HTML_DAY_MONTH_YEAR_FORMAT",
    "HTML_YEAR_FORMAT",
    "HTML_TEMPLATES_PACKAGE",
    "HTML_TEMPLATE_NAME",
    "HTML_PRETTIFY_KWARGS",
]


RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__COMPANY: Final[str] = "label-primary"
RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__OPENSOURCE: Final[str] = "label-success"
RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__FREELANCE: Final[str] = "label-warning"
RESUME_PYPROJECT_PATH: Final[str] = "pyproject.toml"

JSON_DUMPS_KWARGS: Final[Dict[str, Any]] = {"indent": 2, "ensure_ascii": False}
JSON_EXCLUDE_FIELDS: Final = {  # noqa: ECE001
    "basics": {"location": {"name"}, "avatar": True},
    "projects": {"__all__": {"company": {"__all__": {"metadata"}}}},
    "metadata": True,
}

HTML_MONTH_YEAR_FORMAT: Final[str] = "%b. %Y"
HTML_DAY_MONTH_YEAR_FORMAT: Final[str] = "%d.%m.%Y"
HTML_YEAR_FORMAT: Final[str] = "%Y"
HTML_TEMPLATES_PACKAGE: Final[str] = "resume"
HTML_TEMPLATE_NAME: Final[str] = "resume.html.jinja"
HTML_PRETTIFY_KWARGS: Final[Dict[str, Any]] = {
    "indent": 4,
    "void_element_close_prefix": "/",
}
