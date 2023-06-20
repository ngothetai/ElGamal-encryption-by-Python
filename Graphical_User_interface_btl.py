from tkinter import *
top= Tk()
top.title('Graphical Use Interface')
top.geometry('1200x500')
top['bg']="#FFFFFF"
top.attributes("-topmost",True)
 
canvas = Canvas(top, width=1200, height=500)
canvas.pack()

# vẽ đường thẳng dọc màu đỏ
canvas.create_line(320, 0, 320, 500, fill="black")


# vẽ đường thẳng dọc màu đỏ
canvas.create_line(760, 0, 760, 500, fill="black")

name = Label(top,text = 'Encrypt', font=('Arial Black',14))
name.place(x=350,y=60)

name1= Label(top, text ='Decrypt',font=('Arial Black',14))
name1.place(x= 770,y=60)

name2= Label(top,text= 'Plaintext')
name2.place(x= 350,y=170)

name3= Label(top,text= 'Codetext')
name3.place(x= 350, y= 330)

name4= Label(top,text= 'Plaintext')
name4.place(x= 770,y=170)

name5= Label(top,text= 'Codetext')
name5.place(x= 770, y= 330)

but = Button(top, text = 'Encrypt',bg='Cyan',width = '10')
but.place(x= 470,y=280)

but1= Button(top,text = 'File', bg ='Cyan', width ='10', height='2')
but1.place(x= 650, y = 190)

but2 =Button(top, text = "Convert", bg= 'Cyan', width = '10')
but2.place(x= 650, y = 360)

but3= Button(top, text= 'Store', bg = 'Cyan', width = '10')
but3.place(x= 650 , y = 390 )

other= Button(top, text = 'Decrypt', bg= "Cyan", width= '10 ')
other.place(x= 890, y = 280)

other1 = Button(top, text = 'File ', bg = "Cyan", width = '10', height = '2')
other1.place(x= 1070, y = 190 )

other2 = Button(top,text = 'Store', bg = "Cyan", width = '10', height = '2')
other2.place(x= 1070, y = 360)

box= Text(top, width= "25", relief="solid", height = '5' )
box.place(x= 420 , y= 150)

box1= Text(top, width='25', relief="solid", height = '5' )
box1.place(x= 850 , y= 150)

box2= Text(top, width= "25",relief="solid",  height = '5' )
box2.place(x= 420 , y= 360)

box3= Text(top, width= "25",relief="solid", height = '5' )
box3.place(x= 850 , y= 360)



title = Label(top, text= 'Make Key', font=('Arial Black',14))
title.place(x= 50 , y = 60 )

iconP = Label(top, text = '     P:    ', font= ('Arial', 10),bg="#DDDDDD")
iconP.place(x= 50 , y = 150)

iconAnpha= Label(top, text= " Anpha: ",font= ('Arial', 10 ), bg="#DDDDDD")
iconAnpha.place(x= 50, y=180)

iconA= Label(top,text= "     A:    ", font= ("Arial", 10),bg="#DDDDDD")
iconA.place(x=50,y=210)

a1= Text(top, width= "20",relief="solid", height = '1' )
a1.place(x= 110 , y= 150)

a2= Text(top, width= "20",relief="solid", height = '1' )
a2.place(x= 110 , y= 180)

a3= Text(top, width= "20",relief="solid", height = '1' )
a3.place(x= 110 , y= 210)

#but = Button(top, text = 'Encrypt',bg='Cyan',width = '10')
#but.place(x= 470,y=280)
iconBeta = Label(top, text = '  Beta:  ', font= ('Arial', 10),bg="#DDDDDD")
iconBeta.place(x= 50 , y = 300)

iconK= Label(top, text= "    K:    ",font= ('Arial', 10 ), bg="#DDDDDD")
iconK.place(x= 50, y=330)

b1= Button(top, text ='Make Key', bg= 'Cyan', width= '10')
b1.place(x=150, y = 250 )

a2= Text(top, width= "20",relief="solid", height = '1' )
a2.place(x= 110 , y= 300)

a3= Text(top, width= "20",relief="solid", height = '1' )
a3.place(x= 110 , y= 330)

b2= Button(top, text ='Random Key', bg= 'Cyan', width= '10')
b2.place(x=150, y = 360 )

b3= Button(top, text ='Delete Data', bg= 'Cyan', width= '10')
b3.place(x=150, y = 400 )

#make key 

#write sth 
#name = Label(top,text = 'Encrypt', font=('Arial Black ',14))
#name.place(x=350,y=60)



top.mainloop()