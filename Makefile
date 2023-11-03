install:
	pip install --upgrade pip && pip install -r requirements.txt

test:
	python -m pytest -vv test_llama.py

format:
	black *.py

lint:
	pylint --disable=R,C main.py llama.py

all: install lint format