from tkinter import *
import os

frame1=Tk()

def frame2():
	os.system('python frame2.py')
	
######################## Images
image1 = PhotoImage(file = 'bg3.gif')
background = Label(frame1, image=image1)
background.place(x=0, y=0)
#background.image = image1
########################

######################## Window
frame1.title('Car Recommendation System')
frame1.geometry('1280x720')
windowWidth = 1058
windowHeight = 595
position_x = int(frame1.winfo_screenwidth()/2 - windowWidth/2)
position_y = int(frame1.winfo_screenheight()/2 - windowHeight/2)
frame1.geometry("+{}+{}".format(position_x, position_y))
icon=Image('photo',file='icon1.png')
frame1.tk.call('wm', 'iconphoto', frame1._w, icon)
########################

######################## Text Box
text=Text(frame1, height=6, width=26, bg='black', fg='white', font=('',14), bd=-2)
text.insert(5.0, "Under the Guidance of\nProf. Shahin Makubhai\nDEPARTMENT OF COMPUTER SCIENCE & ENGINEERING\nMIT SCHOOL of Engineering\nLoni Kalbhor Pune")
text.config(state='disabled')
text.place(x=10, y=50)
########################

######################## Buttons
exit_button = Button(frame1, text = 'EXIT', width = 6, command = frame1.destroy, fg='red', bg='#252525', font=('',30), bd=-2)
exit_button.place(x=150,y=545)

continue_button = Button(frame1, text = 'CONTINUE', width = 9, height = 1, bg='#7CFC00', fg='red', font=('',30), borderwidth=5, command=frame2)
continue_button.place(x=910,y=535)

#b1_button = Button(frame1, text = 'Developers Info', width = 12, height = 1, bg='white', fg='grey', font=('',24), borderwidth=5, command=f3)
#b1_button.place(x=970,y=85)
########################

frame1.mainloop()

