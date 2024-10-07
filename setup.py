from setuptools import setup, find_packages

setup(
    name="scrapy_zenrows",
    version="0.1",
    description="A Scrapy middleware for accessing ZenRows Scraper API with minimal setup.",
    long_description=open("README.md").read(),
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
