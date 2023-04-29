import os
import shutil
def clean():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    try:
        shutil.rmtree(r"binary")
        shutil.rmtree(r"bin")
        shutil.rmtree(r"obj")
        os.remove("test.cs")
        os.remove("minicallib.csproj")
    except:
        print("")
def Grab():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    clean()
    os.chdir("../../../")
    os.system(r"Xcopy src\languages\cs\binary\ test\tests\cs\binary /e /h /c /i")
    os.system(r"copy src\languages\cs\test.cs test\tests\cs\test.cs")
    os.system(r"copy src\languages\cs\minicallib.csproj test\tests\cs\minicallib.csproj")
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.system("dotnet build")
    os.system("clear")
    os.system("cls")
    os.system(r".\bin\Debug\net6.0\minicallib.exe")
# Grab()
# clean()