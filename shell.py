import basic
from tkinter import *

alive = True


while alive:
	# text = input('WritingMachine > ')
	# if text.strip() == "": continue
	input_memory = open("memory.txt", "r")
	file = input_memory.read()

	# file = 'example.myopl'
	comand = f'RUN("{file}")'

	result, error = basic.run(file, comand)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))

	alive = False
