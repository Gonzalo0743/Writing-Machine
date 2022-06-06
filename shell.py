import WritingMachine
from tkinter import *

alive = True


while alive:
	# text = input('WritingMachine > ')
	# if text.strip() == "": continue
	input_memory = open("memory.txt", "r")
	file = input_memory.read()

	comand = f'RUN("{file}")'

	result, error = WritingMachine.run(file, comand)

	if error:
		print(error.as_string())
	#Quiza eliminar?
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))

	alive = False
