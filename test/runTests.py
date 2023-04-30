import os
import shutil

from tests.python.LibGrabber import clean as PythonClean
from tests.python.LibGrabber import Grab as PythonGrab

from tests.js.LibGrabber import cleanES as EsClean
from tests.js.LibGrabber import GrabEs as EsGrab

from tests.js.LibGrabber import cleanNode as NodeClean
from tests.js.LibGrabber import GrabNode as NodeGrab

from tests.java.LibGrabber import clean as JavaClean
from tests.java.LibGrabber import Grab as JavaGrab

from tests.cs.LibGrabber import clean as CsClean
from tests.cs.LibGrabber import Grab as CsGrab

from tests.go.LibGrabber import clean as GoClean
from tests.go.LibGrabber import Grab as GoGrab


os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("""

[0] Python
[1] Nodejs : Es6_Modules
[2] Nodejs : Node_Modules
[3] Java
[4] Cs
[5] Go

""")

t=int(input("[?]: "))

if (t == 0):
    PythonGrab()
    from tests.python.test import test as PythonTest
    PythonTest()
    PythonClean()

if (t == 1):
    EsGrab()
    os.system("node test.mjs")
    EsClean()
    
if (t == 2):
    NodeGrab()
    os.system("node test.js")
    NodeClean()

if (t == 3):
    JavaGrab()
    os.system("java -jar test.jar")
    JavaClean()

if (t == 4):
    CsGrab()
    os.system("dotnet build")
    os.system(r".\bin\Debug\net6.0\minicallib.exe")
    CsClean()

if (t == 5):
    GoGrab()
    os.system("go run .")
    GoClean()