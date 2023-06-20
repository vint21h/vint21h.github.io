#!/usr/bin/env python

from datetime import date
from typing import List, Optional

from pydantic import BaseModel, EmailStr, HttpUrl

__all__: List[str] = []


class ResumeBasicsLocation(BaseModel):
    """Resume basics location field representation."""

    country_code: str


class ResumeBasics(BaseModel):
    """Resume basics field representation."""

    name: str
    label: str
    email: EmailStr
    linkedin: HttpUrl
    site: HttpUrl
    location: ResumeBasicsLocation
    updated: date


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


class ResumeProjectCompany(BaseModel):
    """Resume projects list company field representation."""

    name: str


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


if __name__ == "__main__":
    # TODO (@vint21h): print resume here
    resume = BaseResume(
        basics=ResumeBasics(
            name="Oleksii Andrushevych",
            label="Python/Django developer",
            email="vint21h@vint21h.pp.ua",
            linkedin="https://www.linkedin.com/in/vint21h/",
            site="https://www.vint21h.pp.ua/",
            location=ResumeBasicsLocation(
                country_code="UA",
            ),
            updated=date(year=2023, month=2, day=10),
        ),
        work=[
            ResumeWork(
                company=ResumeWorkCompany(
                    original="Anadea",
                ),
                position="Python/Django developer",
                website="https://anadea.info/",
                start_date=date(year=2020, month=9, day=7),
                end_date=date(year=2023, month=1, day=1),
            ),
            ResumeWork(
                company=ResumeWorkCompany(
                    original="Freelance",
                ),
                position="Python/Django developer",
                start_date=date(year=2020, month=4, day=27),
                end_date=date(year=2020, month=8, day=28),
            ),
            ResumeWork(
                company=ResumeWorkCompany(
                    original="Zakaz.ua",
                ),
                position="Python developer",
                website="https://zakaz.ua/",
                start_date=date(year=2019, month=10, day=21),
                end_date=date(year=2020, month=1, day=27),
            ),
            ResumeWork(
                company=ResumeWorkCompany(
                    original="DCOD",
                ),
                position="Python/Django developer",
                website="http://d-cod.com/",
                start_date=date(year=2011, month=10, day=25),
                end_date=date(year=2019, month=5, day=28),
            ),
            ResumeWork(
                company=ResumeWorkCompany(
                    original='ФПТП "ДРФЦ"',
                    en='FPTP "DRFC"',
                ),
                position="System administrator",
                start_date=date(year=2010, month=11, day=25),
                end_date=date(year=2011, month=8, day=11),
            ),
            ResumeWork(
                company=ResumeWorkCompany(
                    original='ООО "Норма-Пресс"',
                    en='"Norma-Press" Ltd.',
                ),
                position="System administrator",
                start_date=date(year=2009, month=10, day=1),
                end_date=date(year=2010, month=11, day=1),
            ),
            ResumeWork(
                company=ResumeWorkCompany(
                    original='ООО "Информбюро"',
                    en='"InformBureau" Ltd.',
                ),
                position="Perl developer",
                start_date=date(year=2009, month=10, day=1),
                end_date=date(year=2010, month=11, day=1),
            ),
            ResumeWork(
                company=ResumeWorkCompany(
                    original='ООО "Донбасс Он-Лайн"',
                    en='"Donbass-Online" Ltd.',
                ),
                position="Perl developer",
                start_date=date(year=2008, month=8, day=29),
                end_date=date(year=2009, month=4, day=1),
            ),
            ResumeWork(
                company=ResumeWorkCompany(
                    original='ООО "Алекс Восток"',
                    en='"Alex-Vostok" Ltd.',
                ),
                position="Perl developer",
                start_date=date(year=2007, month=8, day=1),
                end_date=date(year=2008, month=7, day=28),
            ),
        ],
        education=[
            ResumeEducation(
                institution=ResumeEducationInstitution(
                    original="Донецький Державний Інститут Штучного Інтелекту",
                    en="State Institute of Artificial Intelligence",
                ),
                start_date=date(year=2004, month=1, day=1),
                end_date=date(year=2006, month=12, day=31),
            ),
        ],
        skills_and_technologies=[
            ResumeSkillOrTechnology(
                name="Python",
            ),
            ResumeSkillOrTechnology(
                name="PostgreSQL",
            ),
            ResumeSkillOrTechnology(
                name="Perl",
            ),
            ResumeSkillOrTechnology(
                name="Django",
            ),
            ResumeSkillOrTechnology(
                name="Linux",
            ),
            ResumeSkillOrTechnology(
                name="Git",
            ),
            ResumeSkillOrTechnology(
                name="CentOS",
            ),
            ResumeSkillOrTechnology(
                name="Fedora",
            ),
            ResumeSkillOrTechnology(
                name="Nagios",
            ),
            ResumeSkillOrTechnology(
                name="Subversion",
            ),
            ResumeSkillOrTechnology(
                name="JavaScript",
            ),
            ResumeSkillOrTechnology(
                name="MySQL",
            ),
            ResumeSkillOrTechnology(
                name="SQL",
            ),
            ResumeSkillOrTechnology(
                name="Backbone.js",
            ),
            ResumeSkillOrTechnology(
                name="Underscore.js",
            ),
            ResumeSkillOrTechnology(
                name="Redis",
            ),
            ResumeSkillOrTechnology(
                name="Memcached",
            ),
            ResumeSkillOrTechnology(
                name="Celery",
            ),
            ResumeSkillOrTechnology(
                name="Nginx",
            ),
            ResumeSkillOrTechnology(
                name="JSON",
            ),
            ResumeSkillOrTechnology(
                name="RabbitMQ",
            ),
            ResumeSkillOrTechnology(
                name="Amazon Web Services (AWS)",
            ),
            ResumeSkillOrTechnology(
                name="Newrelic",
            ),
            ResumeSkillOrTechnology(
                name="Highcharts",
            ),
            ResumeSkillOrTechnology(
                name="jQuery",
            ),
            ResumeSkillOrTechnology(
                name="PHP",
            ),
            ResumeSkillOrTechnology(
                name="CSS",
            ),
            ResumeSkillOrTechnology(
                name="AJAX",
            ),
            ResumeSkillOrTechnology(
                name="XML",
            ),
            ResumeSkillOrTechnology(
                name="jQuery UI",
            ),
            ResumeSkillOrTechnology(
                name="Google Calendar API",
            ),
            ResumeSkillOrTechnology(
                name="Sentry",
            ),
            ResumeSkillOrTechnology(
                name="Google Maps API",
            ),
            ResumeSkillOrTechnology(
                name="pnp4nagios",
            ),
            ResumeSkillOrTechnology(
                name="Ext JS",
            ),
            ResumeSkillOrTechnology(
                name="XML-RPC",
            ),
            ResumeSkillOrTechnology(
                name="GTFS",
            ),
            ResumeSkillOrTechnology(
                name="REST",
            ),
            ResumeSkillOrTechnology(
                name="Remote Work",
            ),
            ResumeSkillOrTechnology(
                name="Ansible",
            ),
            ResumeSkillOrTechnology(
                name="Solidity",
            ),
            ResumeSkillOrTechnology(
                name="Web3",
            ),
            ResumeSkillOrTechnology(
                name="GNU Make",
            ),
            ResumeSkillOrTechnology(
                name="Webpack",
            ),
            ResumeSkillOrTechnology(
                name="gulp.js",
            ),
            ResumeSkillOrTechnology(
                name="SASS",
            ),
            ResumeSkillOrTechnology(
                name="GraphQL",
            ),
            ResumeSkillOrTechnology(
                name="WebSockets",
            ),
            ResumeSkillOrTechnology(
                name="Unit Tests",
            ),
            ResumeSkillOrTechnology(
                name="Functional Tests",
            ),
            ResumeSkillOrTechnology(
                name="Integration Tests",
            ),
            ResumeSkillOrTechnology(
                name="Pushpin",
            ),
            ResumeSkillOrTechnology(
                name="HAProxy",
            ),
            ResumeSkillOrTechnology(
                name="Docker",
            ),
            ResumeSkillOrTechnology(
                name="docker-compose",
            ),
            ResumeSkillOrTechnology(
                name="Vagrant",
            ),
            ResumeSkillOrTechnology(
                name="consul-templaterb",
            ),
            ResumeSkillOrTechnology(
                name="Apache CouchDB",
            ),
            ResumeSkillOrTechnology(
                name="Apache Solr",
            ),
            ResumeSkillOrTechnology(
                name="RQ",
            ),
            ResumeSkillOrTechnology(
                name="Python Code Analysis/Quality tools",
            ),
            ResumeSkillOrTechnology(
                name="aiohttp",
            ),
            ResumeSkillOrTechnology(
                name="peewee",
            ),
            ResumeSkillOrTechnology(
                name="OpenAPI",
            ),
            ResumeSkillOrTechnology(
                name="GitLab CI/CD",
            ),
            ResumeSkillOrTechnology(
                name="Dokku",
            ),
            ResumeSkillOrTechnology(
                name="Dart",
            ),
            ResumeSkillOrTechnology(
                name="DAAP",
            ),
            ResumeSkillOrTechnology(
                name="gjs",
            ),
            ResumeSkillOrTechnology(
                name="gRPC",
            ),
            ResumeSkillOrTechnology(
                name="PostGIS",
            ),
            ResumeSkillOrTechnology(
                name="Bitbucket Pipelines",
            ),
            ResumeSkillOrTechnology(
                name="GitHub Actions",
            ),
            ResumeSkillOrTechnology(
                name="Django REST framework",
            ),
            ResumeSkillOrTechnology(
                name="Vimeo API",
            ),
            ResumeSkillOrTechnology(
                name="SQS",
            ),
            ResumeSkillOrTechnology(
                name="YouTube API",
            ),
        ],
        languages=[
            ResumeLanguage(
                language="English",
                fluency="Professional working proficiency",
            ),
            ResumeLanguage(
                language="Ukrainian",
                fluency="Native or bilingual proficiency",
            ),
        ],
    )
