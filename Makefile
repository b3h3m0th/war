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
	python src/your_project/main.py

clean:
	rm -rf __pycache__ .pytest_cache
