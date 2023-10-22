import subprocess
import sys

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

def check_libraries():
    libraries = ["numpy", "pandas", "matplotlib", "scikit-learn"]
    for library in libraries:
        try:
            subprocess.check_output(["pip", "show", library])
            print(f"{library} is installed.")
        except subprocess.CalledProcessError:
            print(f"{library} is not installed.")
            sys.exit(1)

def main():
    check_python()
    check_git()
    check_libraries()

if __name__ == "__main__":
    main()