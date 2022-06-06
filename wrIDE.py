from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
import os

compiler = Tk()
compiler.title('Writing Machine IDE')
file_path = ''
file_name = ''

def set_file_path(path):
    global file_path, file_name
    file_path = path
    file_name = os.path.basename(file_path)
    input_memory = open("memory.txt", "w")
    input_memory.write(file_name)
    print(file_name)

def get_file_name():
    return file_name

def open_file():
    path = askopenfilename(filetypes=[('WM Files', '*.wrm')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)


def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('WM Files', '*.wrm')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)


def run():
    code_output.delete('1.0', END)
    code_output.insert('1.0', "Running..\n")
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Before running,save your code')
        text.pack()
        return
    shell_path = "shell.py"
    command = f'python {shell_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert(END, output)
    code_output.insert(END,  error)

def compile():
    code_output.delete('1.0', END)
    code_output.insert('1.0', "Compiling..\n")
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Before running,save your code')
        text.pack()
        return
    shell_path = "compileShell.py"
    command = f'python {shell_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()

    code_output.insert(END,  error)
    code_output.insert(END, output)


menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As' , command=save_as)
file_menu.add_command(label='Exit')
menu_bar.add_cascade(label='File', menu=file_menu)

run_button = Button(compiler, text= '         Run         ', command=run)
run_button.grid(row=1, column=9)

compile_button = Button(compiler, text= '         Compile         ', command=compile)
compile_button.grid(row=1, column=0)

compiler.config(menu=menu_bar)

editor = Text()
editor.config(bg= '#362f2e', fg= '#d2ded1', insertbackground= 'white')
editor.grid(row=0, columnspan=10)

code_output = Text(height=10)
code_output.config(bg= '#362f2e', fg= '#d2ded1', insertbackground= 'white')
code_output.grid(row=2, columnspan=10)
code_output.insert("1.0", "Welcome to Writing Machine IDE! \nRemember to save your code each time before running! ^-^")

compiler.mainloop()