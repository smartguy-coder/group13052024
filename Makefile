LANG = uk

.PHONY: run-trans
run-trans:
	python3 translate_app.py ${LANG}
	@echo 'some info'

.PHONY: run-all
run-all: run-trans
	@echo 'run all data !!!!!!!!!'

.PHONY: run-def
run-def:
	echo  'make run-def name=Vasyl'
	@echo 'Greeting ${name}'
