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


#docs-init:
#	pip install -r docs/requirements.txt
#
#docs:
#	cd docs && make html
#	@echo "\033[95m\n\nBuild successful! View the docs homepage at docs/_build/html/index.html.\n\033[0m"
