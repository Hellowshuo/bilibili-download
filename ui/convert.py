#!/usr/bin/python3
import os
file_list = os.listdir(".")
for file in file_list:
    if file[-2:] == 'ui':
        convert_str = "pyuic5 %s.ui -o ../Qwidget/%s_ui.py" % (file[0:-3],file[0:-3])
        print(convert_str)
        os.system(convert_str)
