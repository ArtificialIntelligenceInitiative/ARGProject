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
        f = open(p)
        line = f.readline()
        with open(new_file_name, "a") as new_file:
            while line:
                line = f.readline()
                print(line)
                new_file_line = translit(line,'ru')
                new_file.write(new_file_line)

        f.close()
        new_file.close()    
        
    

print('Hello, World!')
s = "hello "
 
s += "you"

print(s)
