# Stage 1: Build dependencies
FROM python:3.12-bookworm AS builder
WORKDIR /app
COPY pyproject.toml requirements.txt ./
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY main.py tests.py ./
RUN pip install pytest  # Install pytest in the builder stage

# Stage 2: Final image
FROM python:3.12-slim-bullseye
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.12/site-packages/ ./site-packages/
COPY --from=builder /app/main.py ./main.py
COPY --from=builder /app/tests.py ./tests.py
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "workers", "4"]