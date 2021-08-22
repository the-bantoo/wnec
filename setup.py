from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in wnec/__init__.py
from wnec import __version__ as version

setup(
	name='wnec',
	version=version,
	description='cd .',
	author='q',
	author_email='[A',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
