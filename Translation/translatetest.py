import codecs
import os
from transliterate import translit, get_available_language_codes

def test():
    for name in os.listdir('./files'):
        f = open('./files/' + name, 'r')
        cy_name = translit(name,'ru')

        with codecs.open('./cy_files/' + cy_name, "w", "utf-16") as cy_file:
            for line in f:
                cy_line = translit(line,'ru')
                cy_file.write(cy_line)

        cy_file.close()
        f.close()

if __name__ == "__main__":
    test()