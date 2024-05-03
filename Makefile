lint:
	pip install ruff
	pip install pre-commit
	pre-commit install
	pre-commit run --all-files

doc:
	pip install -U pdoc3
	rm -rf docs
	pdoc --html ./src/genai_apis/ --output-dir docs
	mv docs/genai_apis/* docs/
	rm -rf docs/genai_apis

test:
	pytest

publish:
	python setup.py bdist_wheel
	twine upload dist/*
	rm -rf dist
	rm -rf src/genai_apis.egg-info
	rm -rf build
	
clean:
	rm -rf dist
	rm -rf src/genai_apis.egg-info
	rm -rf build