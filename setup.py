
from setuptools import setup, find_packages
from osdelnetsdk.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='osdelnetsdk',
    version=VERSION,
    description='SDK for OSDELNET Rest API',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Sotirios Oikonomou',
    author_email='sotoik@gmail.com',
    url='https://github.com/sotiris-oikonomou/osdelnetsdk',
    license='GNU General Public License v3.0',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    include_package_data=True,
)
