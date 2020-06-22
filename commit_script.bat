set /A n=%RANDOM% %% 15 + 5

py commit_script.py %n%
