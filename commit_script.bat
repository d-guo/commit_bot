set /A n=%RANDOM% %% 15 + 10

py commit_script.py %n%
