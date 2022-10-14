from tkinter import*
import parser
page = Tk()

def get_variables(num):
	display.insert(END, num)
	
def calculate():
	entire_string = display.get('1.0', 'end-1c')
	try:
		a = parser.expr(entire_string).compile()
		result = eval(a)
		clear_all()
		display.insert(0.0, result)
	except Exception:
		clear_all()
		display.insert(0.0, 'Error')
		
def clear_all():
	display.delete(0.0, END)
	
def undo():
	entire_string = display.get('1.0', 'end-1c')
	if len(entire_string):
		new_string = entire_string[:-1]
		clear_all()
		display.insert(1.0, new_string)	
	else:
		clear_all()
		display.insert(0.0, 'Error')	

Label(page, text='CALCULATOR', font=('arial',8,'bold')).grid(row=0, columnspan=4)

display = Text(page, width=30, height=3)
display.grid(row=1, columnspan=4)

def buttons(txt,com,row,col):
	out = Button(page, text=txt, command=com, width=3,height=3).grid(row=row, column=col)
	return out
	
def buttonz(txt,com,row,col):
	out = Button(page, text=txt, command=com, width=10, height=3).grid(row=row, column=col, columnspan=2)
	return out

buttons('/', lambda:get_variables('/'), 2, 3)
buttons('<<', undo, 2, 2)
buttons('7', lambda:get_variables('7'), 3, 0)
buttons('8', lambda:get_variables('8'), 3, 1)
buttons('9', lambda:get_variables('9'), 3, 2)
buttons('x', lambda:get_variables('*'), 3, 3)
buttons('4', lambda:get_variables('4'), 4, 0)
buttons('5', lambda:get_variables('5'), 4, 1)
buttons('6', lambda:get_variables('6'), 4, 2)
buttons('-', lambda:get_variables('-'), 4, 3)
buttons('1', lambda:get_variables('1'), 5, 0)
buttons('2', lambda:get_variables('2'), 5, 1)
buttons('3', lambda:get_variables('3'), 5, 2)
buttons('+', lambda:get_variables('+'), 5, 3)
buttons('.', lambda:get_variables('.'), 6, 0)
buttons('0', lambda:get_variables('0'), 6, 1)
buttonz('C', clear_all, 2, 0)
buttonz('=', calculate, 6, 2)

page.mainloop()