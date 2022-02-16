VIRTUALENV = $(shell which virtualenv)

clean: shutdown
	rm -fr microservices.egg-info
	rm -fr venv

venv:
	$(VIRTUALENV) venv

install: clean venv
	. venv/bin/activate; python setup.py install
	. venv/bin/activate; python setup.py develop

launch: shutdown
	docker-compose up --build -d

shutdown:
	docker-compose down

test: clean venv
	. venv/bin/activate; python test/accounting.test.py
	. venv/bin/activate; python test/sales.test.py
	. venv/bin/activate; python test/warehouse.test.py