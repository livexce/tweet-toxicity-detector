from src.pipeline_utils import run_step


def test_run_step(tmp_path, caplog):
    caplog.set_level("INFO")
    run_step("echo hello")
    assert "Running: echo hello" in caplog.text
