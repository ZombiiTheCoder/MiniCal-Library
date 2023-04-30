import os
import shutil

from tests.python.LibGrabber import clean as PythonClean
from tests.python.LibGrabber import Grab as PythonGrab

from tests.nodejs.LibGrabber import clean as NodeClean
from tests.nodejs.LibGrabber import Grab as NodeGrab

from tests.java.LibGrabber import clean as JavaClean
from tests.java.LibGrabber import Grab as JavaGrab

from tests.cs.LibGrabber import clean as CsClean
from tests.cs.LibGrabber import Grab as CsGrab

from tests.go.LibGrabber import clean as GoClean
from tests.go.LibGrabber import Grab as GoGrab


os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("""

[0] Python
[1] Nodejs
[2] Java
[3] Cs
[4] Go

""")

t=int(input("[?]: "))

if (t == 0):
    PythonGrab()
    from tests.python.test import test as PythonTest
    PythonTest()
    PythonClean()
    

if (t == 1):
    NodeGrab()
    # os.chdir("tests/nodejs")
    os.system("node test.js")
    NodeClean()

if (t == 2):
    JavaGrab()
    # os.chdir("tests/java")
    os.system("java -jar test.jar")
    JavaClean()

if (t == 3):
    CsGrab()
    os.system("dotnet build")
    os.system(r".\bin\Debug\net6.0\minicallib.exe")
    CsClean()

if (t == 4):
    GoGrab()
    os.system("go run .")
    GoClean()