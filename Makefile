.PHONY: install format lint test run clean coverage uml-docs api-docs docs

activate:
	source .venv/bin/activate

install:
	pip install -r requirements.txt

format:
	black src tests

lint:
	flake8 src tests

test:
	pytest

uml-docs:
	mkdir -p docs/uml/png
	mkdir -p docs/uml/plantuml
	pyreverse --output plantuml --output-directory docs/uml/plantuml --project war src/models src/enums src/utils 
	python src/scripts/generate_uml_pngs.py

api-docs:
	pdoc src/models src/enums src/utils --output-dir docs/api

docs: uml-docs api-docs

coverage:
	coverage run -m pytest
	coverage report

run:
	python src/main.py

clean:
	rm -rf __pycache__ .pytest_cache
	rm -rf src/enums/__pycache__ 
	rm -rf src/models/__pycache__ 
	rm -rf src/utils/__pycache__ 
	rm -rf src/scripts/__pycache__ 
	rm -rf tests/__pycache__ 
