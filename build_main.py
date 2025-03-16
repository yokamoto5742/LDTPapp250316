import subprocess
import os
import glob

from version_manager import update_version, update_version_py


def find_package_dlls(base_path, package_name):
    """
    指定されたパッケージに関連するDLLファイルを再帰的に検索する
    """
    site_packages = os.path.join(base_path, "Lib", "site-packages")
    all_dlls = []

    # パッケージのルートディレクトリを検索
    package_paths = []
    for root, dirs, files in os.walk(site_packages):
        if os.path.basename(root).startswith(package_name):
            package_paths.append(root)

    # 各パスでDLLを検索
    for path in package_paths:
        for root, dirs, files in os.walk(path):
            dlls = [os.path.join(root, f) for f in files if f.endswith('.dll')]
            if dlls:
                print(f"Found DLLs in {root}:")
                for dll in dlls:
                    print(f"  - {dll}")
                all_dlls.extend(dlls)

    return all_dlls


def build_executable():
    new_version = update_version()
    update_version_py(new_version)

    # 環境変数のパスを設定
    venv_path = r"C:\Users\yokam\PycharmProjects\LDTPapp250316\.venv"

    # DLLファイルを検索
    print("Searching for DLLs...")
    pandas_dlls = find_package_dlls(venv_path, "pandas")
    numpy_dlls = find_package_dlls(venv_path, "numpy")

    if not pandas_dlls and not numpy_dlls:
        print("警告: DLLファイルが見つかりません。別の方法を試みます。")
        # 代替パスを試す
        alt_paths = [
            os.path.join(venv_path, "Lib", "site-packages"),
            os.path.join(venv_path, "libs"),
            os.path.join(venv_path, "DLLs"),
            os.path.join(os.path.dirname(os.__file__), "site-packages")
        ]

        for path in alt_paths:
            print(f"Checking alternative path: {path}")
            if os.path.exists(path):
                print(f"Directory contents of {path}:")
                for item in os.listdir(path):
                    print(f"  - {item}")

    # PyInstallerのオプションを設定
    pyinstaller_options = [
        "pyinstaller",
        "--name=LDTPapp",
        "--windowed",
        "--icon=assets/LDPTapp_icon.ico",
        "--add-data", "config.ini;.",
    ]

    pyinstaller_options.extend([
        "--hidden-import", "pandas._libs.aggregations",
        "--hidden-import", "pandas._libs.window.aggregations",
        "--hidden-import", "pandas._libs.window",
        "--hidden-import", "pandas._libs.groupby",
        "--hidden-import", "numpy",
        "--hidden-import", "scipy",
        "--clean",
        "--noconfirm",
        "main.py"
    ])

    try:
        # バッチファイルで実行
        batch_file = "build_app.bat"
        with open(batch_file, "w", encoding="utf-8") as f:
            f.write(" ".join(pyinstaller_options))

        print(f"バッチファイル {batch_file} を作成しました")
        print(f"コマンド: {' '.join(pyinstaller_options)}")

        # バッチファイルを実行
        print("バッチファイルを実行します...")
        os.system(batch_file)

        print(f"Executable build process completed. Version: {new_version}")

    except Exception as e:
        print(f"Error during build process: {e}")
        raise


if __name__ == "__main__":
    build_executable()
