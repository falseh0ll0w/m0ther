import os
import importlib

def check_python_installed():
    """
    Checks if Python is installed.
    """
    try:
        subprocess.check_output(["python", "--version"], encoding='utf-8')
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def check_module_installed(module_name):
    """
    Checks if a Python module is installed.
    """
    try:
        importlib.import_module(module_name)
        return True
    except ImportError:
        return False

def import_missing_modules():
    """
    Imports all missing modules in the current directory.
    """
    for file in os.listdir():
        if file.endswith(".py"):
            module_name = file[:-3]
            if not check_module_installed(module_name):
                print(f"Importing {module_name}...")
                importlib.import_module(module_name)

def main():
    if not check_python_installed():
        print("Python is not installed.")
        return

    import_missing_modules()

if __name__ == "__main__":
    main()