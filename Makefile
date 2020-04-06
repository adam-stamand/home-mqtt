root := $(dir $(abspath $(lastword $(MAKEFILE_LIST))/../..))

repository := us.gcr.io/loft-orbital-picu
image := picu-build
container := ${image}-$(shell whoami)
version := 0.5.5


.PHONY: help build start stop push

help:
	@echo "targets"
	@echo "... help"
	@echo "... build"
	@echo "... start"
	@echo "... stop"
	@echo "... push"

build-client:
	@echo building ${CLIENT}
	@docker build                               \
		--tag=${CLIENT} 						\
		--build-arg client=${CLIENT}      		\
		--file=docker/${CLIENT}.Dockerfile  \
		.

start-client:
	@echo starting ${CLIENT}
	@docker run                             \
		-i -t --rm                          \
		--name=${CLIENT}                 	\
		--network mqtt						\
		${CLIENT}

start-broker:
	@echo starting mosquitto
	@docker run                             \
		-i -t --rm                          \
		--name=mosquitto                 	\
		--network mqtt						\
		-p 1883:1883						\
		eclipse-mosquitto

stop:
	@echo stopping ${container}
	@docker container stop ${container}

push:
	@echo pushing ${repository}/${image}:${version}
	@docker push "${repository}/${image}:${version}"
