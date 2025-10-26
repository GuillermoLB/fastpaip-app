# fastpaip-app

[![CI](https://github.com/GuillermoLB/fastpaip-app/actions/workflows/ci.yml/badge.svg)](https://github.com/GuillermoLB/fastpaip-app/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/GuillermoLB/fastpaip-app/branch/main/graph/badge.svg)](https://codecov.io/gh/GuillermoLB/fastpaip-app)

`fastpaip-app` is a modern Python application designed to process events using a modular pipeline architecture, powered by AI.

## Project Structure

This project is structured as a monorepo using a `uv` workspace. The core logic and framework components are separated into distinct packages for better organization and reusability.

-   `src/fastpaip_app/`: The main application-specific code.
-   `packages/core/`: A reusable package containing the core domain logic, services, and infrastructure for text classification.
-   `packages/plummy/`: A lightweight, reusable pipeline framework for building event-driven handlers and processors.
-   `tests/`: Contains integration and end-to-end tests for the main application.

## Getting Started

Follow these instructions to set up the development environment.

### Prerequisites

-   Python 3.12+
-   [uv](https://github.com/astral-sh/uv) (Python package installer and resolver)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd fastpaip-app
    ```

2.  **Create a virtual environment:**
    `uv` can create and manage the virtual environment for you.
    ```bash
    uv venv
    ```

3.  **Activate the virtual environment:**
    ```bash
    source .venv/bin/activate
    ```

4.  **Install dependencies:**
    Install the project in editable mode along with all development dependencies (like `pytest` and `uvicorn`).
    ```bash
    uv pip install -e ".[dev]"
    ```

## Configuration

The application requires API keys and other settings to be configured via environment variables.

1.  Create a `.env` file in the project root by copying the example file:
    ```bash
    cp .env.example .env
    ```

2.  Edit the `.env` file and add your credentials, such as the `OPENAI_API_KEY`.

## Usage

You can run the application using the scripts defined in `pyproject.toml`.

### Run the Local Processing Script

To run the local entry point that processes a sample event (defined in `packages/core/src/core/application/entrypoints/local.py`):

```bash
uv run core
```

### Run the Web Server (Development)

To run the application as a web service with `uvicorn`:

```bash
uv run uvicorn fastpaip_app.main:app --reload
```
*(Note: You may need to create `src/fastpaip_app/main.py` and define a FastAPI `app` instance for this to work.)*

## Running Tests

To run the entire test suite for all packages, execute the following command from the project root:

```bash
uv run pytest
```
// filepath: README.md
# fastpaip-app

`fastpaip-app` is a modern Python application designed to process and classify text-based events using a modular pipeline architecture, powered by AI.

## Project Structure

This project is structured as a monorepo using a `uv` workspace. The core logic and framework components are separated into distinct packages for better organization and reusability.

-   `src/fastpaip_app/`: The main application-specific code.
-   `packages/core/`: A reusable package containing the core domain logic, services, and infrastructure for text classification.
-   `packages/plummy/`: A lightweight, reusable pipeline framework for building event-driven handlers and processors.
-   `tests/`: Contains integration and end-to-end tests for the main application.

## Getting Started

Follow these instructions to set up the development environment.

### Prerequisites

-   Python 3.12+
-   [uv](https://github.com/astral-sh/uv) (Python package installer and resolver)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd fastpaip-app
    ```

2.  **Create a virtual environment:**
    `uv` can create and manage the virtual environment for you.
    ```bash
    uv venv
    ```

3.  **Activate the virtual environment:**
    ```bash
    source .venv/bin/activate
    ```

4.  **Install dependencies:**
    Install the project in editable mode along with all development dependencies (like `pytest` and `uvicorn`).
    ```bash
    uv pip install -e ".[dev]"
    ```

## Configuration

The application requires API keys and other settings to be configured via environment variables.

1.  Create a `.env` file in the project root by copying the example file:
    ```bash
    cp .env.example .env
    ```

2.  Edit the `.env` file and add your credentials, such as the `OPENAI_API_KEY`.

## Usage

You can run the application using the scripts defined in `pyproject.toml`.

### Run the Local Processing Script

To run the local entry point that processes a sample event (defined in `packages/core/src/core/application/entrypoints/local.py`):

```bash
uv run core
```

### Run the Web Server (Development)

To run the application as a web service with `uvicorn`:

```bash
uv run uvicorn fastpaip_app.main:app --reload
```
*(Note: You may need to create `src/fastpaip_app/main.py` and define a FastAPI `app` instance for this to work.)*

## Running Tests

To run the entire test suite for all packages, execute the following command from the project root:

```bash
uv run