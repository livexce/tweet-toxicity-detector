#!/usr/bin/env bash
set -e
python scripts/scrape_web.py
python scripts/preprocess.py
python scripts/train_rf.py
python scripts/serve_model.py &
sleep 5
curl -X POST http://localhost:8000/predict -d '{"features":[...]}'
