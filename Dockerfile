FROM python:3.10-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /code/

COPY pyproject.toml .
COPY uv.lock .

ENV UV_PROJECT_ENVIRONMENT="/usr/local/"
RUN uv sync --all-groups --frozen

COPY src/ src
COPY main.py .

# prepare config.json based on user_parameters.json
WORKDIR /data/
COPY data/ .
RUN ./_create_config_json.sh user_parameters.json config.json

# run
WORKDIR /code/
CMD ["uv", "run", "main.py"]
