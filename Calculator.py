from tkinter import *  

#creating the main application window.   
root = Tk() 
# root.geometry("240x280")
root.title("Calculator")

x = Entry(root, width=30, borderwidth=6)
x.grid(padx=30, pady=10, row=0, column=0, columnspan=4)

def button_click(value):

	current=x.get()
	# deleting existing values
	x.delete(0, END)    

	# new
	x.insert(0,str(current)+ str(value))

def button_clear():
	x.delete(0, END)   


def add():
	global firstNum
	global operation
	firstNum=int(x.get())
	x.delete(0, END)

	operation="+"

def sub():
	global firstNum
	global operation
	firstNum=int(x.get())
	x.delete(0, END)

	operation="-"


def mul():
	global firstNum
	global operation
	firstNum=int(x.get())
	x.delete(0, END)

	operation="*"

def div():
	global firstNum
	global operation
	firstNum=int(x.get())
	x.delete(0, END)

	operation="/"

def ans():
	secondNum=x.get()
	x.delete(0, END)
	if(operation=="+"):
		x.insert(0, firstNum + int(secondNum))

	if(operation=="-"):
		x.insert(0, firstNum - int(secondNum))

	if(operation=="*"):
		x.insert(0, firstNum * int(secondNum))

	if(operation=="/"):
		x.insert(0, firstNum / int(secondNum))



button0 = Button(root, text = "0", padx=25, pady=20, command=lambda:button_click(0)).grid(row=4, column=1)
button1 = Button(root, text = "1", padx=25, pady=20,command=lambda:button_click(1)).grid(row=3, column=0)
button2 = Button(root, text = "2", padx=25, pady=20,command=lambda:button_click(2)).grid(row=3 , column=1 )
button3 = Button(root, text = "3", padx=25, pady=20,command=lambda:button_click(3)).grid(row=3, column=2)

button4 = Button(root, text = "4", padx=25, pady=20,command=lambda:button_click(4)).grid(row=2 , column=0 )
button5 = Button(root, text = "5", padx=25, pady=20,command=lambda:button_click(5)).grid(row=2 , column=1 )
button6 = Button(root, text = "6", padx=25, pady=20,command=lambda:button_click(6)).grid(row=2 , column=2 )

button7 = Button(root, text = "7", padx=25, pady=20,command=lambda:button_click(7)).grid(row=1 , column=0 )
button8 = Button(root, text = "8", padx=25, pady=20,command=lambda:button_click(8)).grid(row=1 , column=1 )
button9 = Button(root, text = "9", padx=25, pady=20,command=lambda:button_click(9)).grid(row=1 , column=2 )


addition = Button(root, text = "+", padx=27, pady=20, bg='#6699cc', command=add).grid(row=1 , column=3)
substraction = Button(root, text = " - ", padx=25, pady=20, bg='#6699cc', command=sub).grid(row=2 , column=3)
multiplication = Button(root, text = " x ", padx=25, pady=20, bg='#6699cc', command=mul).grid(row=3 , column=3 )
division = Button(root, text = " / ", padx=25, pady=20, bg='#6699cc',command=div).grid(row=4 , column=3 )
answer = Button(root, text = "=", padx=24, pady=20, bg = '#40E0D0',command=ans).grid(row=4 , column=2)
clear = Button(root, text = "C", padx=25, pady=20, bg='#6699cc', command=button_clear).grid(row=4, column=0)





root.mainloop()
