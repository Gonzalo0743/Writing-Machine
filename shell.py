import WritingMachine
from tkinter import *

alive = True


while alive:

	input_memory = open("memory.txt", "r")
	file = input_memory.read()

	comand = f'RUN("{file}")'

	result, error = WritingMachine.run(file, comand)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))

	alive = False
