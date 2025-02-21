check-venv:
	which python3

run-server:
	uvicorn examples.io_bound.app:app --reload --port 5002