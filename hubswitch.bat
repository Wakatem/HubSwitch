@echo off
call conda activate cli
python "%~dp0main.py" %*
call conda deactivate