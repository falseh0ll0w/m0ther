import subprocess
import pkg_resources

def install_missing_libraries():
    required_libraries = ["library1", "library2", "library3"]  # Replace with the names of the required libraries
    
    missing_libraries = []
    for library in required_libraries:
        try:
            pkg_resources.require(library)
        except pkg_resources.DistributionNotFound:
            missing_libraries.append(library)
    
    if missing_libraries:
        for library in missing_libraries:
            try:
                subprocess.check_call(["pip", "install", library])
                print(f"Successfully installed {library}")
            except subprocess.CalledProcessError:
                print(f"Error installing {library}")
    else:
        print("All required libraries are already installed.")

if __name__ == "__main__":
    install_missing_libraries()