clean-build:
	@echo "Cleaning build directories..."
	rm -rf build main.spec dist

build: clean-build 
	./venv/bin/python -m PyInstaller --onefile --windowed main.py 
