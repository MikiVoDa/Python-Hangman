import random
from os import system, name
def cls():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
print("Hangman by Kikian.\n")
mai_ai_0 = '''
   +------+
   |      |
   O      |
  /|\     |
   |      |
  / \     |
          |
        =====
'''
mai_ai_1 = '''
   +------+
   |      |
   O      |
  /|\     |
   |      |
  /       |
          |
        =====
'''
mai_ai_2 = '''
   +------+
   |      |
   O      |
  /|\     |
   |      |
          |
          |
        =====
'''
mai_ai_3 = '''
   +------+
   |      |
   O      |
  /|      |
   |      |
          |
          |
        =====
'''     # desenele pentru spanzuratoare
mai_ai_4 = '''
   +------+
   |      |
   O      |
   |      |
   |      |
          |
          |
        =====
'''
mai_ai_5 = '''
   +------+
   |      |
   O      |
          |
          |
          |
          |
        =====
'''
mai_ai_6 = '''
   +------+
   |      |
          |
          |
          |
          |
          |
        =====
'''
vieti = [mai_ai_6, mai_ai_5, mai_ai_4, mai_ai_3, mai_ai_2, mai_ai_1, mai_ai_0] # lista de desene
lista_cuvinte = ["mangusta", "minotaur", "balaur", "dinozaur", "jmeker", "deca"] # lista de cuvinte
cuvant_cheie = random.choice(lista_cuvinte) # se alege un cuvant random
# print(f"Psst, cuvantul e {cuvant_cheie}, asta asa pentru test.")
cuvant_cheie_ascuns = [] # pregatim un alt cuvant ca sa il avem ascuns de ___
for litera in cuvant_cheie:
    cuvant_cheie_ascuns.append("_")     # cream cuvantul ascuns de ___
vieti_ramase = 0                # tinem cont de vietile ramase
cuvant_cheie_conditie = []      # tinem cuvantul ca o lista de elemente pentru a usura munca
for litera in cuvant_cheie:
    cuvant_cheie_conditie.append(litera) # cream conditia si tinem cuvantul ca sa lucram cu el
while cuvant_cheie_conditie != cuvant_cheie_ascuns and vieti_ramase != 6:       # cat timp lista de elemente (adica cuvantul) este ghicit complet si nu am pierdut toate vietile
        ghiceste = input("Ghiceste o litera: ") # ghicim litere
        cls()
        guess = ghiceste.lower()        # transformam orice litera ghicita in litere mici
        k=-1 # counter
        schimbat = 0 # verificator
        for litera in cuvant_cheie:     # daca ghicim litera/e din cuvant vor fii inlocuite sau vom pierde vieti daca nu am ghicit
            k+=1
            if guess == cuvant_cheie[k]:
                cuvant_cheie_ascuns[k] = litera         # plus in forul asta faca sa nu iti mai arate odata cuvantul ghicit
                schimbat += 1                           # aici fac doar codul sa iese frumos
        if vieti_ramase == 6:
            vieti_ramase += 1
        elif cuvant_cheie_conditie == cuvant_cheie_ascuns:
            break
        elif schimbat == 0:
            vieti_ramase += 1
            print(vieti[vieti_ramase])
            print("Ups, ai gresit!")
            print(' '.join(cuvant_cheie_ascuns))

        elif schimbat != 0:
            print(vieti[vieti_ramase])
            print("Nice, continua tot asa!")
            print(' '.join(cuvant_cheie_ascuns))
if cuvant_cheie_conditie == cuvant_cheie_ascuns:        # ultima data ne dam seama ce urare trimitem. daca a castigat sau daca a pierdut
    print(cuvant_cheie)
    print("Ai castigat!")
elif vieti_ramase == 6:
    print("Ai pierdut!")
    print(f"Cuvantul era {cuvant_cheie}...")