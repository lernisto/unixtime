
install: dist
	pip install -U dist/*

clean:
	rm -rf build dist __pycache__ *.egg-info src/__pycache__ src/*.egg-info

black: src setup.py
	black setup.py src tests

dist: clean black
	python setup.py bdist_wheel

test: test install 
	pytest


.PHONY: clean dist install test black
