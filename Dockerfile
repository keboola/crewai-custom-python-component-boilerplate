FROM python:3.10-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN uv tool install crewai
RUN ln -s /root/.local/bin/crewai /usr/local/bin/crewai

WORKDIR /code/

COPY pyproject.toml .
COPY uv.lock .

ENV UV_PROJECT_ENVIRONMENT="/usr/local/"
RUN uv sync --all-groups --frozen

COPY src/ src

# prepare config.json based on user_parameters.json
WORKDIR /data/
COPY data/ .

# run
WORKDIR /code/
CMD ["uv", "run", "src/sample_flow/main.py"]
