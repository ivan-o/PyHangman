import random
import string
import subprocess

#=================================#
#---DEF---------------------------#
#=================================#
def clear():
	subprocess.call("clear", shell=True)
	return

def testo(n):
	if lan == 1:
		diz = {
		0 : "\n\
\t#==============================================#\n\
\t#              GIOCO DELL'IMPICCATO            #\n\
\t#==============================================#\n\
\t#                                              #\n\
\t#  Lo scopo del gioco e' di          --------  #\n\
\t#  indovinare la parola celata,      |/        #\n\
\t#  aggiungendo una lettera alla      |         #\n\
\t#  volta.                            |         #\n\
\t#  Man mano che si fanno errori,     |         #\n\
\t#  viene costruito il patibolo.      |         #\n\
\t#  Evita di essere...             ---+---      #\n\
\t#                                 |  |  |      #\n\
\t#                 IMPICCATO!!!                 #\n\
\t#                                              #\n\
\t#==============================================#\n",
		1 : "\n\n INIZIA QUI!\n\n >>> Scegli la difficolta': 12 o 7 errori?\n (digita l'opzione desiderata e poi primo invio): ",
		2 : "\n\n Inserire un input valido!",
		3 : " Desideri l'aiuto delle lettere iniziali e finali? (y/n)\n (digita l'opzione desiderata e poi primo invio): ",
		4 : "\tLETTERE USATE:",
		5 : "\n\tInserisci una lettera da aggiungere alla parola e poi premi invio: ",
		6 : "\n\n\tLettera gia' utilizzata!",
		7 : "\n\n\tInserire un input valido!",
		8 : "\n\n\n\tVuoi giocare un'altra partita? (y/n)\n\t(digita l'opzione desiderata e poi primo invio): "
		}

	elif lan == 2:
		diz = {
		0 : "\n\
\t#==============================================#\n\
\t#                  HANGMAN GAME                #\n\
\t#==============================================#\n\
\t#                                              #\n\
\t#  The aim of the game is to guess   --------  #\n\
\t#  the hidden word by adding         |/        #\n\
\t#  a letter at a time.               |         #\n\
\t#  As you make mistakes, it is       |         #\n\
\t#  built the gallows.                |         #\n\
\t#  Avoid being...                    |         #\n\
\t#                                 ---+---      #\n\
\t#                  HANGED!!!      |  |  |      #\n\
\t#                                              #\n\
\t#==============================================#\n",
		1 : "\n\n START HERE!\n\n >>> Choose your difficulty: 12 or 7 errors?\n (enter the desired option and then hit execute): ",
		2 : "\n\n Enter a valid input!",
		3 : " Do you want the help of the initial and final letters? (y/n)\n (enter the desired option and then hit execute): ",
		4 : "\tLETTERS USED:",
		5 : "\n\tEnter a letter to be added to the word and then hit execute: ",
		6 : "\n\n\tLetter already used!",
		7 : "\n\n\tEnter a valid input!",
		8 : "\n\n\n\tYou want to play another game? (y/n)\n\t(enter the desired option and then hit execute):"
		}

	else: print "\n\n\t\t!!! ERROR: def testo() !!!\n\n"

	return diz[n]

def fig(e,stmp):
	s = ""
	for i in stmp: s += (i + ' ')

	print "\n" * 2

	if e == 0: print "\
\n\
\t\t                 \" %s\"\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n" % (s)

	elif e == 1: print "\
\n\
\t\t                 \" %s\"\n\
\n\
\n\
\n\
\n\
\n\
\n\
\t\t|  |  |\n" % (s)

	elif e == 2: print "\
\n\
\t\t                 \" %s\"\n\
\n\
\n\
\n\
\n\
\n\
\t\t-------\n\
\t\t|  |  |\n" % (s)

	elif e == 3: print "\
\n\
\t\t                 \" %s\"\n\
\t\t   |\n\
\t\t   |\n\
\t\t   |\n\
\t\t   |\n\
\t\t   |\n\
\t\t---+---\n\
\t\t|  |  |\n" % (s)

	elif e == 4: print "\
\n\
\t\t   --------      \" %s\"\n\
\t\t   |\n\
\t\t   |\n\
\t\t   |\n\
\t\t   |\n\
\t\t   |\n\
\t\t---+---\n\
\t\t|  |  |\n" % (s)

	elif e == 5: print "\
\n\
\t\t   --------      \" %s\"\n\
\t\t   |/\n\
\t\t   |\n\
\t\t   |\n\
\t\t   |\n\
\t\t   |\n\
\t\t---+---\n\
\t\t|  |  |\n" % (s)

	elif e == 6: print "\
\n\
\t\t   --------      \" %s\"\n\
\t\t   |/\n\
\t\t   |      O\n\
\t\t   |\n\
\t\t   |\n\
\t\t   |\n\
\t\t---+---\n\
\t\t|  |  |\n" % (s)

	elif e == 7: print "\
\n\
\t\t   --------      \" %s\"\n\
\t\t   |/\n\
\t\t   |      O\n\
\t\t   |      |\n\
\t\t   |\n\
\t\t   |\n\
\t\t---+---\n\
\t\t|  |  |\n" % (s)

	elif e == 8: print "\
\n\
\t\t   --------      \" %s\"\n\
\t\t   |/\n\
\t\t   |      O\n\
\t\t   |      |\n\
\t\t   |     /\n\
\t\t   |\n\
\t\t---+---\n\
\t\t|  |  |\n" % (s)

	elif e == 9: print "\
\n\
\t\t   --------      \" %s\"\n\
\t\t   |/\n\
\t\t   |      O\n\
\t\t   |      |\n\
\t\t   |     / \ \n\
\t\t   |\n\
\t\t---+---\n\
\t\t|  |  |\n" % (s)

	elif e == 10: print "\
\n\
\t\t   --------      \" %s\"\n\
\t\t   |/\n\
\t\t   |      O\n\
\t\t   |     /|\n\
\t\t   |     / \ \n\
\t\t   |\n\
\t\t---+---\n\
\t\t|  |  |\n" % (s)

	elif e == 11: print "\
\n\
\t\t   --------      \" %s\"\n\
\t\t   |/\n\
\t\t   |      O\n\
\t\t   |     /|\ \n\
\t\t   |     / \ \n\
\t\t   |\n\
\t\t---+---\n\
\t\t|  |  |\n" % (s)

	elif e == 12 and lan == 1: print "\
\n\
\t\t   --------      \" %s\"\n\
\t\t   |/     |\n\
\t\t   |     \O/\n\
\t\t   |      |  - GAME OVER - La parola era \" %s\".\n\
\t\t   |     / \ \n\
\t\t   |\n\
\t\t---+---\n\
\t\t|  |  |\n" % (s, parola)

	elif e == 12 and lan == 2: print "\
\n\
\t\t   --------      \" %s\"\n\
\t\t   |/     |\n\
\t\t   |     \O/\n\
\t\t   |      |  - GAME OVER - The word is \" %s\".\n\
\t\t   |     / \ \n\
\t\t   |\n\
\t\t---+---\n\
\t\t|  |  |\n" % (s, parola)

	elif e == 0.5: print "\
\n\
\t\t   --------      \" %s\"\n\
\t\t   |/\n\
\t\t   |\n\
\t\t   |           !!! YOU WIN !!!\n\
\t\t   |\n\
\t\t   |       O/\n\
\t\t---+---   /|\n\
\t\t|  |  |   / \ \n" % (s)

	return

#=================================#
#---PROGRAMMA---------------------#
#=================================#

clear()
w0 = 0
while w0 == 0:
	l = raw_input("\n\n >>> SCEGLI LA LINGUA / CHOOSE THE LANGUAGE\n\n\t(1)\titaliano\n\t(2)\tenglish\n\n (digita l'opzione desiderata e poi primo invio / choose the option and click enter): ")
	l = l.lower()
	if l == 'ita' or l == '1' or l == 'italiano':
		lan = 1
		w0 = 1
	elif l == 'eng' or l == '2' or l == 'english':
		lan = 2
		w0 = 1
	else: print "\n\n Inserire un input valido! / Insert a valid input!"

clear()

print testo(0)

# CICLO NUOVO GIOCO
ripeti = 1
while ripeti == 1:

	# IMPOSTAZIONI
	w1 = 0
	while w1 == 0:
		d = raw_input(testo(1))
		if d == '12' or d == '7': w1 = 1
		else: print testo(2)

	print

	w2 = 0
	while w2 == 0:
		a = raw_input(testo(3))
		a = a.lower()
		if a == 'y' or a == 'yes':
			aiuto = 1
			w2 = 1
		elif a == 'n' or a == 'no':
			aiuto = 0
			w2 = 1
		else: print testo(2)

	# DIFFICOLTA'
	errore = 0
	if d == '7': errore = 5

	usate = []

	corta = 1
	while corta == 1:
		if lan ==1: vocaboli = open('diz_ita.txt','r')
		elif lan == 2: vocaboli = open('diz_eng.txt','r')
		else: print "\n\n\t\t!!! ERROR: while corta !!!\n\n"
		diz_ita = vocaboli.read().split()
		vocaboli.close()
		diz_ita.sort()
		caso = random.randint(0, (len(diz_ita)-1))
		parola = diz_ita[caso]
		if len(parola) <= 4: corta = 1
		else: corta = 0

	# PREPARAZIONE PAROLA STAMPATA
	stampa = []
	for i in range(0, len(parola)): stampa.append('_')

	# AIUTI
	if aiuto == 1:
		stampa[0] = parola[0]
		stampa[-1] = parola[-1]
		usate.append(parola[0])
		usate.append(parola[-1])
		i = 0
		for l in parola:
			if l == parola[0]: stampa[i] = parola[0]
			elif l == parola[-1]: stampa[i] = parola[-1]
			i += 1

	clear()

	# CICLO
	game = 0
	while game == 0:
		# stampa
		fig(errore,stampa)

		print testo(4),
		for u in usate: print u,
		print "\n"

		# input
		w3 = 0
		while w3 == 0:
			lettera = raw_input(testo(5))
			lettera = lettera.lower()
			if lettera in string.lowercase:
				w3 = 1
				if lettera in usate:
					print testo(6),
					w3 = 0
					continue
				else:
					usate.append(lettera)
					usate.sort()

			if w3 == 0:
				print testo(7),

		# controllo lettera
		if lettera in parola:
			for i in range(0,len(parola)):
				if lettera == parola[i]: stampa[i] = lettera
		else: errore += 1

		# controllo partita
		ctrl = ""
		for i in stampa: ctrl += i
		if ctrl == parola:
			errore = 0.5
			game = 2

		# controllo errori
		if errore >= 12:
			errore = 12
			game = 1

		clear()

	# FINE CICLO

	if game == 2:
		fig(errore,stampa)
		print testo(4),
		for u in usate: print u,
		print "\n"

	if game == 1:
		fig(errore,stampa)
		print testo(4),
		for u in usate: print u,
		print "\n"

	w4 = 0
	while w4 == 0:
		a = raw_input(testo(8))
		a = a.lower()
		if a == 'y' or a == 'yes':
			w4 = 1
			clear()
		elif a == 'n' or a == 'no':
			ripeti = 0
			w4 = 1
		else: print testo(7),

print "\n\n\t\tEND\n"
