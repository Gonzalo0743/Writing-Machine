import compOnlyWM
from tkinter import *

alive = True


while alive:

	input_memory = open("memory.txt", "r")
	file = input_memory.read()

	comand = f'RUN("{file}")'

	result, error = compOnlyWM.run(file, comand)

	if error:
		print("Ups!\n")
		print(error.as_string())
	elif result:
		print("Compilation complete, nothing to fix! ;)")


	alive = False
