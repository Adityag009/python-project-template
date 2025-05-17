FROM python:3.8-slim

WORKDIR /app

COPY pyproject.toml .
COPY README.md .
COPY src/ src/

RUN pip install --no-cache-dir -e .

CMD ["python", "-m", "src.hello"] 