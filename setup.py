from setuptools import setup, find_packages

setup(
    name='graphutils',
    version='0.0.6',
    description='A library to help you use graphs',
    author='Gerti',
    packages=find_packages(),
    install_requires=["pydot"],
    readme = "README.md"
)