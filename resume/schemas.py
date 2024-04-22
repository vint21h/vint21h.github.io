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
    "ResumeMetadata",
    "ResumeBasicsLocation",
    "ResumeMetadataLanguage",
    "Resume",
    "ResumeBasicsAvatar",
    "ResumeBasicsAvatarEasterEgg",
]


class ResumeBasicsLocation(CamelModel):
    """Resume basics location field representation."""

    name: str
    country_code: str


class ResumeMetadataLanguage(CamelModel):
    """Resume metadata language field representation."""

    name: str
    language_code: str


class ResumeMetadata(CamelModel):
    """Resume metadata field representation."""

    updated: date
    language: ResumeMetadataLanguage
    version: Optional[str] = None


class ResumeBasicsAvatarEasterEgg(CamelModel):
    """Resume basics avatar easter-egg field representation."""

    path: str
    nickname: str


class ResumeBasicsAvatar(CamelModel):
    """Resume basics avatar field representation."""

    path: str
    width: int
    height: int
    easter_egg: Optional[ResumeBasicsAvatarEasterEgg] = None


class ResumeBasics(CamelModel):
    """Resume basics field representation."""

    name: str
    label: str
    email: EmailStr
    linkedin: HttpUrl
    site: HttpUrl
    location: ResumeBasicsLocation
    avatar: Optional[ResumeBasicsAvatar] = None
    summary: Optional[str] = None


class ResumeWorkCompany(CamelModel):
    """Resume work company list field representation."""

    original: str
    en: Optional[str] = None


class ResumeWork(CamelModel):
    """Resume work list field representation."""

    company: ResumeWorkCompany
    position: str
    website: Optional[HttpUrl] = None
    start_date: date
    end_date: Optional[date] = None


class ResumeEducationInstitution(CamelModel):
    """Resume education institution field representation."""

    original: str
    en: Optional[str] = None


class ResumeEducation(CamelModel):
    """Resume education list field representation."""

    institution: ResumeEducationInstitution
    start_date: date
    end_date: Optional[date] = None


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
    metadata: Optional[ResumeProjectCompanyMetadata] = None


class ResumeProject(CamelModel):
    """Resume projects list field representation."""

    name: str
    start_date: date
    end_date: Optional[date] = None
    summary: str
    url: Optional[HttpUrl] = None
    company: List[ResumeProjectCompany] = None
    role: Optional[str] = None
    responsibilities: Optional[List[ResumeProjectResponsibility]] = None
    technologies: Optional[List[ResumeProjectTechnology]] = None


class Resume(CamelModel):
    """
    Resume representation.

    Deeply opinionated imagination of the "https://jsonresume.org/".
    All fields representation are also opinionated.
    """

    basics: ResumeBasics
    work: Optional[List[ResumeWork]] = None
    education: Optional[List[ResumeEducation]] = None
    skills_and_technologies: Optional[List[ResumeSkillOrTechnology]] = None
    languages: Optional[List[ResumeLanguage]] = None
    projects: Optional[List[ResumeProject]] = None
    metadata: Optional[ResumeMetadata] = None
