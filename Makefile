clean-build:
	@echo "Cleaning build directories..."
	rm -rf build task-management.spec dist

build: clean-build 
	./venv/bin/python -m PyInstaller --onefile --windowed --name=task-management main.py
	chmod +x ./dist
	cp ./images/task.png ./dist
