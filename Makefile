test:
	python -m barecli.core
	nosetests

install:
	pip install --editable .

uninstall:
	pip uninstall barecli
