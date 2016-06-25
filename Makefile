
PYTHON=`which python`
PYTHON3=`which python3`


test:
	@echo "TODO: Hook up tests."

doc:
	cd docs; make html

source:
	$(PYTHON) setup.py sdist

upload:
	$(PYTHON) setup.py register sdist upload

pypi:
	pandoc --from=markdown --to=rst --output=README.rst README.md
	make source
	make upload

install:
	@echo "Installing for Python 2..."
	$(PYTHON) setup.py install
	@echo "Installing for Python 3..."
	$(PYTHON3) setup.py install

clean:
	$(PYTHON) setup.py clean
	rm -rf build/ MANIFEST
	make delpyc

delpyc:
	find . -name '*.pyc' -delete

install-libs:
	pip-2.7 install -U requirements.txt
	pip-3.2 install -U requirements.txt
