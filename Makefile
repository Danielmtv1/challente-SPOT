.PHONY: api test

api:
	docker-compose up -d

test:
	docker-compose up -d && python -m unittest discover
