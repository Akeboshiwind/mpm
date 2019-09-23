EX='mpm'

build-deps:
	pip3 install PyInstaller

build: build-deps
	pyinstaller main.py --onefile -n ${EX}
	cp ./dist/${EX} ./

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +
	rm -rf build/ dist/ __pycache__/
	rm -f mpm mpm.spec

install: build
	cp ./${EX} ~/bin/

.PHONY: build-deps build clean install
