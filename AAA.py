import os
import sys

here = os.path.split(__file__)[0]

# Makes sublime_lib package available for all packages.
libpath = os.path.normpath(os.path.join(here, "Lib"))
if not libpath in sys.path:
    sys.path.append(libpath)
    print("[AAAPackageDev] Added %s to sys.path." % libpath)