@REM Copyright (c) 2023 Geo-Studios - All Rights Reserved.

@echo off

set "JarName=MiniCalTest" 
set "MainClass=test"
set "KeepSrcOut=false"

set "javaDir="
set "experiments=true"

@REM Only works if experiments are enabled
set "javaBaseDir=E:\Program Files\Java"
set "javaJdkVer=jdk-13"



@Rem IMPORTANT DO NOT CHANGE
set "java=%javaBaseDir%\%javaJdkVer%\bin\"

CLS
MKDIR "bin"
DEL "bin\%JarName%.jar" /Q /S
RMDIR srcOut /Q /S
Xcopy src\languages\java srcOut /e/h/c/i
cd srcOut
CLS
if "%experiments%" == "false" "%javaDir%javac" *.java
if "%experiments%" == "false" "%javaDir%jar" cf "%JarName%.jar" *.class *
if "%experiments%" == "false" "%javaDir%jar" --update --verbose --file "%JarName%.jar" --main-class "%MainClass%"

if "%experiments%" == "true" "%java%javac" *.java
if "%experiments%" == "true" "%java%jar" cf "%JarName%.jar" *.class *
if "%experiments%" == "true" "%java%jar" --update --verbose --file "%JarName%.jar" --main-class "%MainClass%"
copy "%JarName%.jar" "../test/tests/java/test.jar"
DEL "%JarName%.jar"
cd ../
if "%KeepSrcOut%" == "false" RMDIR srcOut /Q /S
CLS
@REM echo Compilation is done and your "%JarName%.jar" is ready sir.
@REM copy "bin/%JarName%.jar" "test/tests/java/test.jar"
@REM if "%experiments%" == "false" "%java%java" -jar "bin/%JarName%.jar"

@REM if "%experiments%" == "true" "%java%java" -jar "bin/%JarName%.jar"