from setuptools import setup, find_packages
from scrapy_zenrows.__version__ import __version__


setup(
    name="scrapy-zenrows",
    version=__version__,
    description="A Scrapy middleware for accessing ZenRows Scraper API with minimal setup.",
    long_description=open("scrapy_zenrows/README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Idowu Omisola and Yuvraj Chandra",
    author_email="support@zenrows.com",
    url="https://github.com/ZenRows/scrapy-zenrows-middleware",
    packages=find_packages(),
    install_requires=[
        "scrapy",
    ],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
