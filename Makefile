.PHONY: install format lint test run clean

install:
	pip install -r requirements.txt

format:
	black src tests

lint:
	flake8 src tests

test:
	pytest

run:
	python src/main.py

clean:
	rm -rf __pycache__ .pytest_cache
	rm -rf src/enums/__pycache__ 
	rm -rf src/models/__pycache__ 
	rm -rf src/utils/__pycache__ 
	rm -rf tests/__pycache__ 
