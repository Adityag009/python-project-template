FROM python:3.8-slim

WORKDIR /app

COPY pyproject.toml .
COPY README.md .
COPY config/ config/
COPY src/ src/

RUN pip install --no-cache-dir -e .

# Expose the port the app runs on
EXPOSE 8000

# Run the FastAPI server
CMD ["python", "-m", "src.api.server", "--host", "0.0.0.0"] 