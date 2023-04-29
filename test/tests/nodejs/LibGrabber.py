import os
import shutil
def clean():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    try:
        shutil.rmtree(r"binary")
        os.remove("test.js")
    except:
        print("")
def Grab():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    clean()
    os.chdir("../../../")
    os.system(r"Xcopy src\languages\nodejs\binary\ test\tests\nodejs\binary /e /h /c /i")
    os.system(r"copy src\languages\nodejs\test.js test\tests\nodejs\test.js")
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.system("clear")
    os.system("cls")