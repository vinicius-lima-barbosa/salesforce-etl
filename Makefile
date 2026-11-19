# ===== Configurações =====
PYTHON       ?= python3
VENV         := .venv
VENV_PY      := $(VENV)/bin/python
VENV_PIP     := $(VENV)/bin/pip
PYTHONPATH   := src

.DEFAULT_GOAL := help

# ===== Help =====
.PHONY: help
help:
	@echo "Alvos disponíveis:"
	@echo "  make setup    - Cria o venv e instala as dependências"
	@echo "  make run      - Executa o pipeline (src/main.py)"
	@echo "  make test     - Roda os testes (pytest)"
	@echo "  make clean    - Remove o venv e caches"
	@echo "  make rebuild  - Reconstrói o ambiente do zero"

# ===== Ambiente =====
$(VENV)/bin/activate: requirements.txt
	$(PYTHON) -m venv $(VENV)
	$(VENV_PIP) install --upgrade pip
	$(VENV_PIP) install -r requirements.txt
	@touch $(VENV)/bin/activate

.PHONY: setup
setup: $(VENV)/bin/activate
	@echo "✔ Ambiente pronto em ./$(VENV)"
	@echo "  Ative manualmente com: source $(VENV)/bin/activate"

# ===== Execução =====
.PHONY: run
run: setup
	PYTHONPATH=$(PYTHONPATH) $(VENV_PY) src/main.py

# ===== Testes =====
.PHONY: test
test: setup
	PYTHONPATH=$(PYTHONPATH) $(VENV_PY) -m pytest -v

# ===== Limpeza =====
.PHONY: clean
clean:
	rm -rf $(VENV)
	find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete
	@echo "✔ Ambiente e caches removidos"

.PHONY: rebuild
rebuild: clean setup