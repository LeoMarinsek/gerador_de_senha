from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="gerador_senhas",
    version="0.0.1",
    author="Leonardo Thomaz Marinsek",
    author_email="leonardomarinsek@hotmail.com",
    description="Gerador automático de senhas seguras",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LeoMarinsek/gerador_de_senha.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
)