from tkinter import *
def btn_click(number):
    global operator
    operator=operator+str(number)
    txt_input.set(operator)
def btn_eq():
    global operator
    op=str(eval(operator))
    txt_input.set(op)
def btn_del():
    value=txt_input.get()
    value=value[:-1]
    txt_input.set(value)
def btn_clr():
    global operator
    operator=""
    txt_input.set(operator)
#making a calculator
window=Tk()
window.title("Welcome to Calculator")
window.geometry("250x250")
operator=""#first an empty value should be given
txt_input=StringVar()#to store string values
#entry
display=Entry(window,font=('arial',10),bg='gray',bd=20,textvariable=txt_input).grid(columnspan=4)
#buttons
button_1=Button(window,text="1",padx="20",command=lambda:btn_click('1'))
button_2=Button(window,text="2",padx="20",command=lambda:btn_click('2'))
button_3=Button(window,text="3",padx="20",command=lambda:btn_click('3'))
button_4=Button(window,text="4",padx="20",command=lambda:btn_click('4'))
button_5=Button(window,text="5",padx="20",command=lambda:btn_click('5'))
button_6=Button(window,text="6",padx="20",command=lambda:btn_click('6'))
button_7=Button(window,text="7",padx="20",command=lambda:btn_click('7'))
button_8=Button(window,text="8",padx="20",command=lambda:btn_click('8'))
button_9=Button(window,text="9",padx="20",command=lambda:btn_click('9'))
button_0=Button(window,text="0",padx="20",command=lambda:btn_click('0'))
button_de=Button(window,text=".",padx="20",command=lambda:btn_click('.'))
button_C=Button(window,text="C",padx="18",command=lambda:btn_del())
button_D=Button(window,text="/",padx="20",command=lambda:btn_click('/'))
button_M=Button(window,text="*",padx="20",command=lambda:btn_click('*'))
button_S=Button(window,text="-",padx="20",command=lambda:btn_click('-'))
button_A=Button(window,text="+",pady="20",padx="18",command=lambda:btn_click('+'))
button_E=Button(window,text="Enter",pady="14",padx="8",command=lambda:btn_eq())
button_clr=Button(window,text="AC",padx="20",command=lambda:btn_clr())
#buttons_placements
button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_0.grid(row=5,column=0)
button_clr.grid(row=5,column=1)
button_de.grid(row=5,column=2)
button_C.grid(row=1,column=0)
button_D.grid(row=1,column=1)
button_M.grid(row=1,column=2)
button_S.grid(row=1,column=3)
button_A.grid(row=2,rowspan=2,column=3)
button_E.grid(row=4,rowspan=2,column=3)
window.mainloop()
