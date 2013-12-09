.PHONY: docs

init:
	pip install -r requirements.txt

test:
	py.test

coverage:
	py.test --verbose --cov-report term --cov=hubcrypt test_hubcrypt.py

publish:
	python setup.py sdist upload
	python setup.py bdist_wheel upload

