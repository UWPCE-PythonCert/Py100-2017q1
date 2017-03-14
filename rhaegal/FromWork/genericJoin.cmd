@echo off
if %1.==. (
    set /p joinPath="Path to Join: "
    set /p outputName="Name of Zip: "
) else (
    if "%1"=="-h" (
        echo "Usage: join.cmd <Path of split files> <output name>
        pause
        exit
    )
    if "%1"=="-help" (
        echo "Usage: join.cmd <Path of split files> <output name>
        pause
        exit
    )
    set joinPath=%1
    set outputName=%2
)

copy /B %joinPath%\part0??? %outputName%.zip
