from tkinter import *
from numpy import var
import time

mpr = Tk()
mpr.geometry("2000x2000")

def open_win():
    top = Toplevel()

    WIDTH=2000
    HEIGHT=2000

    canvas = Canvas(top,width=WIDTH,height=HEIGHT, background='white')
    canvas.pack()
    label = Label(top, text="SELECTION SORT", font= ('Courier 35 underline')).place(x = 570, y = 50)

    image_2=PhotoImage(file='ani/numbers/number-2.png')
    image_7=PhotoImage(file='ani/numbers/number-7.png')
    image_8=PhotoImage(file='ani/numbers/number-8.png')
    image_9=PhotoImage(file='ani/numbers/number-9.png')
    image_11=PhotoImage(file='ani/numbers/number-11.png')
    image_5=PhotoImage(file='ani/numbers/number-5.png')
    image_4=PhotoImage(file='ani/numbers/number-4.png')
    image_3=PhotoImage(file='ani/numbers/number-3.png')
    image2=image_2.subsample(5,5)
    image7=image_7.subsample(5,5)
    image8=image_8.subsample(5,5)
    image9=image_9.subsample(5,5)
    image11=image_11.subsample(5,5)
    image5=image_5.subsample(5,5)
    image4=image_4.subsample(5,5)
    image3=image_3.subsample(5,5)
    my_image2= canvas.create_image(316,250,image=image2,anchor=NW)
    my_image7= canvas.create_image(1243,250,image=image7,anchor=NW)
    my_image8= canvas.create_image(775,250,image=image8,anchor=NW)
    my_image9= canvas.create_image(469,250,image=image9,anchor=NW)
    my_image11= canvas.create_image(163,250,image=image11,anchor=NW)
    my_image5= canvas.create_image(1081,250,image=image5,anchor=NW)
    my_image4= canvas.create_image(928,250,image=image4,anchor=NW)
    my_image3= canvas.create_image(622,250,image=image3,anchor=NW)
    
    def animsort():
        xVelocity=1
        xVelocity3=0
        xVelocity7=0
        xVelocity9=0
        xVelocity11=0
        xVelocity4=0
        xVelocity5=0
        xVelocity8=0

        while True:  
            coordinates=canvas.coords(my_image2)
            coordinates7=canvas.coords(my_image7)
            coordinates8=canvas.coords(my_image8)
            coordinates11=canvas.coords(my_image11)
            coordinates9=canvas.coords(my_image9)
            coordinates5=canvas.coords(my_image5)
            coordinates4=canvas.coords(my_image4)
            coordinates3=canvas.coords(my_image3)
            if(coordinates[0]==316 and coordinates11[0]==163):
                xVelocity=-xVelocity
                xVelocity11=1

            if(coordinates[0]==163 and coordinates11[0]==316):
                xVelocity=0
                label2= Label(top, text="i=1:  [2,11,9,3,8,4,5,7]", font= ('Bold 25')).place(x = 163, y = 410)
                time.sleep(0.2)

            if(coordinates3[0]==622 and coordinates[0]==163):
                xVelocity3=-1

            if(coordinates11[0]==622 or coordinates3[0]==316 and (coordinates9[0]==469 and coordinates4[0]==928)):
                xVelocity11=0
                xVelocity3=0
                label3= Label(top, text="i=2:  [2,3,9,11,8,4,5,7]", font= ('Bold 25')).place(x = 163, y = 470)

                xVelocity9=1
                xVelocity4=-1
            if(coordinates11[0]==622 and (coordinates4[0]==469 or coordinates9[0]==928)):
                xVelocity9=0
                xVelocity4=0
                label4= Label(top, text="i=3:  [2,3,4,11,8,9,5,7]", font= ('Bold 25')).place(x = 163, y = 530)

            if(coordinates11[0]==622 and coordinates5[0]==1081 and coordinates4[0]==469):
                xVelocity11=1
                xVelocity5=-1
            if(coordinates5[0]==622 and coordinates11[0]==1081):
                xVelocity11=0
                xVelocity5=0
                label5= Label(top, text="i=4:  [2,3,4,5,8,9,11,7]", font= ('Bold 25')).place(x = 163, y = 590)

            if(coordinates7[0]==1243 and coordinates8[0]==775 and coordinates11[0]==1081):
                xVelocity7=-1
                xVelocity8=1

            if(coordinates8[0]==1243 or coordinates7[0]==775 and coordinates9[0]==928):
                xVelocity7=0
                xVelocity8=0
                label6= Label(top, text="i=5:  [2,3,4,5,7,9,11,8]", font= ('Bold 25')).place(x = 963, y = 410)
                time.sleep(0.2)

            if(coordinates7[0]==775 and coordinates9[0]==928):
                xVelocity8=-1
                xVelocity9=1

            if(coordinates8[0]==928 and coordinates9[0]==1243):
                label7= Label(top, text="i=6:  [2,3,4,5,7,8,11,9]", font= ('Bold 25')).place(x = 963, y = 470)
                xVelocity8=0
                xVelocity9=0

            if(coordinates9[0]==1243):
                xVelocity9=-1
                xVelocity11=1

            if(coordinates11[0]==1243 and  coordinates9[0]==1081):
                label7= Label(top, text="i=7:  [2,3,4,5,7,8,9,11]", font= ('Bold 25')).place(x = 963, y = 530)
                label8= Label(top, text="SORTED:  [2,3,4,5,7,8,9,11]", font= ('Bold 25')).place(x =570, y = 650)

                xVelocity9=0
                xVelocity11=0
            
            canvas.move(my_image2,xVelocity,0)
            canvas.move(my_image3,xVelocity3,0)
            canvas.move(my_image11,xVelocity11,0)
            canvas.move(my_image7,xVelocity7,0)
            canvas.move(my_image9,xVelocity9,0)
            canvas.move(my_image4,xVelocity4,0)
            canvas.move(my_image5,xVelocity5,0)
            canvas.move(my_image8,xVelocity8,0)
            top.update()
            time.sleep(0.01)
    btn = Button(top, width=7,height=1,text="SORT", command= lambda:animsort()).place(x=700, y=500)     
    top.mainloop()

    
def win():
    top = Toplevel()
    WIDTH=2000
    HEIGHT=2000

    canvas = Canvas(top,width=WIDTH,height=HEIGHT, background='white')
    canvas.pack()
    label = Label(top, text="INSERTION SORT", font= ('Courier 35 underline')).place(x = 570, y = 50)

    image_2=PhotoImage(file='ani/numbers/number-2.png')
    image_7=PhotoImage(file='ani/numbers/number-7.png')
    image_8=PhotoImage(file='ani/numbers/number-8.png')
    image_9=PhotoImage(file='ani/numbers/number-9.png')
    image_11=PhotoImage(file='ani/numbers/number-11.png')
    image_5=PhotoImage(file='ani/numbers/number-5.png')
    image_4=PhotoImage(file='ani/numbers/number-4.png')
    image_3=PhotoImage(file='ani/numbers/number-3.png')
    image2=image_2.subsample(5,5)
    image7=image_7.subsample(5,5)
    image8=image_8.subsample(5,5)
    image9=image_9.subsample(5,5)
    image11=image_11.subsample(5,5)
    image5=image_5.subsample(5,5)
    image4=image_4.subsample(5,5)
    image3=image_3.subsample(5,5)
    my_image4= canvas.create_image(163,250,image=image4,anchor=NW)
    my_image7= canvas.create_image(316,250,image=image7,anchor=NW)
    my_image8= canvas.create_image(469,250,image=image8,anchor=NW)
    my_image9= canvas.create_image(622,250,image=image9,anchor=NW)
    my_image3= canvas.create_image(775,250,image=image3,anchor=NW)
    my_image2= canvas.create_image(928,250,image=image2,anchor=NW)
    my_image5= canvas.create_image(1081,250,image=image5,anchor=NW)
    my_image11= canvas.create_image(1243,250,image=image11,anchor=NW)

    def animsort():
        xVelocity=0
        xVelocity3=0
        xVelocity7=0
        xVelocity9=0
        xVelocity11=0
        xVelocity4=0
        xVelocity5=0
        xVelocity8=0
        yVelocity=0
        yVelocity3=0
        yVelocity7=0
        yVelocity9=0
        yVelocity11=0
        yVelocity4=0
        yVelocity5=0
        yVelocity8=0
    
        while True:  
            coordinates=canvas.coords(my_image2)
            coordinates7=canvas.coords(my_image7)
            coordinates8=canvas.coords(my_image8)
            coordinates11=canvas.coords(my_image11)
            coordinates9=canvas.coords(my_image9)
            coordinates5=canvas.coords(my_image5)
            coordinates4=canvas.coords(my_image4)
            coordinates3=canvas.coords(my_image3)
            
            if((coordinates[0]==928 and coordinates4[0]==163 ) and coordinates[1]==250):
                  yVelocity=1
                 
            if(coordinates[1]==400):
                  yVelocity=0
                  #time.sleep(0.2)

            if(coordinates4[0]==163 and coordinates[1]==400):
                  xVelocity3=1
                  xVelocity4=1
                  xVelocity7=1
                  xVelocity8=1
                  xVelocity9=1
            if(coordinates3[0]==928 and coordinates[1]==400):
                  xVelocity3=0
                  xVelocity4=0
                  xVelocity7=0
                  xVelocity8=0
                  xVelocity9=0
                  xVelocity=-1
                  
            if(coordinates[0]==163 and coordinates[1]==400):
                  xVelocity=0
                  yVelocity=-1
            if(coordinates[0]==163 and coordinates[1]==250 and coordinates3[0]==928):
                  yVelocity=0
                  label2= Label(top, text="i=1:  [2,4,7,8,9,3,5,11]", font= ('Bold 25')).place(x = 163, y = 500)

                  yVelocity3=1
            if(coordinates3[1]==400):
                  yVelocity3=0

            if(coordinates3[1]==400 and coordinates4[0]==316): 
                  xVelocity4=1
                  xVelocity7=1
                  xVelocity8=1
                  xVelocity9=1
            if(coordinates9[0]==928 and coordinates3[1]== 400):
                  xVelocity4=0
                  xVelocity7=0
                  xVelocity8=0
                  xVelocity9=0
                  xVelocity3=-1
            if(coordinates3[0]==316 and coordinates3[1]==400):
                  xVelocity3=0
                  yVelocity3=-1
            if(coordinates3[1]==250 and coordinates3[0]==316 and coordinates4[0]==469 and coordinates5[1]==250):
                  yVelocity3=0
                  label3= Label(top, text="i=2:  [2,3,4,7,8,9,5,11]", font= ('Bold 25')).place(x = 163, y = 570)

                  yVelocity5=1
            if(coordinates5[1]==400 and coordinates5[0]==1081):
                  yVelocity5=0

            if(coordinates5[1]==400 and coordinates4[0]==469):
                  xVelocity7=1
                  xVelocity8=1
                  xVelocity9=1
            if(coordinates9[0]==1081 and coordinates5[1]== 400):
                  xVelocity7=0
                  xVelocity8=0
                  xVelocity9=0
                  xVelocity5=-1
            if(coordinates5[0]==622 and coordinates5[1]==400):
                  xVelocity5=0
                  yVelocity5=-1
            if(coordinates5[1]==250 and coordinates5[0]==622 and coordinates7[0]==775):
                  yVelocity5=0
                  label4= Label(top, text="i=3:  [2,3,4,5,7,8,9,11]", font= ('Bold 25')).place(x = 163, y = 640)
                  label5= Label(top, text="SORTED:  [2,3,4,5,7,8,9,11]", font= ('Bold 25')).place(x = 900, y = 500)

            canvas.move(my_image2,xVelocity,yVelocity)
            canvas.move(my_image3,xVelocity3,yVelocity3)
            canvas.move(my_image11,xVelocity11,yVelocity11)
            canvas.move(my_image7,xVelocity7,yVelocity7)
            canvas.move(my_image9,xVelocity9,yVelocity9)
            canvas.move(my_image4,xVelocity4,yVelocity4)
            canvas.move(my_image5,xVelocity5,yVelocity5)
            canvas.move(my_image8,xVelocity8,yVelocity8)
            top.update()
            time.sleep(0.00)
    btn = Button(top, width=7,height=1,text="SORT", command= lambda: animsort()).place(x=700, y=600)     
    top.mainloop()
    

def win2():

    WIDTH=2000
    HEIGHT=2000
    top = Toplevel()
    canvas = Canvas(top,width=WIDTH,height=HEIGHT, background='white')
    canvas.pack()
    label = Label(top, text="HEAP SORT", font= ('Courier 35 underline')).place(x = 560, y = 50)

    image_2=PhotoImage(file='ani/numbers/number-2.png')
    image_11=PhotoImage(file='ani/numbers/number-11.png')
    image_5=PhotoImage(file='ani/numbers/number-5.png')
    image_4=PhotoImage(file='ani/numbers/number-4.png')
    image_3=PhotoImage(file='ani/numbers/number-3.png')
    image2=image_2.subsample(6,6)

    image11=image_11.subsample(6,6)
    image5=image_5.subsample(6,6)
    image4=image_4.subsample(6,6)
    image3=image_3.subsample(6,6)
    my_image2= canvas.create_image(775,600,image=image2,anchor=NW)
    my_image11= canvas.create_image(316,600,image=image11,anchor=NW)
    my_image5= canvas.create_image(622,600,image=image5,anchor=NW)
    my_image4= canvas.create_image(163,600,image=image4,anchor=NW)
    my_image3= canvas.create_image(469,600,image=image3,anchor=NW)
    def animsort():
            i=0
            xVelocity=0
            xVelocity3=0
            xVelocity11=0
            xVelocity4=0
            xVelocity5=0
            yVelocity4 = -1
            yVelocity5 = 0
            yVelocity3 = 0
            yVelocity11 = 0
            yVelocity = 0

            while True:  
                
                coordinates=canvas.coords(my_image2)
                coordinates11=canvas.coords(my_image11)
                coordinates5=canvas.coords(my_image5)
                coordinates4=canvas.coords(my_image4)
                coordinates3=canvas.coords(my_image3)
                if(coordinates4[1]==100 and coordinates11[0]==316):
                    yVelocity4=0
                    xVelocity4=1
                    xVelocity11 = -1
                if(coordinates4[0]==250):
                    xVelocity4=0
                if(coordinates11[0]==130 and coordinates11[1]==600):
                    xVelocity11 = 0
                    yVelocity11=-1
                if(coordinates11[1]==220 and coordinates3[1]==600):
                    # canvas.create_line(267,172,165,230, fill="red",width=2)
                   
                    yVelocity11=0
                    xVelocity3=-1
                if(coordinates3[0]==370 and coordinates3[1]==600):
                    yVelocity3=-1
                    xVelocity3=0
                if(coordinates3[1]==220 and coordinates5[0]==622 and i==0):
                    # canvas.create_line(325,172,420,230, fill="red",width=2)
                    
                    xVelocity5=-1
                    yVelocity3=0
                if(coordinates5[0]==10 and coordinates5[1]==600):
                    yVelocity5=-1
                    xVelocity5=0
                if(coordinates5[1]==340 and coordinates[0]==775):
                    #canvas.create_line(155,300,60,340, fill="red",width=2)
                    
                    xVelocity=-1
                    yVelocity5=0
                if(coordinates[0]==250 and coordinates[1]==600):
                    yVelocity=-1
                    xVelocity=0
                if(coordinates[1]==340 and coordinates[0]==250):
                    #canvas.create_line(180,300,275,340, fill="red",width=3)
                    
                    yVelocity=0  
                if(coordinates4[0]==250 and coordinates11[0]==130 and coordinates[1]==340):
                    label1 = Label(top, text="Step 1: Since 11 > 4, swap 4 with 11.\nSince 5 > 4,swap 4 with 5.\nSwap first and last node.\nRemove 11 from heap.", font=('Bold 15'), bg='black', fg='white').place(x=940, y=145)
                    label1
                    xVelocity11 =1
                    yVelocity11=-1
                    xVelocity4=-1
                    yVelocity4=1
                if(coordinates4[1]==220 and coordinates11[1]==100):
                    xVelocity11 =0
                    yVelocity11=0
                    xVelocity4=0
                    yVelocity4=0
                    time.sleep(0.2)
                if(coordinates4[0]==130 and coordinates5[0]==10 and coordinates11[1]==100):
                    xVelocity5 =1
                    yVelocity5=-1
                    xVelocity4=-1
                    yVelocity4=1
                if(coordinates4[1]==340 and coordinates5[1]==220):
                    xVelocity5 =0
                    yVelocity5=0
                    xVelocity4=0
                    yVelocity4=0
                if(coordinates[1]==340 and coordinates11[1]==100 and coordinates5[1]==220):
                    yVelocity11 =1
                    yVelocity =-1
                if(coordinates[1]==100 and coordinates11[1]==340):
                    yVelocity11=0
                    yVelocity=0
                    time.sleep(0.2)
                    yVelocity11=1
                if(coordinates11[1]==600 and coordinates11[0]==250 and coordinates[1]==100):
                    yVelocity11=0
                    xVelocity11=1
                if(coordinates11[1]==600 and coordinates11[0]==775 and coordinates[1]==100):
                    xVelocity11=0
                if(coordinates5[0]==130 and coordinates11[0]==775 and coordinates[1]==100 and i==0):
                    label2 = Label(top, text="Step 2: Since 5 > 2, swap 2 with 5.\nSince 4 > 2, swap 2 with 4.\nSwap first and last node.\nRemove 5 from heap.",font=('Bold 15'),bg='black', fg='white').place(x=940, y=275)
                    label2
                    xVelocity5=1
                    yVelocity5=-1
                    xVelocity=-1
                    yVelocity=1
                    i=1
                if(coordinates[0]==130 and coordinates5[1]==100 and coordinates[1]==220):
                    xVelocity=0
                    yVelocity=0
                    xVelocity5=0
                    yVelocity5=0
                    time.sleep(0.2)
                if(coordinates[0]==130 and coordinates4[0]==10 and coordinates5[1]==100):
                    xVelocity4=1
                    yVelocity4=-1
                    xVelocity=-1
                    yVelocity=1
                if(coordinates[0]==10 and coordinates4[1]==220 and coordinates4[0]==130):
                    xVelocity=0
                    yVelocity=0
                    xVelocity4=0
                    yVelocity4=0
                    time.sleep(0.2)
                if(coordinates5[0]==250 and coordinates[0]==10 and coordinates4[1]==220):
                    xVelocity=1
                    yVelocity=-1
                    xVelocity5=-1
                    yVelocity5=1
                if(coordinates[0]==250 and coordinates5[1]==340 and coordinates11[0]==775):
                    xVelocity=0
                    yVelocity=0
                    xVelocity5=0
                    yVelocity5=0
                    time.sleep(0.0002)
                    yVelocity5=1
                if(coordinates11[0]==775 and coordinates5[1]==600 and coordinates[1]==100 and i==1):
                    yVelocity5=0
                    xVelocity5=1
                    i=2
                if(coordinates11[0]==775 and coordinates5[0]==622 and coordinates[1]==100 and i==2):
                    xVelocity5=0
                    label3 = Label(top, text="Step 3: Since 4 > 2, swap 2 with 4.\nSwap first and last node.\nRemove 4 from heap.",font=('Bold 15'),bg='black', fg='white').place(x=940, y=402)
                    label3
                    xVelocity=-1
                    yVelocity=1
                    xVelocity4=1
                    yVelocity4=-1
                if(coordinates4[1]==100 and coordinates5[0]==622 and coordinates[1]==220):
                    xVelocity=0
                    yVelocity=0
                    xVelocity4=0
                    yVelocity4=0
                    i=3
                    time.sleep(0.2)
                if(coordinates4[1]==100 and coordinates3[0]==370 and i==3):
                    xVelocity3=-1
                    yVelocity3=-1
                    xVelocity4=1
                    yVelocity4=1
                    i=4
                if(coordinates4[0]==370 and coordinates3[1]==100):
                    xVelocity4=0
                    yVelocity4=0
                    xVelocity3=0
                    yVelocity3=0
                    yVelocity4=1
                if(coordinates4[1]==600 and coordinates3[1]==100 and coordinates4[0]==370):
                    yVelocity4=0
                    xVelocity4=1
                if(coordinates4[1]==600 and coordinates3[1]==100 and coordinates4[0]==469 ):
                    xVelocity4=0
                    label4 = Label(top, text="Step 4: 3 remove from heap as it\nwas max heap.", font=("Bold 15"),bg='black', fg='white').place(x=940, y=510)
                    label4
                    yVelocity3=1
                if(coordinates3[1]==600 and coordinates4[0]==469):
                    yVelocity3=0
                    xVelocity3=1
                if(coordinates3[1]==600 and coordinates3[0]==316 and i==4):
                    xVelocity3=0
                    label5 = Label(top, text="Step 5: 2 remove from heap.", font=("Bold 15"), bg='black', fg='white').place(x=940, y=600)
                    label5
                    yVelocity=1
                if(coordinates[1]==600 and coordinates3[0]==316 and i==4):
                    yVelocity=0
                    xVelocity=1
                    i=5
                if(coordinates[1]==600 and coordinates[0]==163 and i==5):
                    xVelocity=0
                    xVelocity3=0
                    label6 = Label(top, text="Sorted array : \n2 3 4 5 11", font=("Bold 20"), bg='black', fg='white').place(x=940, y=690)
                    label6

                canvas.move(my_image2,xVelocity,yVelocity)
                canvas.move(my_image3,xVelocity3,yVelocity3)
                canvas.move(my_image11,xVelocity11,yVelocity11)
                canvas.move(my_image4,xVelocity4,yVelocity4)
                canvas.move(my_image5,xVelocity5,yVelocity5)
                mpr.update()
                
    btn = Button(top, width=7,height=1,text="SORT", command= animsort).place(x=700, y=500)     
    top.mainloop()


C = Canvas(mpr)

canvas_make = Canvas(mpr, bg="gray", width=2000, height=100, relief=RAISED, bd=8)
canvas_make.place(x=0, y=0)
canvas_make = Canvas(mpr, bg="Black", width=750, height=1900, relief=RAISED, bd=8)
canvas_make.place(x=0, y=110)
canvas_make = Canvas(mpr, bg="black", width=820, height=1900, relief=RAISED, bd=8)
canvas_make.place(x=700, y=110)
#canvas_make = Canvas(mpr, bg="white", width=580, height=70, relief=RAISED, bd=5)
#canvas_make.place(x=35, y=570)
canvas_make = Canvas(mpr, bg="white", width=1600, height=600, relief=RAISED, bd=5)
canvas_make.place(x=150, y=580)


def printInput():
    inp = inputtxt.get("1.0","end")
    Var.append(inp)
    
def printl(Var):
    k=4
    for i in range (len(Var)):
        label2 = Label(mpr, text = "", font = 'Times 25')
        label2.place(x=k*55,y=590) 
        label2.config(text="%s" %Var[i],bg="white")  
        k=k+1
             

def clearToTextInput():
   inputtxt.delete("1.0","end")

label1 = Label(mpr, text="Sorting using LinkedList", font= ('Courier 30'),bg="gray").place(x = 450, y = 50)
label3 = Label(mpr, text="Select sorting technique:", font= ('Courier 22 bold'),bg="black",fg="white").place(x = 800, y = 140)
label2 = Label(mpr, text="Input here: ", font= ('Courier 20 bold'), bg="black", fg="white").place(x = 185, y = 200)
label4 = Label(mpr, text="Input: ", font="Times 20",bg="black", fg="white").place(x=70,y=590)
label5 = Label(mpr, text="Output:", font="Times 20",bg="black", fg="white").place(x=60,y=680)
label6= Label(mpr, text="Visualize here:", font="Courier 15 bold",bg="black", fg="white").place(x=235,y=350)
Var = []

inputtxt = Text(mpr,height =1.5, width = 10,font=20)
inputtxt.place(x=400, y=200)
Button(mpr , height=1,width=11, text="Insert",font='Times 12', bd=5,command=lambda: [ printInput(), clearToTextInput(), printl(Var)]).place(x=250,y=270)
Button(mpr , height=1,width=15, text="Visual Selection Sort",font='Times 15',bd=5, command=open_win).place(x=60,y=470)
Button(mpr , height=1,width=15, text="Visual Heap Sort",font='Times 15',bd=5, command=win2).place(x=235,y=400)                                                                        
Button(mpr , height=1,width=15, text="Visual Insertion Sort",font='Times 15',bd=5, command=win).place(x=410,y=470)

#Button(mpr, width=15,height=2,text="Add more", command=add_entries).place(x=20, y=120)
# Button(mpr, width=15,height=2,text="Sort", command= lambda:[LinkedList().selectionsortList()]).place(x=200, y=120)
Button(mpr, width=18,height=2,text="Bubble Sort",font="Times 15", bd=5, command = lambda: [LinkedList().bubblesortList(Var)]).place(x=800,y=210)
Button(mpr, width=18,height=2,text="Insertion Sort",font="Times 15",bd=5,command = lambda: [LinkedList().insertionsortList(Var)]).place(x=1065,y=210)
Button(mpr, width=18,height=2,text="Selection Sort",font="Times 15",bd=5,command = lambda: [LinkedList().selectionsortList(Var)]).place(x=800,y=305)
Button(mpr, width=18,height=2,text="Merge Sort",font="Times 15",bd=5,command = lambda: [LinkedList().insertionsortList(Var)]).place(x=1065,y=305)
Button(mpr, width=18,height=2,text="Heap Sort",font="Times 15",bd=5,command = lambda: [LinkedList().bubblesortList(Var)]).place(x=800,y=390)
Button(mpr, width=18,height=2,text="Bucket Sort",font="Times 15",bd=5,command = lambda: [LinkedList().selectionsortList(Var)]).place(x=1065,y=390)
Button(mpr, width=18,height=2,text="Quick Sort",font="Times 15",bd=5,command = lambda: [LinkedList().insertionsortList(Var)]).place(x=800,y=475)
Button(mpr, width=18,height=2,text="Modified Bubble Sort",font="Times 15",bd=5, command = lambda: [LinkedList().modifybubbleList(Var)]).place(x=1065,y=475)


class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        if(self.head==None): print("None")
        while(temp!=None):
                print(temp.data)
                temp = temp.next

    
    def insertAtend(self, data):
        newNode = Node(data)
        newNode.next = None 
        if (self.head == None) :
            self.head = newNode
            
        else:
              
                temp = self.head
                while(temp.next != None):
                        temp = temp.next
                temp.next = newNode
        print("Node inserted:",data) 


    def bubblesortList(self,Var):  
        for i in range (len(Var)):
            newNode = Node(Var[i])
            newNode.next = None 
            if (self.head == None) :
                self.head = newNode
            else:
                    temp = self.head
                    while(temp.next != None):
                            temp = temp.next
                    temp.next = newNode
        #Node current will point to head  
        current = self.head;  
        if(self.head == None):  
            return;  
        else:  
            while(current.next != None):  
                #Node index will point to node next to current  
                post = current.next;  
                while(post != None):  
                    #If current node's data is greater than index's node data, swap the data between them  
                      if(int(current.data) > int(post.data)):  
                            temp = current.data
                            current.data = post.data 
                            post.data = temp  
                      post = post.next  
                current = current.next
        temp = self.head
        if(self.head==None): print("None")
        while(temp!=None):
                i=10
                print(temp.data)
                temp = temp.next
        temp = self.head
        k=4
        while temp!=None:
            label4 = Label(mpr, text = temp.data , font = 'Times 25')
            label4.place(x=k*55,y=680) 
            label4.config(text="%s" %temp.data,bg="white") 
            temp = temp.next
            k=k+1
    

    def selectionsortList(self,Var):
        for i in range (len(Var)):
            newNode = Node(Var[i])
            newNode.next = None 
            if (self.head == None) :
                self.head = newNode
            else:
                    temp = self.head
                    while(temp.next != None):
                            temp = temp.next
                    temp.next = newNode
        current = self.head
        if(self.head == None):
            return
        else:
            while(current.next != None):
                new = current.next
                min = current
                while(new != None):
                    if(int(min.data) > int(new.data)):
                        min = new
                    new = new.next
                temp = min.data
                min.data = current.data
                current.data = temp
                current = current.next
        #printing----
        temp = self.head
        if(self.head==None): print("None")
        while(temp!=None):
                i=10
                print(temp.data)
                temp = temp.next
        temp = self.head
        k=4
        while temp!=None:
            label4 = Label(mpr, text = temp.data , font = 'Times 25')
            label4.place(x=k*55,y=680) 
            label4.config(text="%s" %temp.data,bg="white") 
            temp = temp.next
            k=k+1
    
    def insertionsortList(self,Var):
        for i in range (len(Var)):
            newNode = Node(Var[i])
            newNode.next = None 
            if (self.head == None) :
                self.head = newNode
            else:
                    temp = self.head
                    while(temp.next != None):
                            temp = temp.next
                    temp.next = newNode
        current = self.head
        if current.next == None:
            return
        else:
            while(current.next != None):
                key = current.next
                while(key != None):
                    if int(current.data) > int(key.data):
                        temp = key.data
                        key.data = current.data
                        current.data = temp
                    key = key.next
                current = current.next
        #printing----
        temp = self.head
        if(self.head==None): print("None")
        while(temp!=None):
                print(temp.data)
                temp = temp.next
        temp = self.head
        k=4
        while temp!=None:
            label5 = Label(mpr, text = temp.data, font = 'Times 25')
            label5.place(x=k*55,y=680) 
            label5.config(text="%s" %temp.data,bg="white") 
            temp = temp.next
            k=k+1


    def modifybubbleList(self,Var):   
        for i in range (len(Var)):
            newNode = Node(Var[i])
            newNode.next = None 
            if (self.head == None) :
                self.head = newNode
            else:
                    temp = self.head
                    while(temp.next != None):
                            temp = temp.next
                    temp.next = newNode
        current = self.head;  
          
        if(self.head == None):  
            return;  
        else:  
            flag = 1
            while(current.next != None and flag == 1):  
                flag = -1
                post = current.next;  
                while(post != None):   
                      if(int(current.data)> int(post.data)):
                            temp = current.data
                            current.data = post.data 
                            post.data = temp  
                            flag = 1
                      post = post.next  
                current = current.next
        temp = self.head
        if(self.head==None): print("None")
        while(temp!=None):
                i=10
                print(temp.data)
                temp = temp.next
        temp = self.head
        k=4
        while temp!=None:
            label4 = Label(mpr, text = temp.data , font = 'Times 25')
            label4.place(x=k*55,y=680) 
            label4.config(text="%s" %temp.data,bg="white") 
            temp = temp.next
            k=k+1


    def heap_sort_linked_list(self):
        # Count the number of nodes in the linked list
        count = 0
        curr = self
        while curr:
            count += 1
            curr = curr.next
        
        # Convert the linked list to an array
        arr = [0] * count
        curr = self
        for i in range(count):
            arr[i] = curr.data
            curr = curr.next
        
        # Build a max heap from the array
        for i in range(count // 2 - 1, -1, -1):
            self.heapify(arr, count, i)
        
        # Extract elements from the heap one by one
        for i in range(count - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)
        
        # Convert the sorted array back to a linked list
        curr = head
        for i in range(count):
            curr.data = arr[i]
            curr = curr.next

    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)


    def quickpartitionList(self,low,high):
       if(low==high or low==None or high==None):
           return low

       pivot = high.data
       prev = low
       curr = low
       while(low != high):
           if(low.data<pivot):
               prev = curr
               temp = curr.data
               curr.data = low.data
               low.data = temp
               curr = curr.next
           low = low.next
       temp = curr.data
       curr.data = pivot
       high.data = temp
       return prev
    
    def quicksortList(self,low,high):
        if(low==None or low==high or low==high.next):
            return
        prev = self.quickpartitionList(low,high)
        self.quicksortList(low,prev)
        if(prev==None and prev==low):
            self.quicksortList(prev.next,high)
        elif(prev != None and prev.next != None):
            self.quicksortList(prev.next.next,high)

    
    def merge_sort(self, Var):
        for i in range (len(Var)):
            newNode = Node(Var[i])
            newNode.next = None 
            if (self.head == None) :
                self.head = newNode
            else:
                    temp = self.head
                    while(temp.next != None):
                            temp = temp.next
                    temp.next = newNode

        if not self or not self.next:
            return self
        
        mid = self.get_mid(self)
        left = self
        right = mid.next
        mid.next = None
        
        left_sorted = self.merge_sort(left)
        right_sorted = self.merge_sort(right)
        
        return self.merge(left_sorted, right_sorted)
       

    def get_mid(self):
        if not self:
            return self
        
        slow = self
        fast = self.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def merge(left, right):
        temp = Node(0)
        curr = temp
        
        while left and right:
            if left.value <= right.value:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            
            curr = curr.next
        
        if left:
            curr.next = left
        elif right:
            curr.next = right
        
        return temp.next

C.pack()
mainloop()       

     
  

                


        
        


 
  
  