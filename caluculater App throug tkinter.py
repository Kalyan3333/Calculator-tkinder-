from tkinter import *
import parser

root = Tk()
# name of the gui
root.title('calculator')
# creating a function to the given statements
i=0
def get_var(num):
    global i
    display.insert(i,num)
    i=i+1
def clear_all():
    display.delete(0,END)

def get_oparation(operator):
    global i
    length=len(operator)
    display.insert(i,operator)
    i+=length

def undo():
    entire_string=display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,'error')

def calculator():
    entire_string=display.get()
    try:
        a=parser.expr(entire_string).compile()
        result=eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,'error')

display = Entry(root)
# to creat the input size of the calculator
display.grid(row=1,columnspan=6)
# placing number's position
Button(root,text='1',command=lambda :get_var(1)).grid(row=2,column=0)
Button(root,text='2',command=lambda :get_var(2)).grid(row=2,column=1)
Button(root,text='3',command=lambda :get_var(3)).grid(row=2,column=2)

Button(root,text='4',command=lambda :get_var(4)).grid(row=3,column=0)
Button(root,text='5',command=lambda :get_var(5)).grid(row=3,column=1)
Button(root,text='6',command=lambda :get_var(6)).grid(row=3,column=2)

Button(root,text='7',command=lambda :get_var(7)).grid(row=4,column=0)
Button(root,text='8',command=lambda :get_var(8)).grid(row=4,column=1)
Button(root,text='9',command=lambda :get_var(9)).grid(row=4,column=2)
# placing operators position
Button(root,text='Ac',command=lambda :clear_all()).grid(row=5,column=0)
Button(root,text='0',command=lambda :get_var(0)).grid(row=5,column=1)
Button(root,text='=',command= lambda :calculator()).grid(row=5,column=2)

Button(root,text='+',command=lambda :get_var('+')).grid(row=2,column=4)
Button(root,text='-',command=lambda :get_var('-')).grid(row=3,column=4)
Button(root,text='*',command=lambda :get_var('*')).grid(row=4,column=4)
Button(root,text='/',command=lambda :get_var('/')).grid(row=5,column=4)

Button(root,text='pi',command=lambda :get_var('3.14')).grid(row=2,column=5)
Button(root,text='%',command=lambda :get_var('%')).grid(row=3,column=5)
Button(root,text='(',command=lambda :get_var('(')).grid(row=4,column=5)
Button(root,text=')',command=lambda :get_var(')')).grid(row=5,column=5)

Button(root,text='x!',command=lambda :get_var('x!')).grid(row=2,column=6)
Button(root,text='->',command=lambda :undo()).grid(row=3,column=6)
Button(root,text='^2',command=lambda :get_var('**2')).grid(row=4,column=6)
Button(root,text='00',command=lambda :get_var('00')).grid(row=5,column=6)
root.mainloop()


# END