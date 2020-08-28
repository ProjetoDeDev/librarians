.PHONY: all help translate test clean update compass collect rebuild

# target: all - Default target. Does nothing.
all:
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

# target: help - Display callable targets.
help:
	@egrep "^# target:" [Mm]akefile

# target: collect - calls the "collectstatic" django command
collect:
	django-admin.py collectstatic  --noinput

migrate:
	python manage.py migrate

mk_migrations:
	python manage.py makemigrations

run:
	python manage.py runserver

clean:
	find . -name "*.pyc" -print0 | xargs -0 rm -rf
	-rm -rf htmlcov
	-rm -rf .coverage
	-rm -rf build
	-rm -rf dist
	-rm -rf src/*.egg-info


