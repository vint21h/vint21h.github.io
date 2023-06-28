from typing import Any, Dict, List, Final


__all__: List[str] = [
    "RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__REGULAR",
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


RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__REGULAR: Final[str] = "bg-primary"
RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__OPENSOURCE: Final[str] = "bg-success"
RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__FREELANCE: Final[str] = "bg-warning"
RESUME_PYPROJECT_PATH: Final[str] = "pyproject.toml"

JSON_DUMPS_KWARGS: Final[Dict[str, Any]] = {"indent": 2, "ensure_ascii": False}
JSON_EXCLUDE_FIELDS: Final = {  # noqa: ECE001
    "basics": {"location": {"name"}, "avatar": True},
    "projects": {"__all__": {"company": {"__all__": {"metadata"}}}},
    "metadata": True,
}

HTML_MONTH_YEAR_FORMAT: str = "%b. %Y"
HTML_DAY_MONTH_YEAR_FORMAT: str = "%d.%m.%Y"
HTML_YEAR_FORMAT: str = "%Y"
HTML_TEMPLATES_PACKAGE: str = "resume"
HTML_TEMPLATE_NAME: str = "resume.html.jinja"
HTML_PRETTIFY_KWARGS: Final[Dict[str, Any]] = {
    "indent": 4,
    "void_element_close_prefix": "/",
}
