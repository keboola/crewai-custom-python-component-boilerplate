- [Example Repository for Custom Python Component](#example-repository-for-custom-python-component)
  - [⚙️ Configuration](#️-configuration)
  - [📦 Managing dependencies](#-managing-dependencies)
  - [🚀 Running locally…](#-running-locally)
    - [🐋 …in Docker](#-in-docker)
    - [💜 …in virtual environment](#-in-virtual-environment)
    - [💔 …locally without uv](#-locally-without-uv)

# CrewAI Boilerplate for Keboola Custom Python Component

This repository provides a boilerplate for running [CrewAI](https://github.com/joaomdmoura/crewAI) flows inside [Keboola's Custom Python Component](https://github.com/keboola/component-custom-python/). Use this as a starting point for integrating CrewAI automations into your Keboola projects.

The structure and configuration are designed to make it easy to:
- Develop and test CrewAI flows locally
- Seamlessly deploy and run them in Keboola's custom python component environment

## ⚙️ Configuration

Before running the project, you must create a configuration file:

1. Copy the example config file:
   ```sh
   cp data/config.json.dist data/config.json
   ```
2. Edit `data/config.json` and provide your OpenAI API key in the parameters section (as `#OPENAI_API_KEY`).

## 📦 Managing dependencies

Dependencies are managed using [uv](https://docs.astral.sh/uv/#installation). The `keboola.component` package is listed as a dev dependency, as it is already included in the Keboola environment. To add dependencies:

- Use `uv add` for runtime dependencies (these will be installed when running the project in Keboola).
- Use `uv add --dev` for development dependencies (these won't be installed in Keboola).

## 🚀 Running locally…

### 🐋 …in Docker

When you have Docker installed, the easiest way to run this example is using `docker compose`:

```sh
docker compose build  # voluntary when running for the 1st time
docker compose run dev
```

This way, the configuration and source files are always updated during the build.
