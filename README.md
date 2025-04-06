### Instruction 

Create a virtual environment and install project dependencies:

```bash
python3 -m pip install uv
uv venv
source .venv/bin/activate 
uv pip sync uv.lock
```

Instal poetry, project dependencies and playwright:

```bash
pip install poetry
poetry install --no-root
playwright install
```
Run tests:
```bash
pytest
```
