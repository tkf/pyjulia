import os
import subprocess
import sys
from textwrap import dedent

from .test_compatible_exe import run


def test_runtests_failure(tmp_path):
    testfile = tmp_path / "test.py"
    testcode = u"""
    def test_THIS_TEST_MUST_FAIL():
        assert False
    """
    testfile.write_text(dedent(testcode))

    env = os.environ.copy()
    env.pop("PYJULIA_TEST_REBUILD", None)
    proc = run(
        [
            sys.executable,
            "-m",
            "julia.runtests",
            "--",
            str(testfile),
            "--no-julia",
            "-k",
            "test_THIS_TEST_MUST_FAIL",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        env=env,
    )
    assert proc.returncode == 1
    assert "1 failed" in proc.stdout
