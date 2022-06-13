from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in dlad_shopify_connector/__init__.py
from dlad_shopify_connector import __version__ as version

setup(
	name="dlad_shopify_connector",
	version=version,
	description="DLAD Shopify Connector",
	author="DLAD Software Solutions",
	author_email="dinesh@dlad.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
