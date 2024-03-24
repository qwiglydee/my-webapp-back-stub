#!/bin/bash
.venv/bin/uvicorn app:app --host ${HOST:-0.0.0.0} --port ${PORT:-8000}