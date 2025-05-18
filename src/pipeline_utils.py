import subprocess
import logging


def run_step(cmd):
    logging.info(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)
