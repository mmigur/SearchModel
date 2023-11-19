DC = docker-compose
APP_FILE = docker_compose/app.yaml

.PYONV: app
app-start:
	${DC} -f ${APP_FILE} up -d

.PYONV: drop-app
app-down:
	${DC} -f ${APP_FILE} down

.PYONV: logs
logs:
	${DC} -f ${APP_FILE} logs
