- [Example Repository for Custom Python Component](#example-repository-for-custom-python-component)
  - [⚙️ Configuration](#️-configuration)
  - [📦 Managing dependencies](#-managing-dependencies)
  - [🚀 Running locally…](#-running-locally)
    - [🐋 …in Docker](#-in-docker)
    - [💜 …in virtual environment](#-in-virtual-environment)
    - [💔 …locally without uv](#-locally-without-uv)


# Example Repository for Custom Python Component

This is an example repository showing how you can use a custom Git repository for passing your own code into **Keboola's [Custom Python Component](https://github.com/keboola/component-custom-python/) (CPC)**.

As the main source file in this repo is located right in the root directory, importing other source files works as expected both when developing locally and when ran using CPC.


## ⚙️ Configuration

For your convenience, the [data/user_parameters.json](data/user_parameters.json) file can have exactly the same contents that you will later be able to place in the **User Parameters** field in CPC configuration, so you can just copy-paste it. Because of that, we prepared a super simple script, which will convert this file to the structure expected by Keboola's [base Python Component](https://github.com/keboola/python-component/) (which is used internally in CPC to handle [Keboola Common Interface](https://developers.keboola.com/extend/common-interface/)) for you.


## 📦 Managing dependencies

The `keboola.component` package is listed in the [pyproject.toml](pyproject.toml) file just as a dev dependency, because CPC already includes it. This example uses [Astral's](https://astral.sh/) brilliant [uv tool](https://docs.astral.sh/uv/#installation) for package management, so when adding more dependencies to your project:

- Use `uv add` for adding runtime dependencies (these will be installed when running the project via CPC).
- Use `uv add --dev` for adding development dependencies (these won't be installed in CPC).


## 🚀 Running locally…


### 🐋 …in Docker

When you have Docker installed, the easiest way to run this example is using `docker compose`:

```sh
docker compose build  # voluntary when running for the 1st time
docker compose up
```

This way, the configuration and source files are always updated during the build, which shall be done before you can say blueberry pie.


### 💜 …in virtual environment

For running this code locally without Docker, follow these steps:

```sh
# 🧑‍🔧 prepare the config.json file
data/_create_config_json.sh data/user_parameters.json data/config.json
# 💜 create virtual environment and install dependencies
uv sync
# 🚀 run
uv run main.py
```


### 💔 …locally without uv

*will be added later on*
