.PHONY: all clean package test

all: clean test

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

package:
	python setup.py sdist

release:
	python setup.py sdist register upload
