VENV = venv
IMAGE_NAME := lukin/fastlid
IMAGE_TAG := $(shell date +%Y%m%d)

.PHONY: run stop restart install

install:
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install wheel
	$(VENV)/bin/pip install -r requirements.txt

run:
	$(VENV)/bin/gunicorn -w 4 -b 0.0.0.0:5000 app:app

stop:
	@pkill -f "gunicorn"

restart: stop
	$(MAKE) run

docker-build:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .
	docker tag $(IMAGE_NAME):$(IMAGE_TAG) $(IMAGE_NAME):latest

docker-push: docker-build
	docker push $(IMAGE_NAME):$(IMAGE_TAG)
	docker push $(IMAGE_NAME):latest

docker-pull:
	docker pull $(IMAGE_NAME):latest

docker-run:
	docker run -d --name fastlid -p 5000:5000 $(IMAGE_NAME):latest

docker-stop:
	docker stop fastlid
	docker rm fastlid

docker-restart: docker-stop docker-run
