from datetime import date
from typing import List

from resume.constants import (
    RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__FREELANCE,
    RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__OPENSOURCE,
    RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__REGULAR,
)
from resume.schemas import (
    BaseResume,
    ResumeBasics,
    ResumeBasicsLocation,
    ResumeBasicsMetadata,
    ResumeBasicsMetadataLanguage,
    ResumeEducation,
    ResumeEducationInstitution,
    ResumeLanguage,
    ResumeProject,
    ResumeProjectCompany,
    ResumeProjectCompanyMetadata,
    ResumeProjectResponsibility,
    ResumeProjectTechnology,
    ResumeSkillOrTechnology,
    ResumeWork,
    ResumeWorkCompany,
)
from resume.utils import get_version

__all__: List[str] = ["RESUME"]


RESUME = BaseResume(
    basics=ResumeBasics(
        name="Oleksii Andrushevych",
        label="Python/Django developer",
        email="vint21h@vint21h.pp.ua",
        linkedin="https://www.linkedin.com/in/vint21h/",
        site="https://www.vint21h.pp.ua/",
        location=ResumeBasicsLocation(
            name="Ukraine",
            country_code="UA",
        ),
        metadata=ResumeBasicsMetadata(
            language=ResumeBasicsMetadataLanguage(
                name="English",
                language_code="en",
            ),
            updated=date(year=2023, month=2, day=10),
            version=get_version(),
        ),
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
        ResumeSkillOrTechnology(
            name="Salt Stack",
        ),
        ResumeSkillOrTechnology(
            name="Sphinx",
        ),
        ResumeSkillOrTechnology(
            name="Fabric",
        ),
        ResumeSkillOrTechnology(
            name="Multithreading",
        ),
        ResumeSkillOrTechnology(
            name="AnyChart",
        ),
        ResumeSkillOrTechnology(
            name="amCharts",
        ),
        ResumeSkillOrTechnology(
            name="PostgreSQL FTS",
        ),
        ResumeSkillOrTechnology(
            name="Mercurial",
        ),
        ResumeSkillOrTechnology(
            name="CVS",
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
    projects=[
        ResumeProject(
            name="nagios-notification-jabber",
            start_date=date(year=2011, month=3, day=1),
            summary="Notifications via jabber Nagios plugin.",
            url="https://github.com/vint21h/nagios-notification-jabber/",
            company=[
                ResumeProjectCompany(
                    name="Open Source",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__OPENSOURCE,
                    ),
                )
            ],
        ),
        ResumeProject(
            name="nagios-check-hddtemp",
            start_date=date(year=2011, month=9, day=1),
            summary="Check HDD temperature Nagios plugin.",
            url="https://github.com/vint21h/nagios-check-hddtemp/",
            company=[
                ResumeProjectCompany(
                    name="Open Source",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__OPENSOURCE,
                    ),
                )
            ],
        ),
        ResumeProject(
            name="GrainUkraine",
            start_date=date(year=2011, month=10, day=1),
            end_date=date(year=2019, month=4, day=28),
            summary="Grain Ukraine - modern bulletin board for ukrainian suppliers of agricultural commodities and services.",
            url="http://www.grainukraine.com/",
            company=[
                ResumeProjectCompany(
                    name="DCOD",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__REGULAR,
                    ),
                )
            ],
            role="Python/Django developer",
            responsibilities=[
                ResumeProjectResponsibility(
                    name="Project architecture development and implementation",
                ),
                ResumeProjectResponsibility(
                    name="Main modules implementation",
                ),
                ResumeProjectResponsibility(
                    name="Frontend development",
                ),
                ResumeProjectResponsibility(
                    name="Deploy development and implementation",
                ),
            ],
            technologies=[
                ResumeProjectTechnology(
                    name="Python",
                ),
                ResumeProjectTechnology(
                    name="Django",
                ),
                ResumeProjectTechnology(
                    name="JavaScript",
                ),
                ResumeProjectTechnology(
                    name="jQuery",
                ),
                ResumeProjectTechnology(
                    name="HTML",
                ),
                ResumeProjectTechnology(
                    name="CSS",
                ),
                ResumeProjectTechnology(
                    name="PostgreSQL",
                ),
                ResumeProjectTechnology(
                    name="Sphinx",
                ),
                ResumeProjectTechnology(
                    name="Memcached",
                ),
                ResumeProjectTechnology(
                    name="Redis",
                ),
                ResumeProjectTechnology(
                    name="Nginx",
                ),
                ResumeProjectTechnology(
                    name="Fabric",
                ),
                ResumeProjectTechnology(
                    name="Salt Stack",
                ),
                ResumeProjectTechnology(
                    name="Amazon Web Services (AWS)",
                ),
            ],
        ),
        ResumeProject(
            name="AgroChart",
            start_date=date(year=2012, month=4, day=1),
            end_date=date(year=2019, month=5, day=28),
            summary="AgroChart - Prices. Trading. Balances. Statistics. News. Forecasts.",
            url="http://www.agrochart.com/",
            company=[
                ResumeProjectCompany(
                    name="DCOD",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__REGULAR,
                    ),
                )
            ],
            role="Python/Django developer",
            responsibilities=[
                ResumeProjectResponsibility(
                    name="Project architecture development and implementation",
                ),
                ResumeProjectResponsibility(
                    name="Main modules implementation",
                ),
                ResumeProjectResponsibility(
                    name="Distributed data sources parsing architecture development and implementation",
                ),
                ResumeProjectResponsibility(
                    name="Distributed data caching system architecture development and implementation",
                ),
                ResumeProjectResponsibility(
                    name="Distributed cache invalidation system architecture development and implementation",
                ),
                ResumeProjectResponsibility(
                    name="Frontend development",
                ),
                ResumeProjectResponsibility(
                    name="Deploy development and implementation",
                ),
            ],
            technologies=[
                ResumeProjectTechnology(
                    name="Python",
                ),
                ResumeProjectTechnology(
                    name="Django",
                ),
                ResumeProjectTechnology(
                    name="Multithreading",
                ),
                ResumeProjectTechnology(
                    name="JavaScript",
                ),
                ResumeProjectTechnology(
                    name="jQuery",
                ),
                ResumeProjectTechnology(
                    name="Backbone.js",
                ),
                ResumeProjectTechnology(
                    name="Underscore.js",
                ),
                ResumeProjectTechnology(
                    name="Ext JS",
                ),
                ResumeProjectTechnology(
                    name="AnyChart",
                ),
                ResumeProjectTechnology(
                    name="amCharts",
                ),
                ResumeProjectTechnology(
                    name="Highcharts",
                ),
                ResumeProjectTechnology(
                    name="HTML",
                ),
                ResumeProjectTechnology(
                    name="CSS",
                ),
                ResumeProjectTechnology(
                    name="SASS",
                ),
                ResumeProjectTechnology(
                    name="gulp.js",
                ),
                ResumeProjectTechnology(
                    name="Celery",
                ),
                ResumeProjectTechnology(
                    name="RabbitMQ",
                ),
                ResumeProjectTechnology(
                    name="MySQL",
                ),
                ResumeProjectTechnology(
                    name="PostgreSQL",
                ),
                ResumeProjectTechnology(
                    name="PostgreSQL FTS",
                ),
                ResumeProjectTechnology(
                    name="Memcached",
                ),
                ResumeProjectTechnology(
                    name="Redis",
                ),
                ResumeProjectTechnology(
                    name="Nginx",
                ),
                ResumeProjectTechnology(
                    name="Fabric",
                ),
                ResumeProjectTechnology(
                    name="Salt Stack",
                ),
                ResumeProjectTechnology(
                    name="Ansible",
                ),
                ResumeProjectTechnology(
                    name="Amazon Web Services (AWS)",
                ),
            ],
        ),
        ResumeProject(
            name="DioraShop",
            start_date=date(year=2012, month=11, day=1),
            end_date=date(year=2013, month=9, day=1),
            summary="Handiwork commodities online shop.",
            url="http://www.diorashop.com/",
            company=[
                ResumeProjectCompany(
                    name="Freelance",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__FREELANCE,
                    ),
                )
            ],
            role="Python/Django developer",
            responsibilities=[
                ResumeProjectResponsibility(
                    name="Project architecture development and implementation",
                ),
                ResumeProjectResponsibility(
                    name="Main modules implementation",
                ),
                ResumeProjectResponsibility(
                    name="Frontend development",
                ),
                ResumeProjectResponsibility(
                    name="Third part services integration",
                ),
                ResumeProjectResponsibility(
                    name="Deploy development and implementation",
                ),
            ],
            technologies=[
                ResumeProjectTechnology(
                    name="Python",
                ),
                ResumeProjectTechnology(
                    name="Django",
                ),
                ResumeProjectTechnology(
                    name="JavaScript",
                ),
                ResumeProjectTechnology(
                    name="jQuery",
                ),
                ResumeProjectTechnology(
                    name="jQuery UI",
                ),
                ResumeProjectTechnology(
                    name="HTML",
                ),
                ResumeProjectTechnology(
                    name="CSS",
                ),
                ResumeProjectTechnology(
                    name="Celery",
                ),
                ResumeProjectTechnology(
                    name="RabbitMQ",
                ),
                ResumeProjectTechnology(
                    name="PostgreSQL",
                ),
                ResumeProjectTechnology(
                    name="Memcached",
                ),
                ResumeProjectTechnology(
                    name="Redis",
                ),
                ResumeProjectTechnology(
                    name="Nginx",
                ),
                ResumeProjectTechnology(
                    name="Fabric",
                ),
                ResumeProjectTechnology(
                    name="Amazon Web Services (AWS)",
                ),
                ResumeProjectTechnology(
                    name="YouTube API",
                ),
            ],
        ),
        ResumeProject(
            name="nagios-notification-google-calendar",
            start_date=date(year=2013, month=1, day=1),
            summary="Notifications via Google Calendar Nagios plugin.",
            url="https://github.com/vint21h/nagios-notification-google-calendar/",
            company=[
                ResumeProjectCompany(
                    name="Open Source",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__OPENSOURCE,
                    ),
                )
            ],
        ),
        ResumeProject(
            name="DCOD",
            start_date=date(year=2013, month=1, day=1),
            end_date=date(year=2019, month=5, day=28),
            summary="DCOD site.",
            url="http://www.d-cod.com/",
            company=[
                ResumeProjectCompany(
                    name="DCOD",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__REGULAR,
                    ),
                )
            ],
            role="Python/Django developer",
            responsibilities=[
                ResumeProjectResponsibility(
                    name="Page generation system development",
                ),
                ResumeProjectResponsibility(
                    name="Frontend development",
                ),
                ResumeProjectResponsibility(
                    name="Deploy development and implementation",
                ),
            ],
            technologies=[
                ResumeProjectTechnology(
                    name="Python",
                ),
                ResumeProjectTechnology(
                    name="Django",
                ),
                ResumeProjectTechnology(
                    name="JavaScript",
                ),
                ResumeProjectTechnology(
                    name="jQuery",
                ),
                ResumeProjectTechnology(
                    name="HTML",
                ),
                ResumeProjectTechnology(
                    name="CSS",
                ),
                ResumeProjectTechnology(
                    name="Cactus",
                ),
                ResumeProjectTechnology(
                    name="Amazon Web Services (AWS)",
                ),
                ResumeProjectTechnology(
                    name="Ansible",
                ),
            ],
        ),
        ResumeProject(
            name="django-po2xls",
            start_date=date(year=2013, month=6, day=1),
            summary="Convert gettext .po files to .xls.",
            url="https://github.com/vint21h/django-po2xls/",
            company=[
                ResumeProjectCompany(
                    name="Open Source",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__OPENSOURCE,
                    ),
                )
            ],
        ),
        ResumeProject(
            name="bstRating",
            start_date=date(year=2013, month=8, day=1),
            end_date=date(year=2014, month=9, day=1),
            summary="Free companies catalog/rating.",
            url="http://www.bstrating.com/",
            company=[
                ResumeProjectCompany(
                    name="DCOD",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__REGULAR,
                    ),
                )
            ],
            role="Python/Django developer",
            responsibilities=[
                ResumeProjectResponsibility(
                    name="Project architecture development and implementation",
                ),
                ResumeProjectResponsibility(
                    name="Main modules implementation",
                ),
                ResumeProjectResponsibility(
                    name="Frontend development",
                ),
                ResumeProjectResponsibility(
                    name="Deploy development and implementation",
                ),
            ],
            technologies=[
                ResumeProjectTechnology(
                    name="Python",
                ),
                ResumeProjectTechnology(
                    name="Django",
                ),
                ResumeProjectTechnology(
                    name="JavaScript",
                ),
                ResumeProjectTechnology(
                    name="jQuery",
                ),
                ResumeProjectTechnology(
                    name="Backbone.js",
                ),
                ResumeProjectTechnology(
                    name="HTML",
                ),
                ResumeProjectTechnology(
                    name="CSS",
                ),
                ResumeProjectTechnology(
                    name="PostgreSQL",
                ),
                ResumeProjectTechnology(
                    name="Memcached",
                ),
                ResumeProjectTechnology(
                    name="Redis",
                ),
                ResumeProjectTechnology(
                    name="Nginx",
                ),
                ResumeProjectTechnology(
                    name="Amazon Web Services (AWS)",
                ),
                ResumeProjectTechnology(
                    name="Salt Stack",
                ),
            ],
        ),
    ],
)
