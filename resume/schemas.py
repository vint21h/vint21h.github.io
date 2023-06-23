from datetime import date
from typing import List, Optional

from pydantic import HttpUrl, EmailStr
from fastapi_camelcase import CamelModel


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
    "Resume",
    "ResumeBasicsAvatar",
    "ResumeBasicsAvatarEasterEgg",
]


class ResumeBasicsLocation(CamelModel):
    """Resume basics location field representation."""

    name: str
    country_code: str


class ResumeBasicsMetadataLanguage(CamelModel):
    """Resume basics metadata language field representation."""

    name: str
    language_code: str


class ResumeBasicsMetadata(CamelModel):
    """Resume basics metadata field representation."""

    updated: date
    language: ResumeBasicsMetadataLanguage
    version: Optional[str]


class ResumeBasicsAvatarEasterEgg(CamelModel):
    """Resume basics avatar easter-egg field representation."""

    path: str
    nickname: str


class ResumeBasicsAvatar(CamelModel):
    """Resume basics avatar field representation."""

    path: str
    width: int
    height: int
    easter_egg: Optional[ResumeBasicsAvatarEasterEgg]


class ResumeBasics(CamelModel):
    """Resume basics field representation."""

    name: str
    label: str
    email: EmailStr
    linkedin: HttpUrl
    site: HttpUrl
    location: ResumeBasicsLocation
    metadata: Optional[ResumeBasicsMetadata]
    avatar: Optional[ResumeBasicsAvatar]


class ResumeWorkCompany(CamelModel):
    """Resume work company list field representation."""

    original: str
    en: Optional[str]


class ResumeWork(CamelModel):
    """Resume work list field representation."""

    company: ResumeWorkCompany
    position: str
    website: Optional[HttpUrl]
    start_date: date
    end_date: Optional[date]


class ResumeEducationInstitution(CamelModel):
    """Resume education institution field representation."""

    original: str
    en: Optional[str]


class ResumeEducation(CamelModel):
    """Resume education list field representation."""

    institution: ResumeEducationInstitution
    start_date: date
    end_date: Optional[date]


class ResumeSkillOrTechnology(CamelModel):
    """Resume skills and technologies list field representation."""

    name: str


class ResumeLanguage(CamelModel):
    """Resume languages list field representation."""

    language: str
    fluency: str


class ResumeProjectTechnology(CamelModel):
    """Resume projects list technologies field representation."""

    name: str


class ResumeProjectResponsibility(CamelModel):
    """Resume projects list responsibilities field representation."""

    name: str


class ResumeProjectCompanyMetadata(CamelModel):
    """Resume projects list company metadata field representation."""

    css_class: str


class ResumeProjectCompany(CamelModel):
    """Resume projects list company field representation."""

    name: str
    metadata: Optional[ResumeProjectCompanyMetadata]


class ResumeProject(CamelModel):
    """Resume projects list field representation."""

    name: str
    start_date: date
    end_date: Optional[date]
    summary: str
    url: Optional[HttpUrl]
    company: List[ResumeProjectCompany]
    role: Optional[str]
    responsibilities: Optional[List[ResumeProjectResponsibility]]
    technologies: Optional[List[ResumeProjectTechnology]]


class Resume(CamelModel):
    """
    Resume representation.

    Deeply opinionated imagination of the "https://jsonresume.org/".
    All fields representation are also opinionated.
    """

    basics: ResumeBasics
    work: Optional[List[ResumeWork]]
    education: Optional[List[ResumeEducation]]
    skills_and_technologies: Optional[List[ResumeSkillOrTechnology]]
    languages: Optional[List[ResumeLanguage]]
    projects: Optional[List[ResumeProject]]
