runserver:
	python manage.py runserver 0.0.0.0:3000

makemigrations:
	python manage.py makemigrations

migrate: makemigrations
	python manage.py migrate