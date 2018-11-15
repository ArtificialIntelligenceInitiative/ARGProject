import codecs
import os
#from transliterate import translit, get_available_language_codes

def encryptTo( lang ):

    if lang == "cy":
        from_folder = "./o_files/"
        to_folder = "./cy_files/"
        encoding = "utf-8"
    elif lang == "la":
        from_folder = "./cy_files/"
        to_folder = "./la_files/"
        encoding = "utf-16"
    else:
        print( "ERROR: Language '" + lang + "' is not supported")
        exit()

    for o_name in os.listdir( from_folder ):
        t_name = translateTo( lang, o_name )
        
        with codecs.open( to_folder + t_name, "w", "utf-16") as t_file:
            o_file = codecs.open( from_folder + o_name, "r", encoding )
            t_code = ""

            for line in o_file:
                t_code += translateTo( lang, line )

            t_file.write( t_code )

        t_file.close()
        o_file.close()

def translateTo( lang, string ):

    key =  {"a":"а","b":"б","c":"ц","d":"д","e":"е","f":"ф","g":"г","h":"х","i":"и","j":"й","k":"к","l":"л","m":"м",
            "n":"н","o":"о","p":"п","q":"я","r":"р","s":"с","t":"т","u":"м","v":"ж","w":"в","x":"ь","y":"ы","z":"з",
            "A":"А","B":"Б","C":"Ц","D":"Д","E":"Е","F":"Ф","G":"Г","H":"Х","I":"И","J":"Й","K":"К","L":"Л","M":"М",
            "N":"Н","O":"О","P":"П","Q":"Я","R":"Р","S":"Ц","T":"Т","U":"У","V":"Ж","W":"В","X":"Ь","Y":"Ы","Z":"З"}

    if lang == "la":
        key = { v:k for k,v in key.items() }

    t_string = ""
    i = 0
    while i < len(string):
        if string[i] in key:
            t_string += key[string[i]]
        else:
            t_string += string[i]
        i+=1

    return t_string


if __name__ == "__main__":
    encryptTo('la')
