@echo off

REM
REM :: Check the health of all downloaded files in MD5.txt
REM

setlocal ENABLEDELAYEDEXPANSION ENABLEEXTENSIONS
set exitCode=0

if exist MD5.txt (
    for /F "tokens=1,2 delims==" %%I in (MD5.txt) do (
        if NOT "%%I" == ".\MD5.txt" (
            if NOT "%%I" == ".\FullSystemInstaller\DONTINDX.MSA" (
                call :GetValue %%I
                set /P value=<hash.txt          
                if NOT "!value!" == "%%J" (
                    echo The following file is corrupt: %%I
                    set exitCode=1
                )
            )
        )
    )   
    del hash.txt
) else (
    echo "The file containing the MD5s of the packages is not present: MD5.txt"
    pause
    exit 1
)
if %exitCode%==1 echo The installer is not healthy. Please see above errors.
if not %exitCode%==1 echo The installer is healthy.
pause
exit %exitCode%
goto :EOF
:GetValue
@echo off
call certutil -hashfile %1 MD5>hash.txt
for /f "delims=: skip=1" %%G in (hash.txt) do if not defined line set "line=%%G"
echo %line%>hash.txt
set line=