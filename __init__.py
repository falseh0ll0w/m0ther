import os
import subprocess
import sys
import pkg_resources


def check_python():
    """
    Check if Python is installed.
    """
    try:
        subprocess.check_output(["python", "--version"])
        print("Python is installed.")
    except subprocess.CalledProcessError:
        print("Python is not installed.")
        sys.exit(1)


def check_git():
    """
    Check if Git is installed.
    """
    try:
        subprocess.check_output(["git", "--version"])
        print("Git is installed.")
    except subprocess.CalledProcessError:
        print("Git is not installed.")
        sys.exit(1)


def check_libraries(directory):
    """
    Check the libraries used in the Python file.

    installed__ages = {pkg.key for pkg in pkg_resources.working_set}
    Args:
        directory (str): The directory to check for libraries.

    for root, dirs, files in os.walk(directory):
                file_path = os.path.join(root, file)
                installed_packages = {pkg.key for pkg in pkg_resources.working_set}
                with open(file_path, "r") as f:
                    code = f.read()
                    libraries = set()
                    for line in code.split("\n"):
                        if line.startswith("import") or line.startswith("from"):
                            words = line.split()
                            if len(words) >= 2:
                                library = words[1]
                                libraries.add(library)
                    for library in libraries:
                        if library in installed_packages:
                            print(f"{library} is installed in {file_path}.")
                        else:
                            print(f"{library} is not installed in {file_path}.")
                            install_library(library)
        for file in files:, encoding="utf-8"
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                installed_packages = {pkg.key for pkg in pkg_resources.working_set}
                with open(file_path, "r") as f:
                    code = f.read()
                    libraries = set()
                    for line in code.split("\n"):
                        if line.startswith("import") or line.startswith("from"):
                            words = line.split()
                            if len(words) >= 2:
                                library = words[1]
                                libraries.add(library)
                    for library in libraries:
                        if library in instalkages:
                            print(f"{library} is installed in {file_path}.")
                        else:
                     print(f"{library} is not installed in {file_path}.")
                            install_library(library)


    pass
def install_library(library):
    """
    Install a library using pip.
    """
