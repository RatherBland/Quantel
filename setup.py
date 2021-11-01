from setuptools import setup, find_packages

INSTALL_REQUIRES = [
    "aiohttp==3.7.4.post0",
    "requests==2.26.0"
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="quantel",
    version="0.4",
    author="Guy M",
    author_email="guy@quantel.io",
    description="Interact with the Quantel Finance API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(),
    url="https://quantel.io",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Intended Audience :: Financial and Insurance Industry",
        "Operating System :: OS Independent",
    ],
    keywords="quantel, finance, stocks, mutual funds, etfs, insider transactions, financial data",
    project_urls={
        'Documentation': 'http://links.quantel.io/python-docs',
        'Source': 'https://github.com/ratherbland/quantel',
    },
)
