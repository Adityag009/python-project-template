# Python Project Template

A production-ready Python project template with a modern project structure and best practices.

## Features

- Modern Python packaging with `pyproject.toml`
- Testing setup with pytest
- Code formatting with Black and isort
- Type checking with mypy
- Linting with flake8
- Docker support
- Makefile for common commands
- Structured for data science/ML projects
- CI/CD ready

## Project Structure

```
project/
├── src/                    # Source code (main package)
│   ├── __init__.py
│   ├── data/              # Data processing modules
│   ├── models/            # ML/AI model implementations
│   └── utils/             # Helper functions
├── tests/                 # Unit and integration tests
├── data/                  # Data files (often gitignored)
│   ├── raw/
│   └── processed/
├── notebooks/             # Jupyter notebooks for exploration
├── config/               # Configuration files
├── scripts/              # Utility scripts
└── [Other configuration files]
```

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/python-project-template.git
   cd python-project-template
   ```

2. Install the package and development dependencies:
   ```bash
   make install
   ```

3. Run the tests:
   ```bash
   make test
   ```

4. Run the example:
   ```bash
   python -m src.hello
   ```

## Development

- Format code: `make format`
- Run linters: `make lint`
- Run tests: `make test`
- Clean build files: `make clean`

## Docker

Build and run the Docker container:

```bash
docker build -t python-project .
docker run python-project
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.