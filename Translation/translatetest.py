import sys
from transliterate import translit, get_available_language_codes

def test():
    text = "Artificial Intelligence Innitiative"
    
    cy = translit(text,'ru')
    print(cy.encode('utf8'))


if __name__ == "__main__":
    test()