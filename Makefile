server:
	poetry run uvicorn main:app --reload

run-tests:
	poetry run pytest --cov -sx -v tests/
