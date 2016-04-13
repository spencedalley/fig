try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
    'description': 'DESCRIPTION',
    'author': 'NAME',
    'url': 'URL',
    'download_url': 'DOWNLOAD_URL',
    'author_email': 'EMAIL',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'NAME'
}

setup(**config)
