import os
import shutil
def cleanNode():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    try:
        shutil.rmtree(r"binary")
        os.remove("test.js")
    except:
        print("")
def cleanES():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    try:
        shutil.rmtree(r"binary")
        os.remove("test.mjs")
    except:
        print("")
def GrabEs():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    cleanES()
    os.chdir("../../../")
    os.system(r"Xcopy src\languages\js\es_module\binary\ test\tests\js\binary /e /h /c /i")
    os.system(r"copy src\languages\js\es_module\test.mjs test\tests\js\test.mjs")
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.system("clear")
    os.system("cls")
def GrabNode():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    cleanNode()
    os.chdir("../../../")
    os.system(r"Xcopy src\languages\js\node_module\binary\ test\tests\js\binary /e /h /c /i")
    os.system(r"copy src\languages\js\node_module\test.js test\tests\js\test.js")
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.system("clear")
    os.system("cls")