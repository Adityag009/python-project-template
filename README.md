# Python Project Template

A production-ready Python project template with a modern project structure and best practices. This template follows the `src` layout pattern and is designed to serve as a foundation for data science, machine learning, and general Python applications.

## Why Project Structure Matters

A well-structured Python repository is like a neat kitchen:

- Anyone can walk in and start cooking (coding)
- It's easy to find ingredients (code, data, configs)
- New chefs (team members) can contribute smoothly
- It helps with debugging, testing, scaling, and deploying

Modern AI and data science projects can become complex quickly, so a standardized structure prevents chaos as the codebase grows.

## Modern Python Project Structures: The src Layout vs. Flat Layout

### The src Layout (Used in This Template)

The src layout places your actual package code in a `src` directory separate from the project root.

**Benefits of the src Layout:**

- **Prevents import confusion**: Python's interpreter includes the current working directory in the import path. The src layout ensures you're always using the installed version of your package, not the development files.
- **Cleaner installation**: Only files meant to be importable are available after installation.
- **Forces proper packaging**: You must install your package to use it, ensuring your package configuration works correctly.
- **Ideal for medium to large projects**: Provides better separation and organization for growing codebases.

### The Flat Layout

The flat layout places package code directly at the project root level, without a src directory.

**Benefits of the Flat Layout:**

- **Simplicity**: Easier to understand for beginners
- **Less nesting**: Fewer directory levels to navigate
- **Direct imports**: Can import modules without installation during development
- **Best for small projects**: Quick setup for simpler applications

### Comparison Summary

| Layout | Best for | Pros | Cons |
|--------|----------|------|------|
| src layout | Medium to large projects, AI/ML | Safe imports, scalable, avoids bugs | Slightly more setup |
| flat layout | Small/simple scripts & packages | Simple, fast setup | Can become messy as project grows |

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
│   ├── unit/              # Unit tests
│   └── integration/       # Integration tests
├── data/                  # Data files (often gitignored)
│   ├── raw/
│   └── processed/
├── notebooks/             # Jupyter notebooks for exploration
├── config/                # Configuration files
├── scripts/               # Utility scripts
├── Dockerfile             # Containerization instructions
├── Makefile               # Common automation commands
├── .gitignore             # Specifies intentionally untracked files
├── pyproject.toml         # Modern Python packaging config
└── README.md              # Project overview and instructions
```

## Benefits of This Structure

1. **Separation of Concerns**: Code, tests, data, and configuration are clearly separated
2. **Modular Design**: Each directory has a specific purpose, making navigation intuitive
3. **Scalability**: The structure can grow with your project without becoming unwieldy
4. **Standardization**: Follows modern Python best practices, making it familiar to other developers
5. **Ease of Testing**: Dedicated test directories for different testing levels
6. **Configuration Management**: Separates code from configuration

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

## Best Practices Implemented

This template implements several Python best practices:

1. **Proper Packaging**: Uses pyproject.toml for modern Python packaging
2. **Type Hints**: Encourages the use of Python type annotations
3. **Automated Testing**: Setup for pytest and test organization
4. **Code Quality Tools**: Black, isort, flake8, and mypy for code quality
5. **Dependency Management**: Clear specification of dependencies
6. **Environment Isolation**: Docker support for consistent environments
7. **Documentation**: Comprehensive README and docstrings

## Extending the Template

This template is designed to be adaptable. Here are some ways you might extend it:

1. **Add CI/CD**: Integration with GitHub Actions, GitLab CI, or other CI/CD systems
2. **API Layer**: Add FastAPI or Flask for RESTful APIs
3. **Database Integration**: Add SQLAlchemy or ORM of choice
4. **Logging**: Implement structured logging
5. **Monitoring**: Add instrumentation for performance monitoring
6. **Documentation**: Extend with Sphinx for auto-generated documentation

## License

This project is licensed under the MIT License - see the LICENSE file for details.