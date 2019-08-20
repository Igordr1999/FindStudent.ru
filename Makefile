.PHONY: docs clean

COMMAND = docker-compose run --rm djangoapp /bin/bash -c

all: build test

restart: stop runfull

production: stop makemigrations migrate collectstatic runprod

build:
	docker-compose build

stop:
	docker-compose stop

run:
	docker-compose up

runprod:
	docker-compose up -d

makemigrations:
	docker-compose run --rm djangoapp findstudent/manage.py makemigrations

migrate:
	$(COMMAND) 'cd findstudent; for db in default database2; do ./manage.py migrate --database=$${db}; done'

collectstatic:
	docker-compose run --rm djangoapp findstudent/manage.py collectstatic --no-input

makemessages:
	docker-compose run --rm djangoapp findstudent/manage.py makemessages -a

compilemessages:
	docker-compose run --rm djangoapp findstudent/manage.py compilemessages

check: checksafety checkstyle

test:
	$(COMMAND) "pip install tox && tox -e test"

checksafety:
	$(COMMAND) "pip install tox && tox -e checksafety"

checkstyle:
	$(COMMAND) "pip install tox && tox -e checkstyle"

coverage:
	$(COMMAND) "pip install tox && tox -e coverage"

clean:
	rm -rf build
	rm -rf findstudent.egg-info
	rm -rf dist
	rm -rf htmlcov
	rm -rf .tox
	rm -rf .cache
	rm -rf .pytest_cache
	find . -type f -name "*.pyc" -delete
	rm -rf $(find . -type d -name __pycache__)
	rm .coverage
	rm .coverage.*

dockerclean:
	docker system prune -f
	docker system prune -f --volumes
