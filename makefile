VIRTUALENV = $(shell which virtualenv)

clean: shutdown
	rm -fr microservices.egg-info
	rm -fr venv

venv:
	$(VIRTUALENV) venv

install: clean venv
	. venv/bin/activate; python setup.py install
	. venv/bin/activate; python setup.py develop

launch: venv shutdown
	. venv/bin/activate; python -m services.warehouse.warehouse &
	. venv/bin/activate; python -m services.sales.sales &
	. venv/bin/activate; python -m services.accounting.accounting &

shutdown:
	ps -ef | grep "services.warehouse.warehouse" | grep -v grep | awk '{print $$2}' | xargs kill  
	ps -ef | grep "services.sales.sales" | grep -v grep | awk '{print $$2}' | xargs kill  
	ps -ef | grep "services.accounting.accounting" | grep -v grep | awk '{print $$2}' | xargs kill  