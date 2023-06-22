from typing import List
from datetime import date

from resume.utils import get_version
from resume.constants import (
    RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__REGULAR,
    RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__FREELANCE,
    RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__OPENSOURCE,
)
from resume.schemas import (
    BaseResume,
    ResumeWork,
    ResumeBasics,
    ResumeProject,
    ResumeLanguage,
    ResumeEducation,
    ResumeWorkCompany,
    ResumeBasicsLocation,
    ResumeBasicsMetadata,
    ResumeProjectCompany,
    ResumeProjectTechnology,
    ResumeSkillOrTechnology,
    ResumeEducationInstitution,
    ResumeProjectResponsibility,
    ResumeBasicsMetadataLanguage,
    ResumeProjectCompanyMetadata,
)


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
        ResumeSkillOrTechnology(
            name="Truffle",
        ),
        ResumeSkillOrTechnology(
            name="Ethereum",
        ),
        ResumeSkillOrTechnology(
            name="JavaScript Code Analysis/Quality tools",
        ),
        ResumeSkillOrTechnology(
            name="SASS Code Analysis/Quality tools",
        ),
        ResumeSkillOrTechnology(
            name="Docker Code Analysis/Quality tools",
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
                    name="Third-party services integration",
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
            summary="DCOD company site.",
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
        ResumeProject(
            name="django-mcadmin",
            start_date=date(year=2013, month=9, day=1),
            summary="Easy run management commands from Django admin.",
            url="https://github.com/vint21h/django-mcadmin/",
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
            name="FRB",
            start_date=date(year=2013, month=10, day=1),
            end_date=date(year=2015, month=11, day=1),
            summary="FINROSTBANK official site.",
            url="http://www.frb.com.ua/",
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
                    name="Celery",
                ),
                ResumeProjectTechnology(
                    name="RabbitMQ",
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
                    name="Amazon Web Services (AWS)",
                ),
                ResumeProjectTechnology(
                    name="Salt Stack",
                ),
            ],
        ),
        ResumeProject(
            name="AgroCharts",
            start_date=date(year=2013, month=12, day=1),
            end_date=date(year=2016, month=10, day=1),
            summary="Increase the information content and traffic to your website by placing on it the latest data of USDA reports, foreign trade and futures. Learn how to get the embed code for your site...",
            url="http://www.agrocharts.com/en/",
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
                    name="JavaScript",
                ),
                ResumeProjectTechnology(
                    name="jQuery",
                ),
                ResumeProjectTechnology(
                    name="Backbone.js",
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
                    name="Amazon Web Services (AWS)",
                ),
                ResumeProjectTechnology(
                    name="Salt Stack",
                ),
                ResumeProjectTechnology(
                    name="Ansible",
                ),
            ],
        ),
        ResumeProject(
            name="django-xls2po",
            start_date=date(year=2014, month=1, day=7),
            summary="django-xls2po is a Django management command to convert django-po2xls generated .xls files to .po files.",
            url="https://github.com/vint21h/django-xls2po/",
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
            name="anyfoodanyfeed",
            start_date=date(year=2014, month=3, day=1),
            end_date=date(year=2019, month=4, day=28),
            summary="Prevailing news resource of an agrarian theme. One of the best in Ukraine.",
            url="http://www.anyfoodanyfeed.com/",
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
                    name="JavaScript",
                ),
                ResumeProjectTechnology(
                    name="jQuery",
                ),
                ResumeProjectTechnology(
                    name="Backbone.js",
                ),
                ResumeProjectTechnology(
                    name="Highcharts",
                ),
                ResumeProjectTechnology(
                    name="Google Maps API",
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
                    name="Amazon Web Services (AWS)",
                ),
                ResumeProjectTechnology(
                    name="Salt Stack",
                ),
                ResumeProjectTechnology(
                    name="Ansible",
                ),
            ],
        ),
        ResumeProject(
            name="django-opensearch",
            start_date=date(year=2014, month=7, day=1),
            summary="Handle opensearch.xml for Django.",
            url="https://github.com/vint21h/django-opensearch/",
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
            name="redactor-plugins-lineheight",
            start_date=date(year=2014, month=10, day=1),
            summary="redactor-plugins-lineheight is a plugin for Redactor Text Editor (http://imperavi.com/redactor/) to set selected text line height.",
            url="https://github.com/vint21h/redactor-plugins-lineheight/",
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
            name="nagios-check-supervisord",
            start_date=date(year=2015, month=3, day=1),
            summary="Check supervisord programs status Nagios plugin.",
            url="https://github.com/vint21h/nagios-check-supervisord/",
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
            name="django-djcopyright",
            start_date=date(year=2015, month=5, day=1),
            summary="Django reusable app to show pretty formatted copyright years.",
            url="https://github.com/vint21h/django-djcopyright/",
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
            name="django-simple-help",
            start_date=date(year=2015, month=9, day=1),
            end_date=date(year=2019, month=5, day=28),
            summary="Django reusable application providing page help.",
            url="https://github.com/DCOD-OpenSource/django-simple-help/",
            company=[
                ResumeProjectCompany(
                    name="DCOD",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__REGULAR,
                    ),
                ),
                ResumeProjectCompany(
                    name="Open Source",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__OPENSOURCE,
                    ),
                ),
            ],
        ),
        ResumeProject(
            name="django-project-version",
            start_date=date(year=2016, month=2, day=1),
            summary="Django reusable app to show your project version.",
            url="https://github.com/DCOD-OpenSource/django-project-version/",
            company=[
                ResumeProjectCompany(
                    name="DCOD",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__REGULAR,
                    ),
                ),
                ResumeProjectCompany(
                    name="Open Source",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__OPENSOURCE,
                    ),
                ),
            ],
        ),
        ResumeProject(
            name="Van #1",
            start_date=date(year=2017, month=3, day=1),
            end_date=date(year=2018, month=8, day=1),
            summary="Van #1 - real coffee-rooms and shops on wheels, where it is comfortable to cook and to sell. This is a real catch for those who are willing to make their business profitable.",
            url="http://www.van1.eu/",
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
                    name="Third-party services integration",
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
                    name="Celery",
                ),
                ResumeProjectTechnology(
                    name="RabbitMQ",
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
                    name="Amazon Web Services (AWS)",
                ),
                ResumeProjectTechnology(
                    name="Ansible",
                ),
            ],
        ),
        ResumeProject(
            name="django-messages-to-bootstrap-notify.",
            start_date=date(year=2017, month=5, day=1),
            end_date=date(year=2019, month=5, day=28),
            summary="Show Django messages using bootstrap-notify.",
            url="https://github.com/DCOD-OpenSource/django-messages-to-bootstrap-notify/",
            company=[
                ResumeProjectCompany(
                    name="DCOD",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__REGULAR,
                    ),
                ),
                ResumeProjectCompany(
                    name="Open Source",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__OPENSOURCE,
                    ),
                ),
            ],
        ),
        ResumeProject(
            name="bootstrap-notify-simple-wrapper",
            start_date=date(year=2017, month=5, day=1),
            end_date=date(year=2019, month=5, day=28),
            summary="Simple wrapper around bootstrap-notify (https://github.com/mouse0270/bootstrap-notify/) to make your life easier.",
            url="https://github.com/DCOD-OpenSource/bootstrap-notify-simple-wrapper/",
            company=[
                ResumeProjectCompany(
                    name="DCOD",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__REGULAR,
                    ),
                ),
                ResumeProjectCompany(
                    name="Open Source",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__OPENSOURCE,
                    ),
                ),
            ],
        ),
        ResumeProject(
            name="django-read-only-admin",
            start_date=date(year=2017, month=5, day=1),
            summary="Really full Django read only admin implementation.",
            url="https://github.com/vint21h/django-read-only-admin/",
            company=[
                ResumeProjectCompany(
                    name="Open Source",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__OPENSOURCE,
                    ),
                ),
            ],
        ),
        ResumeProject(
            name="BSTfeed",
            start_date=date(year=2017, month=12, day=1),
            end_date=date(year=2019, month=5, day=28),
            summary="BSTfeed.com - your best independent source for grains, oilseeds and feedstuffs markets data.",
            url="https://www.bstfeed.com/",
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
                    name="JavaScript",
                ),
                ResumeProjectTechnology(
                    name="jQuery",
                ),
                ResumeProjectTechnology(
                    name="Backbone.js",
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
                    name="Amazon Web Services (AWS)",
                ),
                ResumeProjectTechnology(
                    name="Ansible",
                ),
            ],
        ),
        ResumeProject(
            name="EterArt",
            start_date=date(year=2018, month=12, day=1),
            end_date=date(year=2019, month=5, day=28),
            summary="EterArt - a unique blockchain platform for collecting and trading digital versions of art objects.",
            url="https://www.eterart.com/",
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
                    name="Partial Ethereum contract development and deploy implementation",
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
                    name="Multithreading",
                ),
                ResumeProjectTechnology(
                    name="Django",
                ),
                ResumeProjectTechnology(
                    name="JavaScript",
                ),
                ResumeProjectTechnology(
                    name="Webpack",
                ),
                ResumeProjectTechnology(
                    name="jQuery",
                ),
                ResumeProjectTechnology(
                    name="Backbone.js",
                ),
                ResumeProjectTechnology(
                    name="Web3",
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
                    name="Solidity",
                ),
                ResumeProjectTechnology(
                    name="Truffle",
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
                    name="PostgreSQL FTS",
                ),
                ResumeProjectTechnology(
                    name="Memcached",
                ),
                ResumeProjectTechnology(
                    name="Redis",
                ),
                ResumeProjectTechnology(
                    name="Ethereum",
                ),
                ResumeProjectTechnology(
                    name="Nginx",
                ),
                ResumeProjectTechnology(
                    name="Amazon Web Services (AWS)",
                ),
                ResumeProjectTechnology(
                    name="Ansible",
                ),
                ResumeProjectTechnology(
                    name="Python Code Analysis/Quality tools",
                ),
            ],
        ),
        ResumeProject(
            name="django-humans-txt",
            start_date=date(year=2019, month=8, day=1),
            summary="Handle humans.txt for Django.",
            url="https://github.com/vint21h/django-humans-txt/",
            company=[
                ResumeProjectCompany(
                    name="Open Source",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__OPENSOURCE,
                    ),
                ),
            ],
        ),
        ResumeProject(
            name="django-xicon",
            start_date=date(year=2018, month=10, day=21),
            summary="Handle modern bunch of site icons for Django.",
            url="https://github.com/vint21h/django-xicon/",
            company=[
                ResumeProjectCompany(
                    name="Open Source",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__OPENSOURCE,
                    ),
                ),
            ],
        ),
        ResumeProject(
            name="Zakaz.ua",
            start_date=date(year=2019, month=10, day=21),
            end_date=date(year=2020, month=1, day=27),
            summary="Hypermarket goods delivery service.",
            url="https://zakaz.ua/",
            company=[
                ResumeProjectCompany(
                    name="Zakaz.ua",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__REGULAR,
                    ),
                )
            ],
            role="Python developer",
            responsibilities=[
                ResumeProjectResponsibility(
                    name="Back-office business workflow requirements implementation",
                ),
                ResumeProjectResponsibility(
                    name="Business logic problems investigation",
                ),
                ResumeProjectResponsibility(
                    name="Back-end services intercommunication mechanisms development and implementation",
                ),
            ],
            technologies=[
                ResumeProjectTechnology(
                    name="Python",
                ),
                ResumeProjectTechnology(
                    name="Apache CouchDB",
                ),
                ResumeProjectTechnology(
                    name="Apache Solr",
                ),
                ResumeProjectTechnology(
                    name="RQ",
                ),
                ResumeProjectTechnology(
                    name="PostgreSQL",
                ),
                ResumeProjectTechnology(
                    name="Redis",
                ),
                ResumeProjectTechnology(
                    name="Docker",
                ),
                ResumeProjectTechnology(
                    name="docker-compose",
                ),
                ResumeProjectTechnology(
                    name="Python Code Analysis/Quality tools",
                ),
            ],
        ),
        ResumeProject(
            name="Under NDA",
            start_date=date(year=2020, month=4, day=28),
            end_date=date(year=2020, month=8, day=28),
            summary="Educational platform for crypto currencies traders/investors.",
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
                    name="Third-party services integration",
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
                    name="Django REST framework",
                ),
                ResumeProjectTechnology(
                    name="Python Code Analysis/Quality tools",
                ),
                ResumeProjectTechnology(
                    name="PostgreSQL",
                ),
                ResumeProjectTechnology(
                    name="Celery",
                ),
                ResumeProjectTechnology(
                    name="SQS",
                ),
                ResumeProjectTechnology(
                    name="Docker",
                ),
                ResumeProjectTechnology(
                    name="docker-compose",
                ),
                ResumeProjectTechnology(
                    name="Bitbucket Pipelines",
                ),
                ResumeProjectTechnology(
                    name="Amazon Web Services (AWS)",
                ),
                ResumeProjectTechnology(
                    name="Vimeo API",
                ),
            ],
        ),
        ResumeProject(
            name="Under NDA",
            start_date=date(year=2020, month=6, day=24),
            end_date=date(year=2020, month=8, day=19),
            summary="Crypto currencies trading/investments/exchange platform.",
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
                    name="Back-office and business logic code enhancements",
                ),
                ResumeProjectResponsibility(
                    name="Internal ETL services architecture development and implementation",
                ),
                ResumeProjectResponsibility(
                    name="Internal ETL services main modules development and implementation",
                ),
                ResumeProjectResponsibility(
                    name="Internal ETL services integration",
                ),
                ResumeProjectResponsibility(
                    name="Third-party services integration",
                ),
                ResumeProjectResponsibility(
                    name="Refactoring of the existing codebase to clean and split to reusable components",
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
                    name="Django REST framework",
                ),
                ResumeProjectTechnology(
                    name="Python Code Analysis/Quality tools",
                ),
                ResumeProjectTechnology(
                    name="PostgreSQL",
                ),
                ResumeProjectTechnology(
                    name="Celery",
                ),
                ResumeProjectTechnology(
                    name="SQS",
                ),
                ResumeProjectTechnology(
                    name="Docker",
                ),
                ResumeProjectTechnology(
                    name="docker-compose",
                ),
                ResumeProjectTechnology(
                    name="Bitbucket Pipelines",
                ),
                ResumeProjectTechnology(
                    name="Amazon Web Services (AWS)",
                ),
                ResumeProjectTechnology(
                    name="Web3",
                ),
                ResumeProjectTechnology(
                    name="aiohttp",
                ),
                ResumeProjectTechnology(
                    name="peewee",
                ),
                ResumeProjectTechnology(
                    name="Various blockchains",
                ),
            ],
        ),
        ResumeProject(
            name="dart-daap-client",
            start_date=date(year=2020, month=8, day=19),
            summary="A DAAP (Digital Audio Access Protocol) client library.",
            url="https://github.com/vint21h/dart-daap-client/",
            company=[
                ResumeProjectCompany(
                    name="Open Source",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__OPENSOURCE,
                    ),
                ),
            ],
        ),
        ResumeProject(
            name="anadea-ai-api",
            start_date=date(year=2021, month=1, day=4),
            end_date=date(year=2023, month=1, day=10),
            summary="Internal project that provides an easy possibility to create REST API for pretrained ML models.",
            company=[
                ResumeProjectCompany(
                    name="Anadea",
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
                    name="Django REST framework",
                ),
                ResumeProjectTechnology(
                    name="Python Code Analysis/Quality tools",
                ),
                ResumeProjectTechnology(
                    name="JavaScript Code Analysis/Quality tools",
                ),
                ResumeProjectTechnology(
                    name="SASS Code Analysis/Quality tools",
                ),
                ResumeProjectTechnology(
                    name="Docker Code Analysis/Quality tools",
                ),
                ResumeProjectTechnology(
                    name="PostgreSQL",
                ),
                ResumeProjectTechnology(
                    name="Redis",
                ),
                ResumeProjectTechnology(
                    name="Ansible",
                ),
                ResumeProjectTechnology(
                    name="Nginx",
                ),
                ResumeProjectTechnology(
                    name="HTML",
                ),
                ResumeProjectTechnology(
                    name="CSS",
                ),
                ResumeProjectTechnology(
                    name="JavaScript",
                ),
                ResumeProjectTechnology(
                    name="SASS",
                ),
                ResumeProjectTechnology(
                    name="gulp.js",
                ),
                ResumeProjectTechnology(
                    name="Webpack",
                ),
                ResumeProjectTechnology(
                    name="Celery",
                ),
                ResumeProjectTechnology(
                    name="RabbitMQ",
                ),
                ResumeProjectTechnology(
                    name="gRPC",
                ),
                ResumeProjectTechnology(
                    name="Dokku",
                ),
                ResumeProjectTechnology(
                    name="Docker",
                ),
                ResumeProjectTechnology(
                    name="docker-compose",
                ),
                ResumeProjectTechnology(
                    name="GitLab CI/CD"
                ),
            ],
        ),
        ResumeProject(
            name="django-security-txt",
            start_date=date(year=2021, month=3, day=20),
            summary="Handle security.txt",
            url="https://github.com/vint21h/django-security-txt/",
            company=[
                ResumeProjectCompany(
                    name="Open Source",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__OPENSOURCE,
                    ),
                ),
            ],
        ),
        ResumeProject(
            name="fedora-intel-remapped-nvme-device-support",
            start_date=date(year=2021, month=4, day=15),
            summary="Instruction and tools to build fedora custom kernel and live/installation media with kernel supporting Intel remapped NVME device.",
            url="https://github.com/vint21h/fedora-intel-remapped-nvme-device-support/",
            company=[
                ResumeProjectCompany(
                    name="Open Source",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__OPENSOURCE,
                    ),
                ),
            ],
        ),
        ResumeProject(
            name="GeoKinesia",
            start_date=date(year=2021, month=7, day=8),
            end_date=date(year=2021, month=10, day=6),
            summary="GeoKinesia interface for purchasing InSAR analysis for a selected area anywhere in the world.",
            url="https://interfacegeokinesia.com/",
            company=[
                ResumeProjectCompany(
                    name="Anadea",
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
                    name="Third-party services integration",
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
                    name="Django REST framework",
                ),
                ResumeProjectTechnology(
                    name="Python Code Analysis/Quality tools",
                ),
                ResumeProjectTechnology(
                    name="JavaScript Code Analysis/Quality tools",
                ),
                ResumeProjectTechnology(
                    name="PostgreSQL",
                ),
                ResumeProjectTechnology(
                    name="Redis",
                ),
                ResumeProjectTechnology(
                    name="Nginx",
                ),
                ResumeProjectTechnology(
                    name="HTML",
                ),
                ResumeProjectTechnology(
                    name="CSS",
                ),
                ResumeProjectTechnology(
                    name="JavaScript",
                ),
                ResumeProjectTechnology(
                    name="Webpack",
                ),
                ResumeProjectTechnology(
                    name="Celery",
                ),
                ResumeProjectTechnology(
                    name="RabbitMQ",
                ),
                ResumeProjectTechnology(
                    name="Docker",
                ),
                ResumeProjectTechnology(
                    name="docker-compose",
                ),
                ResumeProjectTechnology(
                    name="Google Maps API",
                ),
                ResumeProjectTechnology(
                    name="React",
                ),
                ResumeProjectTechnology(
                    name="PostGIS",
                ),
                ResumeProjectTechnology(
                    name="Amazon Web Services (AWS)",
                ),
            ],
        ),
        ResumeProject(
            name="gnome-shell-extension-tuned-profile-switcher",
            start_date=date(year=2021, month=6, day=7),
            summary="Displays a list of the TuneD profiles and allows to switch between them.",
            url="https://github.com/vint21h/gnome-shell-extension-tuned-profile-switcher/",
            company=[
                ResumeProjectCompany(
                    name="Open Source",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__OPENSOURCE,
                    ),
                ),
            ],
        ),
        ResumeProject(
            name="EncircleLabs",
            start_date=date(year=2021, month=7, day=20),
            end_date=date(year=2022, month=6, day=23),
            summary="Powering the Future of Construction Finance.",
            company=[
                ResumeProjectCompany(
                    name="Anadea",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__REGULAR,
                    ),
                )
            ],
            role="Python/Django developer",
            responsibilities=[
                ResumeProjectResponsibility(
                    name="Internal ETL service architecture development and implementation",
                ),
                ResumeProjectResponsibility(
                    name="Internal ETL service modules development and implementation",
                ),
                ResumeProjectResponsibility(
                    name="Integration with internal ETL service",
                ),
                ResumeProjectResponsibility(
                    name="Improvements of third-party services integrations",
                ),
                ResumeProjectResponsibility(
                    name="Refactoring of the existing codebase to clean and split to reusable components"
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
                    name="Django REST framework",
                ),
                ResumeProjectTechnology(
                    name="Python Code Analysis/Quality tools",
                ),
                ResumeProjectTechnology(
                    name="JavaScript Code Analysis/Quality tools",
                ),
                ResumeProjectTechnology(
                    name="PostgreSQL",
                ),
                ResumeProjectTechnology(
                    name="Celery",
                ),
                ResumeProjectTechnology(
                    name="RabbitMQ",
                ),
                ResumeProjectTechnology(
                    name="Docker",
                ),
                ResumeProjectTechnology(
                    name="docker-compose",
                ),
                ResumeProjectTechnology(
                    name="Amazon Web Services (AWS)",
                ),
            ],
        ),
        ResumeProject(
            name="pre-commit-config-shellcheck",
            start_date=date(year=2022, month=8, day=1),
            end_date=date(year=2023, month=1, day=10),
            summary="Tool for checking entry points in the pre-commit config with ShellCheck.",
            url="https://github.com/Anadea/pre-commit-config-shellcheck/",
            company=[
                ResumeProjectCompany(
                    name="Anadea",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__REGULAR,
                    ),
                ),
                ResumeProjectCompany(
                    name="Open Source",
                    metadata=ResumeProjectCompanyMetadata(
                        css_class=RESUME_PROJECT_COMPANY_METADATA_CSS_CLASS__OPENSOURCE,
                    ),
                ),
            ],
        ),
        ResumeProject(
            name="Swim Genius",
            start_date=date(year=2022, month=8, day=18),
            end_date=date(year=2023, month=1, day=10),
            summary="Platform for swimming teams/competitions management.",
            url="https://www.myswimgenius.com/",
            company=[
                ResumeProjectCompany(
                    name="Anadea",
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
                    name="Third-party services integration",
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
                    name="Django REST framework",
                ),
                ResumeProjectTechnology(
                    name="Python Code Analysis/Quality tools",
                ),
                ResumeProjectTechnology(
                    name="Docker Code Analysis/Quality tools",
                ),
                ResumeProjectTechnology(
                    name="PostgreSQL",
                ),
                ResumeProjectTechnology(
                    name="Redis",
                ),
                ResumeProjectTechnology(
                    name="Nginx",
                ),
                ResumeProjectTechnology(
                    name="HTML",
                ),
                ResumeProjectTechnology(
                    name="CSS",
                ),
                ResumeProjectTechnology(
                    name="JavaScript",
                ),
                ResumeProjectTechnology(
                    name="Celery",
                ),
                ResumeProjectTechnology(
                    name="RabbitMQ",
                ),
                ResumeProjectTechnology(
                    name="Docker",
                ),
                ResumeProjectTechnology(
                    name="docker-compose",
                ),
                ResumeProjectTechnology(
                    name="Google Maps API",
                ),
                ResumeProjectTechnology(
                    name="React",
                ),
                ResumeProjectTechnology(
                    name="Ansible",
                ),
                ResumeProjectTechnology(
                    name="Amazon Web Services (AWS)",
                ),
            ],
        ),
    ],
)
