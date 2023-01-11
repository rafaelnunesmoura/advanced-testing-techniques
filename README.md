# advanced-testing-techniques
This repo is for doing advanced testing


## Setup Project

1. Create and source virtualenv

```bash
    python3.10 -m venv venv
    source venv/bin/activate
```

2. Create Scaffold

```bash
touch makefile && touch requirement.txt && touch hello.py && touch test_hello.py
```

3. Populate `makefile`

```bash
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=hello --cov=hellocli test_hello.py

lint:
	pylint --disable=R,C hello.py hellocli.py

all: install lint test
```
### How to Debug

* print
* pdb
* testing

