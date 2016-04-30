try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
    'description': 'Project creation utility script',
    'author': 'Spence',
    'url': 'URL',
    'download_url': 'DOWNLOAD_URL',
    'author_email': 'EMAIL',
    'version': '0.1.0',
    'install_requires': ['nose', 'gitpython',],
    'packages': ['fig'],
    'scripts': [],
    'name': 'fig'
}

setup(**config)
