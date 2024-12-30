from setuptools import setup, find_packages

setup(
    name="bible-app",
    version="0.1.0",
    packages=find_packages(),
    package_data={
        'bible_app': ['data/*.json'],
    },
    install_requires=[
        'taipy-gui==2.0.0',
    ],
)