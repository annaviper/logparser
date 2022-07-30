dist:
	python3 setup.py sdist bdist_wheel

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/

test:
	pytest