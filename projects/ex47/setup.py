try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': '�� ������Ʈ',
    'author': '�� �̸�',
    'url': '������Ʈ URL',
    'download_url': '�������� �� �ִ� ��',
    'author_email': '�� �̸���',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': '������Ʈ �̸�'
}

setup(**config)