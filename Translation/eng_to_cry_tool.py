import codecs
import os
#from transliterate import translit, get_available_language_codes

def test():
    for name in os.listdir('./files'):
        f = open('./files/' + name, 'r')
        #cy_name = translit(name,'ru')
        en_name = os.path.splitext(name)[0]
        cy_name = ""
        i = 0
        while i < len(en_name):
            if(en_name[i] == "a"):
                cy_name  += "а"
            elif(en_name[i] == "b"):
                cy_name  += "б"
            elif(en_name[i] == "c"):
                cy_name  += "ц"    
            elif(en_name[i] == "d"):
                cy_name  += "д"
            elif(en_name[i] == "e"):
                cy_name  += "е"  
            elif(en_name[i] == "f"):
                cy_name  += "ф"
            elif(en_name[i] == "g"):
                cy_name  += "г"    
            elif(en_name[i] == "h"):
                cy_name  += "х"
            elif(en_name[i] == "i"):
                cy_name  += "и"
            elif(en_name[i] == "j"):
                cy_name  += "й"
            elif(en_name[i] == "k"):
                cy_name  += "к"    
            elif(en_name[i] == "l"):
                cy_name  += "л"
            elif(en_name[i] == "m"):
                cy_name  += "м"
            elif(en_name[i] == "n"):
                cy_name  += "н"
            elif(en_name[i] == "o"):
                cy_name  += "о"    
            elif(en_name[i] == "p"):
                cy_name  += "п"
            elif(en_name[i] == "q"):
                cy_name  += "я"
            elif(en_name[i] == "r"):
                cy_name  += "р"
            elif(en_name[i] == "s"):
                cy_name  += "с"    
            elif(en_name[i] == "t"):
                cy_name  += "т"
            elif(en_name[i] == "u"):
                cy_name  += "м"
            elif(en_name[i] == "v"):
                cy_name  += "ж"
            elif(en_name[i] == "w"):
                cy_name  += "в"    
            elif(en_name[i] == "x"):
                cy_name  += "ь"
            elif(en_name[i] == "y"):
                cy_name  += "ы"
            elif(en_name[i] == "z"):
                cy_name  += "з"    
            elif(en_name[i] == "A"):
                cy_name  += "А"
            elif(en_name[i] == "B"):
                cy_name  += "Б"
            elif(en_name[i] == "C"):
                cy_name  += "Ц"
            elif(en_name[i] == "D"):
                cy_name  += "Д"
            elif(en_name[i] == "E"):
                cy_name  += "Е"  
            elif(en_name[i] == "F"):
                cy_name  += "Ф"
            elif(en_name[i] == "G"):
                cy_name  += "Г"    
            elif(en_name[i] == "H"):
                cy_name  += "Х"
            elif(en_name[i] == "I"):
                cy_name  += "И"
            elif(en_name[i] == "J"):
                cy_name  += "Й"
            elif(en_name[i] == "K"):
                cy_name  += "К"    
            elif(en_name[i] == "L"):
                cy_name  += "Л"
            elif(en_name[i] == "M"):
                cy_name  += "М"
            elif(en_name[i] == "N"):
                cy_name  += "Н"
            elif(en_name[i] == "O"):
                cy_name  += "О"    
            elif(en_name[i] == "P"):
                cy_name  += "П"
            elif(en_name[i] == "Q"):
                cy_name  += "Я"
            elif(en_name[i] == "R"):
                cy_name  += "Р"
            elif(en_name[i] == "S"):
                cy_name  += "Ц"    
            elif(en_name[i] == "T"):
                cy_name  += "Т"
            elif(en_name[i] == "U"):
                cy_name  += "У"
            elif(en_name[i] == "V"):
                cy_name  += "Ж"
            elif(en_name[i] == "W"):
                cy_name  += "В"    
            elif(en_name[i] == "X"):
                cy_name  += "Ь"
            elif(en_name[i] == "Y"):
                cy_name  += "Ы"
            elif(en_name[i] == "Z"):
                cy_name  += "З"
            else:
                cy_name  += en_name[i]
            i += 1
        
        cy_name += ".пы"
        
        with codecs.open('./cy_files/' + cy_name, "w", "utf-16") as cy_file:
            for line in f:
                i=0
                new_file_line = ""
                while i < len(line):
                    
                    if(line[i] == "a"):
                        new_file_line += "а"
                    elif(line[i] == "b"):
                        new_file_line += "б"
                    elif(line[i] == "c"):
                        new_file_line += "ц"    
                    elif(line[i] == "d"):
                        new_file_line += "д"
                    elif(line[i] == "e"):
                        new_file_line += "е"  
                    elif(line[i] == "f"):
                        new_file_line += "ф"
                    elif(line[i] == "g"):
                        new_file_line += "г"    
                    elif(line[i] == "h"):
                        new_file_line += "х"
                    elif(line[i] == "i"):
                        new_file_line += "и"
                    elif(line[i] == "j"):
                        new_file_line += "й"
                    elif(line[i] == "k"):
                        new_file_line += "к"    
                    elif(line[i] == "l"):
                        new_file_line += "л"
                    elif(line[i] == "m"):
                        new_file_line += "м"
                    elif(line[i] == "n"):
                        new_file_line += "н"
                    elif(line[i] == "o"):
                        new_file_line += "о"    
                    elif(line[i] == "p"):
                        new_file_line += "п"
                    elif(line[i] == "q"):
                        new_file_line += "я"
                    elif(line[i] == "r"):
                        new_file_line += "р"
                    elif(line[i] == "s"):
                        new_file_line += "с"    
                    elif(line[i] == "t"):
                        new_file_line += "т"
                    elif(line[i] == "u"):
                        new_file_line += "м"
                    elif(line[i] == "v"):
                        new_file_line += "ж"
                    elif(line[i] == "w"):
                        new_file_line += "в"    
                    elif(line[i] == "x"):
                        new_file_line += "ь"
                    elif(line[i] == "y"):
                        new_file_line += "ы"
                    elif(line[i] == "z"):
                        new_file_line += "з"

                    elif(line[i] == "A"):
                        new_file_line += "А"
                    elif(line[i] == "B"):
                        new_file_line += "Б"
                    elif(line[i] == "C"):
                        new_file_line += "Ц"    
                    elif(line[i] == "D"):
                        new_file_line += "Д"
                    elif(line[i] == "E"):
                        new_file_line += "Е"  
                    elif(line[i] == "F"):
                        new_file_line += "Ф"
                    elif(line[i] == "G"):
                        new_file_line += "Г"    
                    elif(line[i] == "H"):
                        new_file_line += "Х"
                    elif(line[i] == "I"):
                        new_file_line += "И"
                    elif(line[i] == "J"):
                        new_file_line += "Й"
                    elif(line[i] == "K"):
                        new_file_line += "К"    
                    elif(line[i] == "L"):
                        new_file_line += "Л"
                    elif(line[i] == "M"):
                        new_file_line += "М"
                    elif(line[i] == "N"):
                        new_file_line += "Н"
                    elif(line[i] == "O"):
                        new_file_line += "О"    
                    elif(line[i] == "P"):
                        new_file_line += "П"
                    elif(line[i] == "Q"):
                        new_file_line += "Я"
                    elif(line[i] == "R"):
                        new_file_line += "Р"
                    elif(line[i] == "S"):
                        new_file_line += "Ц"    
                    elif(line[i] == "T"):
                        new_file_line += "Т"
                    elif(line[i] == "U"):
                        new_file_line += "У"
                    elif(line[i] == "V"):
                        new_file_line += "Ж"
                    elif(line[i] == "W"):
                        new_file_line += "В"    
                    elif(line[i] == "X"):
                        new_file_line += "Ь"
                    elif(line[i] == "Y"):
                        new_file_line += "Ы"
                    elif(line[i] == "Z"):
                        new_file_line += "З"
                    else:
                        new_file_line += line[i]
                        
                    i += 1
                cy_file.write(new_file_line)

        cy_file.close()
        f.close()

if __name__ == "__main__":
    test()
