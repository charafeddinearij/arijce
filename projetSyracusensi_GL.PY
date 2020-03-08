'''
Suite de Syracuse

Gayaneh Lustermann, 1er G2
Arij Charaf-Eddine, 1er G6

1.11.2019
'''

import sys 
import numpy as np
import matplotlib.pyplot as plt

# intro pour l'utlisateur
print(''' 
Welcome to the world of Syracuse sequence!
==========================================

Grace a ce programme vous pouvez tester la suite de Syracuse.
La suite de Syracuse c'est quoi?

La conjecture de Syracuse dit que peu importe le nombre, a la fin de la sequence de nombre naturel, on termine toujours par le cycle trivial.
- Si le nombre est pair: On le divise par 2.
- Si le nombre est impair: On le multiplie par 3 puis on lui ajoute 1.
On fait cela jusqu'a finir par 4, 2, 1.   
	
Si vous utilisez ce programme, entrez un nombre obligatoirement entier > 0 s'il vous plait.
''')



# demande a l'utlisateur le nombre start pour la suite syracuse
start = input("Avec quel nombre veux-tu tester la suite de Syracuse? ")
# verification de la validite de la valeur d'entree
try: 
	t = int(start)
except:
	print(start,' is not an integer, aborting program!')
	sys.exit()	

if t < 1:
	print('L\'entier doit etre plus grand que 0!')
	sys.exit()


# calcul et sauvgarde de la suite de syracuse	
history = []	
			
N = int(start)
history.append(N)
while N != 1:
	if N%2 == 0:
		N = N/2			
	elif  N%2 == 1:
		N = (N*3+1)/2
	history.append(N)

tempsDeVol = len(history)-1 # -1 enleve la valeur initiale car pas une iteration

## resultats				
# graphique representant la suite complete

historyArray = np.array(history)
plt.plot(historyArray,'r.-')
plt.xlabel('Iteration - Temps de vol')
plt.ylabel('Valeur - Altitude')	
plt.title('Suite de Syracuse')	
plt.grid(True)
plt.show()				
		
# selectionne fin de la suite, representation graphique, impression des resultats		
historyLength = 12
if tempsDeVol + 1 < historyLength:
	historyLength = tempsDeVol + 1
	
if len(history) > historyLength:
	shortHistory = history[-historyLength:]
else:
	shortHistory = history
	
shortHistoryArray = np.array(shortHistory)
plt.figure()
plt.plot(shortHistoryArray,'r.-')
plt.xlabel('Iteration - Temps de vol')
plt.ylabel('Valeur - Altitude')	
plt.title('Suite de Syracuse, derniere ' + str(historyLength) +' iterations')	
plt.grid(True)
plt.show()	
			
print('La suite de syracuse des dernieres ' + str(historyLength) + ' iterations est:', shortHistory)

print('Le temps de vol est de:', tempsDeVol)


	
	


