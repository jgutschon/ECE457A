VENV_NAME = virtual-env

createEnv:
	python -m venv $(VENV_NAME)

env:
	source $(VENV_NAME)/bin/activate

install:
	pip install -r requirements.txt

run:
	python q4.py