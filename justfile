venv:
	[ -d ./venv ] || python3 -m venv ./venv

install: venv
	./venv/bin/pip install -r ./REQUIREMENTS.txt

run *ARGS:
	./venv/bin/python3 ./src/serial_debugger.py {{ARGS}}

clean:
	[ ! -d ./venv ] || rm -rf ./venv
	[ ! -d ./.mypy_cache ] || rm -r ./.mypy_cache
	[ ! -d ./src/__pycache__ ] || rm -r ./src/__pycache__
