# -----------------------------------------------------------------------------
#
# This file is the copyrighted property of Tableau Software and is protected
# by registered patents and other applicable U.S. and international laws and
# regulations.
#
# Unlicensed use of the contents of this file is prohibited. Please refer to
# the NOTICES.txt file for further details.
#
# -----------------------------------------------------------------------------
import setuptools


setuptools.setup(
    name='tableauhyperapi',
    version='0.0.11249',
    author='Tableau Software, LLC',
    author_email='tableauhyperapi@tableau.com',
    description='Hyper API for Python',
    long_description="""The Hyper API contains a set of functions you can use to automate your interactions with Tableau extract (.hyper) files. You can use the API to create new extract files, or to open existing files, and then insert, delete, update, or read data from those files.

Using the Hyper API developers and administrators can:
- Create extract files for data sources not currently supported by Tableau.
- Automate custom extract, transform and load (ETL) processes (for example, implement rolling window updates or custom incremental updates).
- Retrieve data from an extract file.

More information can be found here: https://help.tableau.com/current/api/hyper_api/en-us/.
""",
    long_description_content_type='text/markdown',
    url='https://help.tableau.com/current/api/hyper_api/en-us/',
    packages=['tableauhyperapi', 'tableauhyperapi/impl'],
    include_package_data=True,
    install_requires=['cffi>=1.12.2,<2'],
    python_requires='>=3.6',
)
