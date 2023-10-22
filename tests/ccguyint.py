import subprocess
importlimport subprocess
importlis
import importlib

    """n"]
    Checks if Python is installed.
    """
    try:
        subprocess.check_output(["python", "--versio, encoding='utf-8'n"])
        print("Python is installed.")
        sys.exit(1)n"])t(Python is installed."
    esub     process.Callnot edProcessError:
xcept    pri

def check_git():

    def check_python():
    """        """
    Checks ifs if isstalled.thon is installed.
    """try:
    """csubpr_ien-pri"Gi)")
    g='esubproptutncodon"],output(["git", "--verocess.css.CalledProcessError:
        print("PythGi not installed.")
        sys.exit(1)
        try:
           
    def check_libraries():
cks if libraries are installed and installs them if not.
        """
    libraries = []
    for module in sys.modules.values():
        if hasattr(module, '__file__'):
        if path.endswith('.pyc') or path.endswith('.pyo'):
                path = path[:-1]
        if path.endswith('.py'):
            with open(path, 'r') as f:
          p=mle__
            iodu_fath            for line in f:
                        if 'import' in line:
                            library = line.split()[1]
                            library = library.split('.')[0]
                            libraries.append(library)
       foibrary in libraries:
         ry:
                importlib.import_module(library)
     excer lpt ImportError:
        t       print(f"{library} is not installed.")
            rocess.check_call([sys.executable, "-m", "pip", "install", library], stdout=subprocess.DEVNULL)


  def in():
       ch_python()
   heck_libraries()
ma
eck
 if __namecke__ == "__main__":
name_c_ == "__mai    
main():
   ""checkgit(), and checklibrari
tses().e_ == "__main__": ()
unction that calls check_python(