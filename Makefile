build:
	@docker-compose build

bash:
	@docker-compose run --rm excercise bash

run:
	@docker-compose up

test:
	@docker-compose run --rm excercise pytest

down:
	@docker-compose down -v

local-test:
	@poetry run pytest
