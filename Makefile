install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py
	# disables refactor and conection messages
	# --ignore-patterns - tells it to ignore these when completing linting 
	# analyze codes ending with .py

format:	
	black *.py 

test:
	python -m pytest -vv --cov=main test_*.py
	# --cov=main runs code coverage analysis on main 
	
		
all: install lint format test 