##Focntion non demandé

def inverser_chaine_carcatere(chaine_caractere:str)->str:
    """inverse une chaine de carcatère"""
    texte_inverse = ""
    i = len(chaine_caractere)
    while i > 0:
        texte_inverse += chaine_caractere[i-1]
        i = i - 1
    return texte_inverse

##Fonction demandé

def convertit_texte_en_binaire(texte:str)->str:
    """Convertit une chaine de caractère texte en base 2"""
    liste_texte_binaire = []
    texte_binaire = ""
    for caractere in texte:
        liste_texte_binaire.append(bin(ord(caractere)).replace('0b', ''))
    for element in liste_texte_binaire:
        while len(element) != 8:
            element = inverser_chaine_carcatere(inverser_chaine_carcatere(element)+"0")
        texte_binaire += element
    return texte_binaire

def convertit_binaire_vers_un_entier_en_base_10(chaine_binaire:str)->int:
    """Convertit base 2 en entier base 10"""
    entier = 0
    chaine_binaire = inverser_chaine_carcatere(chaine_binaire)
    for i in range(len(chaine_binaire)):
        if chaine_binaire[i] == '1':
            entier += 2**i
    return entier

def convertit_binaire_en_texte(binaire:str)->str:
    """Convertit base 2 en texte"""
    dico_lettre_texte = {}
    convertion_binaire = ""
    for i in range(0, len(binaire), 8):
        dico_lettre_texte[str(i//8)] = chr(convertit_binaire_vers_un_entier_en_base_10(binaire[i:i+8]))
    for lettre in dico_lettre_texte.values():
        convertion_binaire += lettre
    return convertion_binaire

def chiffre_xor(chaine_binaire:str, cle_binaire:str)->str:
    """Chiffre chaine_binaire avec un xor grâce à cle_binaire"""
    message_chiffre = ""
    for i in range(len(chaine_binaire)):
        a = int(chaine_binaire[i])
        b = int(cle_binaire[i%len(cle_binaire)])
        message_chiffre += str(a^b)
    return message_chiffre

def convertit_binaire_vers_decimal(octet:str)->float:
	"""Convertit base 2 en base 10 en octet"""
	return convertit_binaire_vers_un_entier_en_base_10(octet)

def genere_clefs_publique_et_privee(a1,b1,a2,b2):
    """ genere et renvoi la cle publique puis la clef privee"""
    M = a1*b1-1
    e = a2*M+a1
    d = b2*M+b1
    n = int((e*d-1)/M)
    return (e,n),(d,n)

def chiffre_message(m:str,clef:tuple)->list:
    """Fonction qui chiffre un message m qui est une chaîne de caractères avec la clé clef, en remplaçant chaque caractère par son code ASCII en décimal."""
    message_convertit = convertit_texte_en_binaire(m)
    liste_lettre_message_convertit = [convertit_binaire_vers_un_entier_en_base_10(message_convertit[i:i+8]) for i in range(0, len(message_convertit), 8)]
    liste_lettre_message_chiffre = list()
    for lettre in liste_lettre_message_convertit:
        liste_lettre_message_chiffre.append(clef[0]*lettre%clef[1])
    return liste_lettre_message_chiffre

def dechiffre_message(m:list[int],clef:tuple):
    """Fonction qui déchiffre un message m qui est une liste de nombres et renvoie le message déchiffré sous la forme d’une chaîne de caractères."""
    return chr(clef[0]*m%clef[1])

def bruteForceKIDRSA(e,n):
    """Fonction qui permet de calculer et de retourner le premier entier inférieur qui vérifie la relation 'e*d−1 est divisible par n'"""
    pass

def egcd(a,b):
    pass

def modinv(e,n):
    pass


##Vérifications des fopnctions (ne suffit pas pour vérifier entierement une fonction)

##Fonction non demandé
    
assert inverser_chaine_carcatere("NSI") == "ISN"

##Fonction demandé

assert convertit_texte_en_binaire("SPECIALITE NSI") =="0101001101010000010001010100001101001001010000010100110001001001010101000100010100100000010011100101001101001001"
assert convertit_texte_en_binaire("TERM") ==  "01010100010001010101001001001101"

assert convertit_binaire_vers_un_entier_en_base_10("01001110") == 78
assert convertit_binaire_vers_un_entier_en_base_10('0001001011111111') == 4863

assert convertit_binaire_en_texte("010011100101001101001001") == 'NSI'
assert convertit_binaire_en_texte('00110010001000000100010001101001011001010111010101111000') == '2 Dieux'

assert chiffre_xor("0101001101010000010001010100001101001001010000010100110001001001010101000100010100100000010011100101001101001001","01010100010001010101001001001101") == "0000011100010101000101110000111000011101000001000001111000000100000000000000000001110010000000110000011100001100" #Avec valeur = "SPECIALITE NSI", et clé = "TERM"
assert chiffre_xor('00110010001000000100010001101001011001010111010101111000', '0101101001100101011100100110111100100000010101000111011101101111') == '01101000010001010011011000000110010001010010000100001111' #Avec valeur = "2 Dieux", et clé = "Zero Two"

assert convertit_binaire_vers_decimal("01010101") == 85
assert convertit_binaire_vers_decimal("10101010") == 170

