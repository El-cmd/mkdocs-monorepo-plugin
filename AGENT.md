# AGENT.md

## Project Snapshot
- Repository: `El-cmd/mkdocs-monorepo-plugin`
- Default branch: `master`
- Detected stack: Python, static web, shell scripts
- Notable root entries: `.github/`, `__tests__/`, `docs/`, `mkdocs_monorepo_plugin/`, `sample-docs/`, `.gitignore`, `catalog-info.yaml`, `LICENSE`, `mkdocs.yml`, `README.md`, `requirements.txt`, `setup.py`
- Source mix: .md:105, .yml:76, .py:8, .sh:4, .yaml:3, .txt:1

## Working Guidelines
- Keep changes scoped to the requested behavior and follow the style already present in the touched files.
- Check `README.md`, `Makefile`, package scripts, and Docker files before introducing new commands or tooling.
- Pin or document Python dependency changes in requirements.txt.
- Do not commit local secrets, `.env` files, generated dependency folders, build artifacts, or editor metadata.

## Setup
- `python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt`

## Run
- `No canonical run command is defined; inspect README/Makefile/package scripts first.`

## Validate
- `python3 -m pytest (when tests are present)`
