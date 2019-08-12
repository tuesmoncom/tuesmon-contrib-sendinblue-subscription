#!/usr/bin/env python
# -*- coding: utf-8 -*-

import versiontools_support
from setuptools import setup, find_packages

setup(
    name = 'tuesmon-contrib-sendinblue-subscription',
    version = ':versiontools:tuesmon_contrib_sendinblue_subscription:',
    description = 'Plugin to subscribe and unsubscribe users to the newsletter in Sendinblue.',
    long_description = 'Plugin to subscribe and unsubscribe users to the newsletter in Sendinblue.',
    keywords = 'tuesmon, sendinblue, integration',
    author = 'Tuesmon Agile LLC',
    author_email = 'tuesmon@tuesmon.com',
    url = 'https://github.com/tuesmoncom/tuesmon-contrib-sendinblue-subscription',
    license = 'AGPL',
    include_package_data = True,
    packages = find_packages(),
    install_requires=[
        "sendinblue == 2.0.4"
    ],
    setup_requires = [
        'versiontools >= 1.9',
    ],
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
