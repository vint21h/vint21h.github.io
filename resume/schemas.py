from datetime import date
from typing import List, Optional

from pydantic import HttpUrl, EmailStr, BaseModel


__all__: List[str] = [
    "ResumeLanguage",
    "ResumeWork",
    "ResumeEducation",
    "ResumeProject",
    "ResumeBasics",
    "ResumeProjectCompany",
    "ResumeProjectCompanyMetadata",
    "ResumeProjectTechnology",
    "ResumeWorkCompany",
    "ResumeSkillOrTechnology",
    "ResumeProjectResponsibility",
    "ResumeEducationInstitution",
    "ResumeBasicsMetadata",
    "ResumeBasicsLocation",
    "ResumeBasicsMetadataLanguage",
    "BaseResume",
]


class ResumeBasicsLocation(BaseModel):
    """Resume basics location field representation."""

    name: str
    country_code: str


class ResumeBasicsMetadataLanguage(BaseModel):
    """Resume basics metadata language field representation."""

    name: str
    language_code: str


class ResumeBasicsMetadata(BaseModel):
    """Resume basics metadata field representation."""

    updated: date
    language: ResumeBasicsMetadataLanguage
    version: Optional[str]


class ResumeBasics(BaseModel):
    """Resume basics field representation."""

    name: str
    label: str
    email: EmailStr
    linkedin: HttpUrl
    site: HttpUrl
    location: ResumeBasicsLocation
    metadata: ResumeBasicsMetadata


class ResumeWorkCompany(BaseModel):
    """Resume work company list field representation."""

    original: str
    en: Optional[str]


class ResumeWork(BaseModel):
    """Resume work list field representation."""

    company: ResumeWorkCompany
    position: str
    website: Optional[HttpUrl]
    start_date: date
    end_date: Optional[date]


class ResumeEducationInstitution(BaseModel):
    """Resume education institution field representation."""

    original: str
    en: Optional[str]


class ResumeEducation(BaseModel):
    """Resume education list field representation."""

    institution: ResumeEducationInstitution
    start_date: date
    end_date: Optional[date]


class ResumeSkillOrTechnology(BaseModel):
    """Resume skills and technologies list field representation."""

    name: str


class ResumeLanguage(BaseModel):
    """Resume languages list field representation."""

    language: str
    fluency: str


class ResumeProjectTechnology(BaseModel):
    """Resume projects list technologies field representation."""

    name: str


class ResumeProjectResponsibility(BaseModel):
    """Resume projects list responsibilities field representation."""

    name: str


class ResumeProjectCompanyMetadata(BaseModel):
    """Resume projects list company metadata field representation."""

    css_class: str


class ResumeProjectCompany(BaseModel):
    """Resume projects list company field representation."""

    name: str
    metadata: Optional[ResumeProjectCompanyMetadata]


class ResumeProject(BaseModel):
    """Resume projects list field representation."""

    name: str
    start_date: date
    end_date: Optional[date]
    summary: Optional[str]
    url: Optional[HttpUrl]
    company: List[ResumeProjectCompany]
    role: Optional[str]
    responsibilities: Optional[List[ResumeProjectResponsibility]]
    technologies: Optional[List[ResumeProjectTechnology]]


class BaseResume(BaseModel):
    """
    Base resume representation.

    An opinionated imagination of "https://jsonresume.org/".
    All fields representation are also opinionated.
    """

    basics: ResumeBasics
    work: Optional[List[ResumeWork]]
    education: Optional[List[ResumeEducation]]
    skills_and_technologies: Optional[List[ResumeSkillOrTechnology]]
    languages: Optional[List[ResumeLanguage]]
    projects: Optional[List[ResumeProject]]
