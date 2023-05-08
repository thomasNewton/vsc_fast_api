@echo off

set UVICORN_CMD=uvicorn htm:app --reload

if not defined UVICORN_WORKERS set UVICORN_WORKERS=1

if "%1" == "" (
  set HOST=127.0.0.1
) else (
  set HOST=%1
)

if "%2" == "" (
  set PORT=8000
) else (
  set PORT=%2
)

if "%3" == "" (
  set LOG_LEVEL=info
) else (
  set LOG_LEVEL=%3
)

 %UVICORN_CMD% --workers %UVICORN_WORKERS% --host %HOST% --port %PORT% --log-level %LOG_LEVEL%

