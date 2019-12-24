set /A n=%RANDOM% %% 15 + 10

python3 commit_script.py %n%
