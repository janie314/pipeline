fmt:
    uv run ruff format
    bun run biome format

lint:
    uv run ruff check
    uv run ruff lint

fix:
    uv run ruff check --fix
    bun run biome lint --write --unsafe

run:
    uv run main.py
