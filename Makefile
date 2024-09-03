DC = docker compose
SERVICE_NAME = currency_exchange
APP_FILE = docker_compose/app.yaml
STORAGE_FILE = docker_compose/storage.yaml

.PHONY: app
app-start:
	${DC} -f ${APP_FILE} up -d

.PHONY: drop-app
drop-app:
	${DC} -f ${APP_FILE} down

.PHONY: rebuild-app
rebuild-app:
	${DC} -f ${APP_FILE} build --no-cache


.PHONY: remove-app
remove-app:
	${DC} -f ${APP_FILE} down
	${DC} -f ${APP_FILE} rm -f ${SERVICE_NAME}

.PHONY: all
all:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} up --build -d

.PHONY: drop-all
drop-all:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} down

.PHONY: remove-all
remove-all:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} rm -f

.PHONY: storage
storage:
	${DC} -f ${STORAGE_FILE} up --build -d

.PHONY: drop-storage
drop-storage:
	${DC} -f ${STORAGE_FILE} down

.PHONY: remove-storage
remove-storage:
	${DC} -f ${STORAGE_FILE} rm -f

.PHONY: logs
logs:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} logs -f

.PHONY: shell
shell:
	${DC} -f ${APP_FILE} exec ${SERVICE_NAME} /bin/sh
