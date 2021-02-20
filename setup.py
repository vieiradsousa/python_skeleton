try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python Project Template',
    'author': 'Herbert Vieirar',
    'url': 'URL to get it at',
    'download_url': 'Where to download it',
    'author_email': 'herbert.vieira.de.sousa@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'python_project_template'
}

setup(**config)