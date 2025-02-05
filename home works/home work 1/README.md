# Home Work 1 - Learn how to use devcontainers in VS Code. Work with uv tool and ruff as linter and formatter. How to launch Docker and basics of it.

## Project Structure:

### 📂 Directories
- **`.devcontainer/`** – Configuration files for a Dev Container in VS Code.
- **`.git/`** – Git repository metadata for version control.
- **`.ruff_cache/`** – Cache for the `ruff` linter to speed up checks.

### 📄 Files
- **`.gitignore`** – Specifies files and directories to be ignored by Git.
- **`.python-version`** – Defines the Python version for tools like `pyenv`.
- **`hello.py`** – A Python script.
- **`pyproject.toml`** – Project metadata, dependencies, and build configuration (used by tools like `uv`, `poetry`).
- **`README.md`** – Markdown documentation for the project (current file).
- **`test ruff.ipynb`** – Jupyter Notebook, likely used for testing `ruff` linter.
- **`uv.lock`** – Lockfile for `uv`, specifying exact dependency versions for reproducibility.