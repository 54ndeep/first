import tkinter
from tkinter import *
from tkinter import messagebox

win= tkinter.Tk()
win.geometry("250x400")
win.resizable(0,0)
win.title("calculator")
win.iconbitmap(r'favicon.ico')

# Functions

val =''
A = 0
operetor = ''

def btn1_hover(button):
    btn1["bg"]="white"

def btn1_end_hover(button):
    btn1["bg"]="SystemButtonFace"
    

def btn2_hover(button):
    btn2["bg"]="white"

def btn2_end_hover(button):
    btn2["bg"]="SystemButtonFace"
    

def btn3_hover(button):
    btn3["bg"]="white"

def btn3_end_hover(button):
    btn3["bg"]="SystemButtonFace"
    

def btn4_hover(button):
    btn4["bg"]="white"

def btn4_end_hover(button):
    btn4["bg"]="SystemButtonFace"


def btn5_hover(button):
    btn5["bg"]="white"

def btn5_end_hover(button):
    btn5["bg"]="SystemButtonFace"


def btn6_hover(button):
    btn6["bg"]="white"

def btn6_end_hover(button):
    btn6["bg"]="SystemButtonFace"


def btn7_hover(button):
    btn7["bg"]="white"

def btn7_end_hover(button):
    btn7["bg"]="SystemButtonFace"


def btn8_hover(button):
    btn8["bg"]="white"

def btn8_end_hover(button):
    btn8["bg"]="SystemButtonFace"


def btn9_hover(button):
    btn9["bg"]="white"

def btn9_end_hover(button):
    btn9["bg"]="SystemButtonFace"


def btn_zero_hover(button):
    btn_zero["bg"]="white"

def btn_zero_end_hover(button):
    btn_zero["bg"]="SystemButtonFace"


def btn_plus_hover(button):
    btn_plus["bg"]="white"

def btn_plus_end_hover(button):
    btn_plus["bg"]="SystemButtonFace"
    

def btn_sub_hover(button):
    btn_substract["bg"]="white"

def btn_sub_end_hover(button):
    btn_substract["bg"]="SystemButtonFace"
    

def btn_divide_hover(button):
    btn_divide["bg"]="white"

def btn_divide_end_hover(button):
    btn_divide["bg"]="SystemButtonFace"
    

def btn_cancel_hover(button):
    btn_cancel["bg"]="white"

def btn_cancel_end_hover(button):
    btn_cancel["bg"]="SystemButtonFace"


def btn_multiply_hover(button):
    btn_multiply["bg"]="white"

def btn_multiply_end_hover(button):
    btn_multiply["bg"]="SystemButtonFace"


def btn_equal_hover(button):
    btn_equal["bg"]="white"

def btn_equal_end_hover(button):
    btn_equal["bg"]="SystemButtonFace"

#First row button funtion

def btn_1_clicked():
    global val
    val= val +'1'
    data.set(val)

def btn_2_clicked():
    global val
    val= val +'2'
    data.set(val)

def btn_3_clicked():
    global val
    val= val +'3'
    data.set(val)

def btn_plus_clicked():
    global val
    global A
    global operetor
    A = int(val)
    operetor = '+'
    val= val +'+'
    data.set(val)

#Second row button function

def btn_4_clicked():
    global val
    val= val +'4'
    data.set(val)

def btn_5_clicked():
    global val
    val= val +'5'
    data.set(val)

def btn_6_clicked():
    global val
    val= val +'6'
    data.set(val)

def btn_subs_clicked():
    global val
    global A
    global operetor
    A = int(val)
    operetor = '-'
    val= val +'-'
    data.set(val)

#third row button function

def btn_7_clicked():
    global val
    val= val +'7'
    data.set(val)

def btn_8_clicked():
    global val
    val= val +'8'
    data.set(val)

def btn_9_clicked():
    global val
    val= val +'9'
    data.set(val)

def btn_div_clicked():
    global val
    global A
    global operetor
    A = int(val)
    operetor = '/'
    val= val +'/'
    data.set(val)

#Fourth row button function

def btn_zero_clicked():
    global val
    val= val +'0'
    data.set(val)

def btn_clear_clicked():
    global val
    global A
    global operetor
    A = 0
    operetor = ''
    val= ''
    data.set(val)

def btn_multy_clicked():
    global val
    global A
    global operetor
    A = int(val)
    operetor = '*'
    val= val +'*'
    data.set(val)

def btn_equal_clicked():
    global val
    global A
    global operetor
    val2= val
    if operetor == '+':
        plus = int((val2.split('+')[1]))
        plus_result= A + plus
        data.set(plus_result)
        val = str(plus_result)

    elif operetor == '-':
        sub = int((val2.split('-')[1]))
        sub_result= A - sub
        data.set(sub_result)
        val = str(sub_result)

    elif operetor == '*':
        mlt = int((val2.split('*')[1]))
        mlt_result= A * mlt
        data.set(mlt_result)
        val = str(mlt_result)

    elif operetor == '/':
        div = int((val2.split('/')[1]))
        if div == 0:
            messagebox.showerror('Error','You cant divide from 0')
            val =''
            A=0
            data.set(val)
        else:
            div_result=int( A / div)
            data.set(div_result)
            val = str(div_result)   

# Functions Ends here.
data= StringVar()

lbl= Label(win,text= "calculator", font=('verdana',20),anchor= SE, textvariable= data,background= '#000000',fg='#ffffff', relief= SOLID, border= (2))
lbl.pack( expand=True, fill= 'both')

row1= Frame(win)
row1.pack(expand= True, fill ='both')

row2= Frame(win)
row2.pack(expand= True, fill ='both')

row3= Frame(win)
row3.pack(expand= True, fill ='both')

row4= Frame(win)
row4.pack(expand= True, fill ='both')

#First rows buttons

btn1= Button(row1, text= '1', font=('verdana',20),relief= GROOVE, border= (0), command= btn_1_clicked,)
btn1.pack(expand=True, fill='both', side= LEFT ,)

btn2= Button(row1, text= '2', font=('verdana',20),relief= GROOVE, border= (0), command= btn_2_clicked,)
btn2.pack(expand=True, fill='both', side= LEFT )

btn3= Button(row1, text= '3', font=('verdana',20),relief= GROOVE, border= (0), command= btn_3_clicked,)
btn3.pack(expand=True, fill='both', side= LEFT )

btn_plus= Button(row1, text= '+', font=('verdana',20),relief= GROOVE, border= (0), command= btn_plus_clicked,)
btn_plus.pack(expand=True, fill='both', side= LEFT )

#Second rows buttons

btn4= Button(row2, text= '4', font=('verdana',20),relief= GROOVE, border= (0), command= btn_4_clicked,)
btn4.pack(expand=True, fill='both', side= LEFT )

btn5= Button(row2, text= '5', font=('verdana',20),relief= GROOVE, border= (0), command= btn_5_clicked,)
btn5.pack(expand=True, fill='both', side= LEFT )

btn6= Button(row2, text= '6', font=('verdana',20),relief= GROOVE, border= (0), command= btn_6_clicked,)
btn6.pack(expand=True, fill='both', side= LEFT )

btn_substract= Button(row2, text= '-', font=('verdana',20),relief= GROOVE, border= (0), command= btn_subs_clicked,)
btn_substract.pack(expand=True, fill='both' , side= LEFT)

#Third rows buttons

btn7= Button(row3, text= '7', font=('verdana',20),relief= GROOVE, border= (0), command= btn_7_clicked,)
btn7.pack(expand=True, fill='both', side= LEFT )

btn8= Button(row3, text= '8', font=('verdana',20),relief= GROOVE, border= (0), command= btn_8_clicked,)
btn8.pack(expand=True, fill='both', side= LEFT )

btn9= Button(row3, text= '9', font=('verdana',20),relief= GROOVE, border= (0), command= btn_9_clicked,)
btn9.pack(expand=True, fill='both', side= LEFT )

btn_divide= Button(row3, text= '/', font=('verdana',20),relief= GROOVE, border= (0), command= btn_div_clicked,)
btn_divide.pack(expand=True, fill='both' , side= LEFT)

#Fourth rows buttons

btn_zero= Button(row4, text= '0', font=('verdana',20),relief= GROOVE, border= (0), command= btn_zero_clicked,)
btn_zero.pack(expand=True, fill='both', side= LEFT )

btn_multiply= Button(row4, text= '*', font=('verdana',20),relief= GROOVE, border= (0), command= btn_multy_clicked,)
btn_multiply.pack(expand=True, fill='both', side= LEFT )

btn_cancel= Button(row4, text= 'C', font=('verdana',20),relief= GROOVE, border= (0), command= btn_clear_clicked,)
btn_cancel.pack(expand=True, fill='both', side= LEFT )

btn_equal= Button(row4, text= '=', font=('verdana',20),relief= GROOVE, border= (0), command= btn_equal_clicked,)
btn_equal.pack(expand=True, fill='both' , side= LEFT)

#hover 

btn1.bind('<Enter>', btn1_hover)
btn1.bind('<Leave>',btn1_end_hover)

btn2.bind('<Enter>', btn2_hover)
btn2.bind('<Leave>',btn2_end_hover)

btn3.bind('<Enter>', btn3_hover)
btn3.bind('<Leave>',btn3_end_hover)

btn4.bind('<Enter>', btn4_hover)
btn4.bind('<Leave>',btn4_end_hover)

btn5.bind('<Enter>', btn5_hover)
btn5.bind('<Leave>',btn5_end_hover)

btn6.bind('<Enter>', btn6_hover)
btn6.bind('<Leave>',btn6_end_hover)

btn7.bind('<Enter>', btn7_hover)
btn7.bind('<Leave>',btn7_end_hover)

btn8.bind('<Enter>', btn8_hover)
btn8.bind('<Leave>',btn8_end_hover)

btn9.bind('<Enter>', btn9_hover)
btn9.bind('<Leave>',btn9_end_hover)

btn_zero.bind('<Enter>', btn_zero_hover)
btn_zero.bind('<Leave>',btn_zero_end_hover)

btn_plus.bind('<Enter>', btn_plus_hover)
btn_plus.bind('<Leave>',btn_plus_end_hover)

btn_substract.bind('<Enter>', btn_sub_hover)
btn_substract.bind('<Leave>',btn_sub_end_hover)

btn_multiply.bind('<Enter>', btn_multiply_hover)
btn_multiply.bind('<Leave>',btn_multiply_end_hover)

btn_divide.bind('<Enter>', btn_divide_hover)
btn_divide.bind('<Leave>',btn_divide_end_hover)

btn_equal.bind('<Enter>', btn_equal_hover)
btn_equal.bind('<Leave>',btn_equal_end_hover)

btn_cancel.bind('<Enter>', btn_cancel_hover)
btn_cancel.bind('<Leave>',btn_cancel_end_hover)


win.mainloop()