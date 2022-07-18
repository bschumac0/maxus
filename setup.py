from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in maxus/__init__.py
from maxus import __version__ as version

setup(
	name="maxus",
	version=version,
	description="maxus",
	author="John Rech G Cabatana",
	author_email="cabatana.johnrech.g@mail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
