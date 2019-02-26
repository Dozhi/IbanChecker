#python3
#DominykasZogas
from schwifty import IBAN
import string
import sys
import os


#starter function
def main():
	greeting_console()


#turn on console and cast user input
def greeting_console():
	print("Press 1 for : IBAN number checking from user input")
	print("Press 2 for : IBAN number checking from text file")
	print(" 'exit'  for exit")

	console_input_taker()

#console's user input taker
def console_input_taker():
	user_answer = input(">>")
	console_input_checker(user_answer)

#checks user input
def console_input_checker(answer):
	if answer == "1":
		get_iban()
	elif answer == "2":
		file_searcher()
	elif answer == "exit":
		sys.exit("exiting...")
	else:
		print("Wrong input")
		greeting_console()
#after user input it's option1 and takes and check given IBAN by user
def get_iban():
	iban_answer = input(">> IBAN: ")
	try:
		check_iban(iban_answer)
		print("IBAN is correct") 
	except ValueError:
		print("IBAN is incorrect")
	greeting_console()


#option2 asks user file's name and locaiton
def file_searcher():
	file_name = input(">>File name : ")
	file_location = input(">>File location :")
	check_and_write_file(file_name , file_location)


def file_taker(file_name , file_location):
	file = open(file_name , "r")
	print(file.read())
	print(file_location)
	file.close()
#check file , reads given file and writes/append new one
def check_and_write_file(first_file_name , first_file_location):
			#give final and checked user location 
			def give_final_location(final_first_file_name , final_first_file_location):
				final_first_file_location+=final_first_file_name
				abs_path = os.path.abspath(final_first_file_location)
				return abs_path
				#change file's name for final action
			def give_final_name(final_name):
				left_final_name = final_name.partition(".")[0]
				return left_final_name	
				#writes to new file 
			def write_file(first_file_second_name , line , value):
				with open(give_final_name(first_file_second_name)+".out.txt" , "a") as file:	
					file.write(line+":"+value+"\n")
					file.close()


			try:
				first_file = open(give_final_location(first_file_name , first_file_location) , "r")

				lines = first_file.readlines()

				for line in lines:	
					try:
						check_iban(line)
						write_file(first_file_name , line,"true")

					except ValueError:
						write_file(first_file_name , line,"false")
				print("Everyting done correctly")
				greeting_console()

			except OSError as e:
				print("File not found")
				greeting_console()
#iban checker
LETTERS = {ord(d): str(i) for i, d in enumerate(string.digits + string.ascii_uppercase)}


def _number_iban(iban):
    return (iban[4:] + iban[:4]).translate(LETTERS)


def generate_iban_check_digits(iban):
    number_iban = _number_iban(iban[:2] + '00' + iban[4:])
    return '{:0>2}'.format(98 - (int(number_iban) % 97))


def valid_iban(iban):
    return int(_number_iban(iban)) % 97 == 1


def check_iban(iban):

    if generate_iban_check_digits(iban) == iban[2:4] and valid_iban(iban):
        print('IBAN ok!\n')
    else:
        print('IBAN not ok!\n')



"""


IBAN CHECKER
"""
if __name__ == '__main__':
	main()