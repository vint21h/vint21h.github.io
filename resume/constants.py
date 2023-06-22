from typing import Any, Set, Dict, List, Final, Union


__all__: List[str] = [
    "RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__REGULAR",
    "RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__OPENSOURCE",
    "RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__FREELANCE",
    "RESUME_PYPROJECT_PATH",
    "JSON_DUMPS_KWARGS",
    "JSON_EXCLUDE_FIELDS",
]


RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__REGULAR: Final[str] = "label-primary"
RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__OPENSOURCE: Final[str] = "label-success"
RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__FREELANCE: Final[str] = "label-warning"
RESUME_PYPROJECT_PATH: Final[str] = "pyproject.toml"

JSON_DUMPS_KWARGS: Final[Dict[str, Any]] = {"indent": 2, "ensure_ascii": False}
JSON_EXCLUDE_FIELDS: Final[  # noqa: ECE001,TAE002
    Dict[
        str,
        Union[
            Dict[str, Union[Set[str], bool]], Dict[str, Dict[str, Dict[str, Set[str]]]]
        ],
    ]
] = {
    "basics": {"location": {"name"}, "metadata": True},
    "projects": {"__all__": {"company": {"__all__": {"metadata"}}}},
}
