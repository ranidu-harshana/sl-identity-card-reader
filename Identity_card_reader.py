from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import re

window = Tk()
window.title("Identity Card Reader")
window.resizable(0,0)
dfgdf
window_width = 360
window_height = 270

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int(screen_width/2 - window_width/2)
y = int(screen_height/2 - window_height/2)

window.geometry("{}x{}+{}+{}".format(window_width,window_height,x,y))

frame = LabelFrame(window, padx=25)
frame.pack(pady=5)

flag = ImageTk.PhotoImage(Image.open("img/flag.png"))
img_label = Label(frame,image=flag)
img_label.grid(row=0,column=0,pady=10)

c_label = Label(frame, text="Software By Ranidu Harshana\n@copyright")
c_label.grid(row=0, column=1)

label = Label(frame, text="Identity Card Number")
label.grid(row=1, column=0, padx=5)

id_noE = Entry(frame, borderwidth=1, width=20)
id_noE.grid(row=1, column=1)

def genarate(counter):
	global year
	global month
	global date
	global sex

	button_counter = counter
	#if user click one more time
	"""
	if (button_counter >= 2):
		year.grid_forget()
		month.grid_forget()
		date.grid_forget()
		sex.grid_forget()
	"""
	nic = str(id_noE.get())
	print(nic)
	print(len(nic))
	#check validity of the number
	if(len(nic) == 10 or len(nic) == 12):
		day_to_int = 0
		if(len(nic) == 12):
			x = re.findall("[a-zA-Z]",nic)
			if x == []:
				year = nic[0] + nic[1] + nic[2] + nic[3]
				s = int(nic[4])
				day = nic[4] + nic[5] + nic[6]
				if(s >= 5):
					day_to_int = int(day) - 500
					sex = "Female"
				else:
					day_to_int = int(day)
					sex = "Male"
				year = Label(frame, text=year, fg="blue")
				year.grid(row=3, column=1)
			else:
				messagebox.showwarning("Warning","ID Number is not Valid")
				year = Label(frame,width=20)
				year.grid(row=3, column=1)
				month = Label(frame,width=20)
				month.grid(row=4, column=1)
				date = Label(frame,width=20)
				date.grid(row=5, column=1)
				sex = Label(frame,width=20)
				sex.grid(row=6, column=1)
		else:
			if nic[9] == 'v':
				year = nic[0] + nic[1]
				s = int(nic[2])
				day = nic[2] + nic[3] + nic[4]
				year_to_int = int(year)
				if(s >= 5):
					day_to_int = int(day) - 500
					sex = "Female"
				else:
					day_to_int = int(day)
					sex = "Male"
				year = Label(frame, text= "19" + year, fg="blue")
				year.grid(row=3, column=1)
			else:
				messagebox.showwarning("Warning","ID Number is not Valid")
				year = Label(frame,width=20)
				year.grid(row=3, column=1)
				month = Label(frame,width=20)
				month.grid(row=4, column=1)
				date = Label(frame,width=20)
				date.grid(row=5, column=1)
				sex = Label(frame,width=20)
				sex.grid(row=6, column=1)
		counter = 1
		if day_to_int != 0:
			if(day_to_int < 31):
				month = "01 - January"
				month = Label(frame, text= month, fg="blue")
				month.grid(row=4, column=1)
				date = Label(frame, text= str(day_to_int), fg="blue")
				date.grid(row=5, column=1)
			else:
				while(day_to_int > 0):
					if(counter == 1):
						if(day_to_int > 31):
							day_to_int = day_to_int - 31
							month = "02 - February"
						else:
							break
					elif(counter == 2):
						if(day_to_int > 29):
							day_to_int = day_to_int - 29
							month = "03 - March"
						else:
							break
					elif(counter == 3):
						if(day_to_int > 31):
							day_to_int = day_to_int - 31
							month = "04 - April"
						else:
							break
					elif(counter == 4):
						if(day_to_int > 30):
							day_to_int = day_to_int - 30
							month = "05 - May"
						else:
							break
					elif(counter == 5):
						if(day_to_int > 31):
							day_to_int = day_to_int - 31
							month = "06 - June"
						else:
							break
					elif(counter == 6):
						if(day_to_int > 30):
							day_to_int = day_to_int - 30
							month = "07 - July"
						else:
							break
					elif(counter == 7):
						if(day_to_int > 31):
							day_to_int = day_to_int - 31
							month = "08 - August"
						else:
							break
					elif(counter == 8):
						if(day_to_int > 31):
							day_to_int = day_to_int - 31
							month = "09 - September"
						else:
							break
					elif(counter == 9):
						if(day_to_int > 30):
							day_to_int = day_to_int - 30
							month = "10 - October"
						else:
							break
					elif(counter == 10):
						if(day_to_int > 31):
							day_to_int = day_to_int - 31
							month = "11 - November"
						else:
							break
					elif(counter == 11):
						if(day_to_int > 30):
							day_to_int = day_to_int - 30
							month = "12 - December"
						else:
							break
					elif(counter == 12):
						break
					counter = counter + 1
				month = Label(frame, text= month, fg="blue")
				month.grid(row=4, column=1)
				date = Label(frame, text= str(day_to_int), fg="blue")
				date.grid(row=5, column=1)
				sex = Label(frame, text= sex, fg="blue")
				sex.grid(row=6, column=1)

				#click the button second time
				b1 = Button(frame, text="Click Here to Find", padx=60, command=lambda:genarate(2))
				b1.grid(row=2, column=0, columnspan=2, pady=10)
	else:
		messagebox.showwarning("Warning","ID Number is Not Valid")
		year = Label(frame,width=20)
		year.grid(row=3, column=1)
		month = Label(frame,width=20)
		month.grid(row=4, column=1)
		date = Label(frame,width=20)
		date.grid(row=5, column=1)
		sex = Label(frame,width=20)
		sex.grid(row=6, column=1)
                
b1 = Button(frame, text="Click Here to Find", padx=60, command=lambda:genarate(1))
b1.grid(row=2, column=0, columnspan=2, pady=10)

label_year = Label(frame,text="Year")
label_year.grid(row=3, column=0)

label_month = Label(frame,text="Month")
label_month.grid(row=4, column=0)

label_date = Label(frame,text="Date")
label_date.grid(row=5, column=0)

label_sex = Label(frame,text="Sex")
label_sex.grid(row=6, column=0)

window.mainloop()