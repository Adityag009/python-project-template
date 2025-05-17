.PHONY: install test lint format clean api

install:
	pip install -e ".[dev]"

test:
	pytest tests/

lint:
	flake8 src tests
	mypy src tests
	black --check src tests
	isort --check-only src tests

format:
	black src tests
	isort src tests

api:
	python -m src.api.server --reload

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete 