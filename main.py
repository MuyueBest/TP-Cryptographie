# Montrer sur un exemple (message et clef de chiffrement de votre choix), que si on chiffre le message avec la clef et qu’on chiffre le message chiffré avec la même clef, on retrouve le message de départ en clair

def inverser_chaine_carcatere(chaine_caractere:str)->str:
    """inverse une chaine de carcatère"""
    texte_inverse = ""
    i = len(chaine_caractere)
    while i > 0:
        texte_inverse += chaine_caractere[i-1]
        i = i - 1
    return texte_inverse

def convertit_texte_en_binaire(texte:str)->str:
    """Convertit une chaine de caractère texte en binaire"""
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
    """Convertit un binaire en entier"""
    entier = 0
    chaine_binaire = inverser_chaine_carcatere(chaine_binaire)
    for i in range(len(chaine_binaire)):
        if chaine_binaire[i] == '1':
            entier += 2**i
    return entier

def convertit_binaire_en_texte(binaire:str)->str:
    """Convertit un binaire en texte"""
    dico_lettre_texte = {}
    convertion_binaire = str()
    for i in range(0, len(binaire), 8):
        dico_lettre_texte[str(i//8)] = chr(convertit_binaire_vers_un_entier_en_base_10(binaire[i:i+8]))
    for lettre in dico_lettre_texte.values():
        convertion_binaire += lettre
    return convertion_binaire

def chiffre_xor(chaine_binaire:str,cle_binaire:str):
    """ chiffre la chaine_binaire par un xor grace à la cle_binaire"""
    message_chiffre = ""
    for i in range(len(chaine_binaire)):
        a = int(chaine_binaire[i])
        b = int(cle_binaire[i%len(cle_binaire)])
        message_chiffre += str(a^b)
    return message_chiffre



def convertit_binaire_vers_decimal(octet):
    pass

def genere_clefs_publique_et_privee(a1,b1,a2,b2):
    """ genere et renvoi la cle publique puis la clef privee"""
    M = a1*b1-1
    e = a2*M+a1
    d = b2*M+b1
    n = int((e*d-1)/M)
    return (e,n),(d,n)

def chiffre_message(m,clef):
    pass

def bruteForceKIDRSA(e,n):
    pass

def egcd(a,b):
    pass

def modinv(e,n):
    pass


## Test

assert inverser_chaine_carcatere("NSI") == "ISN"

assert convertit_binaire_vers_un_entier_en_base_10("01001110") == 78

assert convertit_binaire_en_texte("010011100101001101001001") == 'NSI'

assert chiffre_xor("0101001101010000010001010100001101001001010000010100110001001001010101000100010100100000010011100101001101001001","01010100010001010101001001001101") == "0000011100010101000101110000111000011101000001000001111000000100000000000000000001110010000000110000011100001100"

assert convertit_texte_en_binaire( "SPECIALITE NSI" ) =="0101001101010000010001010100001101001001010000010100110001001001010101000100010100100000010011100101001101001001"

assert convertit_texte_en_binaire( "TERM" ) ==  "01010100010001010101001001001101"


##Exemple

message = "SPECIALITE NSI"
clef = "TERM"
message_binaire = convertit_texte_en_binaire(message)
print(message,"en binaire",message_binaire)
clef_binaire = convertit_texte_en_binaire(clef)
print(clef,"en binaire",clef_binaire)
message_binaire_chiffre = chiffre_xor(message_binaire,clef_binaire)
print("message chiffré" ,message_binaire_chiffre)
message_binaire_dechiffre = chiffre_xor(message_binaire_chiffre,clef_binaire)
print("message_binaire_dechiffre",message_binaire_dechiffre)
print("message dechiffré en ASCII",convertit_binaire_en_texte(message_binaire_dechiffre))
