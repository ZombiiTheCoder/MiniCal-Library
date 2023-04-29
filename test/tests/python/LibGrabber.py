import os
import shutil
def clean():
    try:
        shutil.rmtree(r"binary")
        os.remove("test.py")
    except:
        print("")
def Grab():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    clean()
    os.chdir("../../../")
    os.system(r"Xcopy src\languages\python\binary\ test\tests\python\binary /e /h /c /i")
    os.system(r"copy src\languages\python\test.py test\tests\python\test.py")
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.system("clear")
    os.system("cls")
    os.system("")