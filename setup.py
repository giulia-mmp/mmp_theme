from setuptools import setup, find_packages

from mmp_theme import __version__

setup(
    name='mmp_theme',
    version=__version__,
    description='Custom theme and functions for MMP plots',

    url='https://github.com/giulia-mmp/mmp_theme',
    author='Giulia Bortolato',
    author_email='giulia.bortolato@milanomultiphysics.com',

    packages=find_packages()
)
