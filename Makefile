# Caminho do venv
VENV_DIR := .venv
PYTHON   := python3
PIP      := $(VENV_DIR)/bin/pip
PYTHON_VENV := $(VENV_DIR)/bin/python

.PHONY: help venv install run clean

help:
	@echo "Comandos disponíveis:"
	@echo "  make venv     - cria o ambiente virtual (.venv)"
	@echo "  make install  - instala dependências no venv (pygame)"
	@echo "  make run      - roda o jogo usando o venv"
	@echo "  make clean    - remove o venv"

venv:
	@echo "==> Criando venv em $(VENV_DIR)"
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "==> Venv criado. Para ativar manualmente: source $(VENV_DIR)/bin/activate"

install: venv
	@echo "==> Atualizando pip no venv"
	$(PIP) install --upgrade pip
	@echo "==> Instalando dependências (pygame)"
	$(PIP) install pygame

run: install
	@echo "==> Rodando jogo com $(PYTHON_VENV)"
	$(PYTHON_VENV) app.py

clean:
	@echo "==> Removendo venv"
	rm -rf $(VENV_DIR)
