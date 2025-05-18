import subprocess


def check_and_retrain():
    res = subprocess.run(
        ["python", "scripts/detect_drift.py"], capture_output=True, text=True
    )
    if "Dérive détectée" in res.stdout:
        subprocess.run(["bash", "scripts/full_pipeline.sh"], check=True)
