SHELL := /bin/bash
clean:
	cd postgres_l30 && docker-compose down
	docker volume rm postgres_l30_postgres_data

up_database:
	cd postgres_l30 && docker-compose up -d
