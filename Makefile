check-venv:
	which python3

run-app:
	uvicorn examples.io_bound.app:app --reload --port 5002