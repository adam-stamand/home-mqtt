.PHONY: help build start stop push

help:
	@echo "targets"
	@echo "... help"
	@echo "... build"
	@echo "... start"

build-client:
	@echo building ${CLIENT}
	@docker build                               \
		--tag=${CLIENT} 						\
		--build-arg client=${CLIENT}      		\
		--file=docker/Dockerfile  \
		.

start-client:
	@echo starting ${CLIENT}
	@docker run                             \
		-i -t --rm                          \
		--name=${CLIENT}                 	\
		--network mqtt						\
		${CLIENT}

run-client:
	@echo running ${CLIENT}
	@python3 main.py


start-broker:
	@echo starting mosquitto
	@docker run                             \
		-i -t --rm                          \
		--name=mosquitto                 	\
		--network mqtt						\
		-p 1883:1883						\
		eclipse-mosquitto

