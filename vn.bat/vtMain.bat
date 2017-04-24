@echo off

set file[0]="_simnow.json"
set file[1]="_dh_he.json"
set file[2]="_dh_feng.json"

cd..
cd vn.trader
python vtMain.py %file[0]%
pause