@echo off

set port=80

if exist "venv\" (
    echo "activating venv"
	venv\Scripts\activate
	echo installing requirements
	pip install -r requirements.txt
	echo requirements install success
	echo ---------------------------
	echo running migration
	flask db upgrade
	echo DB upgrade success
	echo ---------------------------
	echo running application at port 80
	echo ---------------------------
	waitress-serve --port=%port% --call "app:create_app"
) else (
    echo No Virtual environment found. Creating venv
	python -m venv venv
	echo Venv creation success
	echo ---------------------
	echo activating venv
	venv\Scripts\activate
	echo installing requirements
	pip install -r requirements.txt
	echo requirements install success
	echo ---------------------------
	echo running migration
	flask db upgrade
	echo DB upgrade success
	echo ---------------------------
	echo running application at port 80
	echo ---------------------------
	waitress-serve --port=%port% --call "app:create_app"
)

