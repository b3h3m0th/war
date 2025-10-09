.PHONY: install format lint test run clean uml docs

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

uml:
	mkdir -p docs/uml/png
	mkdir -p docs/uml/plantuml
	pyreverse --output plantuml --output-directory docs/uml/plantuml --project war src/models src/enums src/utils 
	python src/scripts/generate_uml_pngs.py

docs:
	make uml

run:
	python src/main.py

clean:
	rm -rf __pycache__ .pytest_cache
	rm -rf src/enums/__pycache__ 
	rm -rf src/models/__pycache__ 
	rm -rf src/utils/__pycache__ 
	rm -rf src/scripts/__pycache__ 
	rm -rf tests/__pycache__ 
