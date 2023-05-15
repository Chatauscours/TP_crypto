def convertit_texte_en_binaire(texte):
    for lettre in texte:
        assert ord(lettre) < 128, "Tous les caractères du textes doivent faire partie de la table Unicode C1 et latin 1 (ISO/CEI 8859-1)"
    code_binaire = ""
    for lettre in texte:
        position = bin(ord(lettre))
        position = position[2:] #On supprime lo 0b du binaire
        while len(position) < 9:
            position = "0" + position
        code_binaire += position
    return code_binaire

i = convertit_texte_en_binaire("NSI")

def convertit_binaire_vers_entier_base_10(chaine_binaire):
    print(chaine_binaire)
    position = int(chaine_binaire, 2)
    return position

def convertit_binaire_en_texte(chaine_binaire):
    message = ""
    while chaine_binaire != "":
        if len(chaine_binaire) < 9:
            position = convertit_binaire_vers_entier_base_10(chaine_binaire)
            chaine_binaire = ""
            message += chr(position)
        else:
            position = convertit_binaire_vers_entier_base_10(chaine_binaire[:9])
            chaine_binaire = chaine_binaire[9:]
            message += chr(position)
    return message
print(convertit_binaire_en_texte(i))