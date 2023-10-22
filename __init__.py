import subprocess
import sys
import pkg_resources
import os

def check_python():
    try:
        subprocess.check_output(["python", "--version"])
        print("Python is installed.")
    except subprocess.CalledProcessError:
        print("Python is not installed.")
        sys.exit(1)

def check_git():
    try:
        subprocess.check_output(["git", "--version"])
        print("Git is installed.")
    except subprocess.CalledProcessError:
        print("Git is not installed.")
        sys.exit(1)

def check_libraries(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                installed_packages = [pkg.key for pkg in pkg_resources.working_set]
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

def install_library(library):
    try:
        subprocess.check_output(["pip", "install", library])
        print(f"Installed {library} successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to install {library}.")

def main():
    check_python()
    check_git()
    directory = input("Enter the directory path to check libraries: ")
    check_libraries(directory)

if __name__ == "__main__":
    main()