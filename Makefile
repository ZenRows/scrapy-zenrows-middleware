.PHONY: build clean lint test

build:
	python setup.py sdist bdist_wheel

clean:
	python setup.py clean
	rm -rf dist build scrapy_zenrows.egg-info .pytest_cache
	find . -name '__pycache__' -delete -o -name '*.pyc' -delete

lint:
	flake8 --config flake8 setup.py scrapy_zenrows
