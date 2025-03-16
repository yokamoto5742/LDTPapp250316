import subprocess
import os
from version_manager import update_version, update_version_py


def build_executable():
    new_version = update_version()
    update_version_py(new_version)

    subprocess.run([
        "pyinstaller",
        "--name=LDTPapp",
        "--windowed",
        "--icon=assets/LDPTapp_icon.ico",
        "--hidden-import=numpy",
        "--hidden-import=numpy.core._dtype_ctypes",
        "--hidden-import=numpy.random.common",
        "--hidden-import=numpy.random.bounded_integers",
        "--hidden-import=numpy.random.entropy",
        "--add-data", "config.ini;.",
        "main.py"
    ])

    print(f"Executable built successfully. Version: {new_version}")


if __name__ == "__main__":
    build_executable()