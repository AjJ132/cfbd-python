# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.4.9
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "cfbd"
VERSION = "4.4.9"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="College Football Data API",
    author_email="admin@collegefootballdata.com",
    url="https://github.com/CFBD/cfbd-python",
    keywords=["Swagger", "College Football Data API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \&quot;Bearer \&quot; prepended (e.g. \&quot;Bearer your_key\&quot;). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501
    """
)
