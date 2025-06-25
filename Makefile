install:
	poetry install --no-root

run:
	poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000

test-unit:
	poetry run pytest tests/unit

test-integration:
	poetry run pytest tests/integration

test-e2e:
	poetry run pytest tests/e2e

test-all: test-unit test-integration test-e2e

generate-requirements:
	poetry export --without-hashes --with-credentials -f requirements.txt > requirements.txt

docker-down:
	docker compose down

docker-build: generate-requirements
	docker compose --build

docker-up: docker-down
	docker compose up -d

docker-build-up: generate-requirements docker-down docker-build docker-up

