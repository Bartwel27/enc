from os.path import exists
from time import sleep
from os import system
from sys import argv
import os

from termcolor import colored

# functions
	
def _clear():
	try:
		clear = lambda:os.system("clear")
		return clear()
	except:
		clear = lambda:os.system("clr")
		return clear()


'''
                                  25
                                   |limit is 25 charecters
                   10        20    26
                    |         |    ||index 26 indicates space in string
          01234567890123456789212345678> index 27 is a special charecter becouse it does not change
									   \ index 28 is a dot
'''  
letter = "abcdefghijklmnopqrstuvwxyz ,."
charec = "~`|×[]%=\^÷?!;:'*@>$_&-+()#,."
upperl = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
upperc = "•√π≈¶∆}{°№¥€¢£©®™±Ωμ<Π₹₱★‽"
number = "0123456789"

letters = []
charecters = []
uletter = []
ucharec = []
numbers = [0,1,2,3,4,5,6,7,8,9]

letters.extend(letter)
charecters.extend(charec)
uletter.extend(upperl)
ucharec.extend(upperc)

#print(uletter)
#print(ucharec)

def _wordencrypt():
	userinput = input(colored("Enter:=> ","magenta"))
	userstore = ""
	for word in userinput:
		if word in letters[0]:
			userstore = userstore + charecters[0]
		elif word in letters[1]:
			userstore = userstore + charecters[1]
		elif word in letters[2]:
			userstore = userstore + charecters[2]
		elif word in letters[3]:
			userstore = userstore + charecters[3]
		elif word in letters[4]:
			userstore = userstore + charecters[4]
		elif word in letters[5]:
			userstore = userstore + charecters[5]
		elif word in letters[6]:
			userstore = userstore + charecters[6]
		elif word in letters[7]:
			userstore = userstore + charecters[7]
		elif word in letters[8]:
			userstore = userstore + charecters[8]
		elif word in letters[9]:
			userstore = userstore + charecters[9]
		elif word in letters[10]:
			userstore = userstore + charecters[10]
		elif word in letters[11]:
			userstore = userstore + charecters[11]
		elif word in letters[12]:
			userstore = userstore + charecters[12]
		elif word in letters[13]:
			userstore = userstore + charecters[13]
		elif word in letters[14]:
			userstore = userstore + charecters[14]
		elif word in letters[15]:
			userstore = userstore + charecters[15]
		elif word in letters[16]:
			userstore = userstore + charecters[16]
		elif word in letters[17]:
			userstore = userstore + charecters[17]
		elif word in letters[18]:
			userstore = userstore + charecters[18]
		elif word in letters[19]:
			userstore = userstore + charecters[19]
		elif word in letters[20]:
			userstore = userstore + charecters[20]
		elif word in letters[21]:
			userstore = userstore + charecters[21]
		elif word in letters[22]:
			userstore = userstore + charecters[22]
		elif word in letters[23]:
			userstore = userstore + charecters[23]
		elif word in letters[24]:
			userstore = userstore + charecters[24]
		elif word in letters[25]:
			userstore = userstore + charecters[25]
		elif word in letters[26]:
			userstore = userstore + charecters[26]
		elif word in letters[27]:
			userstore = userstore + charecters[27]
		elif word in letters[28]:
			userstore = userstore + charecters[28]
		
		
		# upper characters
		elif word in uletter[0]:
			userstore = userstore + ucharec[0]
		elif word in uletter[1]:
			userstore = userstore + ucharec[1]
		elif word in uletter[2]:
			userstore = userstore + ucharec[2]
		elif word in uletter[3]:
			userstore = userstore + ucharec[3]
		elif word in uletter[4]:
			userstore = userstore + ucharec[4]
		elif word in uletter[5]:
			userstore = userstore + ucharec[5]
		elif word in uletter[6]:
			userstore = userstore + ucharec[6]
		elif word in uletter[7]:
			userstore = userstore + ucharec[7]
		elif word in uletter[8]:
			userstore = userstore + ucharec[8]
		elif word in uletter[9]:
			userstore = userstore + ucharec[9]
		elif word in uletter[10]:
			userstore = userstore + ucharec[10]
		elif word in uletter[11]:
			userstore = userstore + ucharec[11]
		elif word in uletter[12]:
			userstore = userstore + ucharec[12]
		elif word in uletter[13]:
			userstore = userstore + ucharec[13]
		elif word in uletter[14]:
			userstore = userstore + ucharec[14]
		elif word in uletter[15]:
			userstore = userstore + ucharec[15]
		elif word in uletter[16]:
			userstore = userstore + ucharec[16]
		elif word in uletter[17]:
			userstore = userstore + ucharec[17]
		elif word in uletter[18]:
			userstore = userstore + ucharec[18]
		elif word in uletter[19]:
			userstore = userstore + ucharec[19]
		elif word in uletter[20]:
			userstore = userstore + ucharec[20]
		elif word in uletter[21]:
			userstore = userstore + ucharec[21]
		elif word in uletter[22]:
			userstore = userstore + ucharec[22]
		elif word in uletter[23]:
			userstore = userstore + ucharec[23]
		elif word in uletter[24]:
			userstore = userstore + ucharec[24]
		elif word in uletter[25]:
			userstore = userstore + ucharec[25]
		
		
		
		# reverse characters
		elif word in ucharec[0]:
			userstore = userstore + uletter[0]
		elif word in ucharec[1]:
			userstore = userstore + uletter[1]
		elif word in ucharec[2]:
			userstore = userstore + uletter[2]
		elif word in ucharec[3]:
			userstore = userstore + uletter[3]
		elif word in ucharec[4]:
			userstore = userstore + uletter[4]
		elif word in ucharec[5]:
			userstore = userstore + uletter[5]
		elif word in ucharec[6]:
			userstore = userstore + uletter[6]
		elif word in ucharec[7]:
			userstore = userstore + uletter[7]
		elif word in ucharec[8]:
			userstore = userstore + uletter[8]
		elif word in ucharec[9]:
			userstore = userstore + uletter[9]
		elif word in ucharec[10]:
			userstore = userstore + uletter[10]
		elif word in ucharec[11]:
			userstore = userstore + uletter[11]
		elif word in ucharec[12]:
			userstore = userstore + uletter[12]
		elif word in ucharec[13]:
			userstore = userstore + uletter[13]
		elif word in ucharec[14]:
			userstore = userstore + uletter[14]
		elif word in ucharec[15]:
			userstore = userstore + uletter[15]
		elif word in ucharec[16]:
			userstore = userstore + uletter[16]
		elif word in ucharec[17]:
			userstore = userstore + uletter[17]
		elif word in ucharec[18]:
			userstore = userstore + uletter[18]
		elif word in ucharec[19]:
			userstore = userstore + uletter[19]
		elif word in ucharec[20]:
			userstore = userstore + uletter[20]
		elif word in ucharec[21]:
			userstore = userstore + uletter[21]
		elif word in ucharec[23]:
			userstore = userstore + uletter[23]
		elif word in ucharec[24]:
			userstore = userstore + uletter[24]	
			
		
		
		# from charecters to words
		elif word in charecters[0]:
			userstore = userstore + letters[0]
		elif word in charecters[1]:
			userstore = userstore + letters[1]
		elif word in charecters[2]:
			userstore = userstore + letters[2]
		elif word in charecters[3]:
			userstore = userstore + letters[3]
		elif word in charecters[4]:
			userstore = userstore + letters[4]
		elif word in charecters[5]:
			userstore = userstore + letters[5]
		elif word in charecters[6]:
			userstore = userstore + letters[6]
		elif word in charecters[7]:
			userstore = userstore + letters[7]
		elif word in charecters[8]:
			userstore = userstore + letters[8]
		elif word in charecters[9]:
			userstore = userstore + letters[9]
		elif word in charecters[10]:
			userstore = userstore + letters[10]
		elif word in charecters[11]:
			userstore = userstore + letters[11]
		elif word in charecters[12]:
			userstore = userstore + letters[12]
		elif word in charecters[13]:
			userstore = userstore + letters[13]
		elif word in charecters[14]:
			userstore = userstore + letters[14]
		elif word in charecters[15]:
			userstore = userstore + letters[15]
		elif word in charecters[16]:
			userstore = userstore + letters[16]
		elif word in charecters[17]:
			userstore = userstore + letters[17]
		elif word in charecters[18]:
			userstore = userstore + letters[18]
		elif word in charecters[19]:
			userstore = userstore + letters[19]
		elif word in charecters[20]:
			userstore = userstore + letters[20]
		elif word in charecters[21]:
			userstore = userstore + letters[21]
		elif word in charecters[22]:
			userstore = userstore + letters[22]
		elif word in charecters[23]:
			userstore = userstore + letters[23]
		elif word in charecters[24]:
			userstore = userstore + letters[24]
		elif word in charecters[25]:
			userstore = userstore + letters[25]
		elif word in charecters[26]:
			userstore = userstore + letters[26]
		elif word in charecters[27]:
			userstore = userstore + letters[27]
		elif word in charecters[28]:
			userstore = userstore + letters[28]
		
		
		# for number
		elif word in str(numbers[0]):
			userstore = userstore + str(numbers[0])
		elif word in str(numbers[1]):
			userstore = userstore + str(numbers[1])
		elif word in str(numbers[2]):
			userstore = userstore + str(numbers[2])
		elif word in str(numbers[3]):
			userstore = userstore + str(numbers[3])
		elif word in str(numbers[4]):
			userstore = userstore + str(numbers[4])
		elif word in str(numbers[5]):
			userstore = userstore + str(numbers[5])
		elif word in str(numbers[6]):
			userstore = userstore + str(numbers[6])
		elif word in str(numbers[7]):
			userstore = userstore + str(numbers[7])
		elif word in str(numbers[8]):
			userstore = userstore + str(numbers[8])
		elif word in str(numbers[9]):
			userstore = userstore + str(numbers[9])
		
				
		else:
			userstore = userstore + colored("error", "red")
	print(colored("results:=> ","green") + userstore)
	
															
_clear()
try:
	script, command = argv
	if command == "--fenc":
		print("[+] files [+]")
		
	elif command == "--wenc":
		print("[+] encrypting [+]")
		while True:
			_wordencrypt()
			
	elif command == "--help" or command == "--h" or command == "-h":
		print("\t[+] Help menu [+]")
		h = ("""
 --fenc :   Its used to encrypt any type of file
 --wenc :   Its used to encrypt words in strings
 --benc :   Used to encrypt binary number into random chars
 --help :   Its used to display this menu message
		""")
		print(h)
except ValueError as ve:
	p = ("""
	
	Argument    action
	________   ____________________________
	--fenc     file encryption & decryption
	--wenc     word encryption & decryption
	--benc     Used to encrypt binary numbers
	--help     prints out a menu of command
	""");print(p,"\n",ve)
