import os
import pathlib
import sys
from transliterate import translit, get_available_language_codes

flist = []
for p in pathlib.Path('.').iterdir():
    if p.is_file():
        new_file_name = os.path.splitext(p)[0]
        new_file_name = translit(new_file_name,'ru')
        new_file_name += ".пы"
        print(p)
        print(new_file_name)
        flist.append(p)
        
    

#print(os.path.splitext("test_project.py")[0])

print('Hello, World!')
s = "hello "
 
s += "you"

print(s)
