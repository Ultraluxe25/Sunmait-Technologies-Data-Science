# Home work `week-2` Overview

This project aims to use machine learning model for sentiment analysis by Hugging Face. The project utilizes a FastAPI backend for serving predictions via a RESTful API.  Comprehensive unit tests ensure the reliability and accuracy of the prediction model.

## Project Structure

The project is organized as follows:

**`.devcontainer/`:**  This directory contains the configuration for a reproducible development container using Docker and VS Code's Remote - Containers extension. This ensures a consistent development environment across different machines.  See the "Development Environment Setup" section below for details.

**`devcontainer.json`:**  Specifies the Docker image (`mcr.microsoft.com/devcontainers/python:1-3.12-bookworm`) and features for the development container, including Uvicorn, pytest, and Ruff for streamlined development and testing.

**`pyproject.toml`:** The project configuration file, defining the project's metadata and dependencies using the PEP 621 standard.  It lists the libraries required by the project.

**`requirements.txt`:**  A file listing the project's Python dependencies in a format compatible with `pip`.  It's generally recommended to generate this file from `pyproject.toml` for consistency.  (Note: the provided `requirements.txt` shows many dependencies; if possible, streamline them to only those absolutely necessary).

**`predict.py`:** This file contains the FastAPI application for making predictions. It loads a pre-trained machine learning model, handles incoming requests, makes predictions, returns results, and gracefully manages errors.

**`tests.py`:** This file contains unit tests for the prediction logic in `predict.py`. These tests verify the correctness and robustness of the prediction functions, covering input validation, prediction accuracy, error handling, and model loading.


## Development Environment Setup

The `.devcontainer` directory facilitates a consistent development environment using Docker. To set up:

1. **Install Docker:** Install and start Docker Desktop.
2. **Install VS Code Remote - Containers extension:** Install this extension to work with dev containers.
3. **Open the project in VS Code:** Open the project's root directory in VS Code.
4. **Rebuild the container (if necessary):** VS Code will detect `.devcontainer` and prompt to rebuild.  You may need to manually rebuild or recreate the container if prompted.

This sets up a container with Python 3.12 and all project dependencies.


## Project Dependencies

The `pyproject.toml` file lists the project's dependencies.  The `requirements.txt` file should ideally be generated from `pyproject.toml` for better maintainability.  Key dependencies include:

* **FastAPI:**  For building the web API.
* **Uvicorn:**  An ASGI server for running the FastAPI application.
* **Pydantic:** For data validation and parsing.
* **Scikit-learn (or TensorFlow/PyTorch):** The machine learning library used for the prediction model.
* **Transformers:** For loading pre-trained transformer models (if applicable).
* **Pytest:** For running unit tests.


## Running the Project

1. **Install Dependencies:** (Adjust based on your actual dependencies)
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the application:**
   ```bash
   uvicorn predict:app --reload
   ```
   This will start the FastAPI server.  `--reload` enables automatic restarts upon code changes.

3. **Run tests:** (Assuming you are using pytest)
   ```bash
   pytest tests.py
   ```


## Further Development

* Add more comprehensive tests to cover edge cases.
* Explore using a more robust model for better accuracy.
* Implement more detailed logging for improved monitoring and debugging.
* Add API documentation using tools like Swagger/OpenAPI.