@echo off
setlocal

for %%I in ("%~dp0..") do set "ROOT=%%~fI"
where py >nul 2>nul
if %ERRORLEVEL%==0 (
  set "PY=py -3"
) else (
  set "PY=python"
)

%PY% "%ROOT%\scripts\manage.py" install --claude %*
exit /b %ERRORLEVEL%
