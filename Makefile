build:
	@docker-compose build

bash:
	@docker-compose run --rm exercise bash

run:
	@docker-compose up

test:
	@docker-compose run --rm exercise pytest

down:
	@docker-compose down -v

local-test:
	@poetry run pytest
