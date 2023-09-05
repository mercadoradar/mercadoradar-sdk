from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='mercadoradar',
    version='1.0.4',
    description='Python client library for the Mercado Radar API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    project_urls={
        'Documentation': 'https://documenter.getpostman.com/view/7792424/2s9Xy6qVgY',
        'Source Code': 'https://github.com/mercadoradar/mercadoradar-sdk',
    },
    author='Mercado Radar',
    author_email='dev@mercadoradar.com.br',
    packages=find_packages(),
    install_requires=requirements,
)
