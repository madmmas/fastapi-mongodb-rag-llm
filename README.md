# FastAPI Skeleton Template

## Run in local
### Install Dependencies
```
poetry install --no-root
```
### Run Test

```
poetry run pytest tests/integration
```

### Code Quality Check
```
poetry run flake8 .
poetry run black . --check
poetry run isort . --check-only --profile black
poetry run bandit .
poetry run safety scan
```

## Run in docker

### Generate requirements.txt file
```
poetry export --without-hashes --with-credentials -f requirements.txt > requirements.txt
```
### Run Docker Compose
```
docker compose up -d
```
