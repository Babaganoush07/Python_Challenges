from tkinter import *
from tkinter import ttk, messagebox
import datetime, re
		
def clear_all():
	first.delete(0, END)
	last.delete(0, END)
	month.delete(0, END)
	day.delete(0, END)
	year.delete(0, END)
	phone_1.delete(0, END)
	phone_2.delete(0, END)
	phone_3.delete(0, END)
	email.delete(0, END)
	username.delete(0, END)
	password.delete(0, END)

def save_new():
	check_counter = 0
	
	# Check password
	if len(password.get()) == 0:
		warning = "Password Error"
	else:
		check_counter += 1
	
	# Check Username
	if len(username.get()) == 0:
		warning = "Username Error"
	else:
		check_counter += 1
		
	# Check Email
	regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
	if(re.fullmatch(regex, email.get())):
		check_counter += 1
	else:
		warning = "Email Error"
 
	# Check for Phone Number
	if len(phone_1.get()) == 3 and len(phone_2.get()) == 3 and len(phone_3.get()) == 4:
		phone_number = phone_1.get()+"-"+phone_2.get()+"-"+phone_3.get()
		check_counter += 1
	else:
		warning = "Phone Error"
			
	# Try to convert birthday to date object
	today = datetime.date.today()
	try:
		birthday = datetime.datetime.strptime(year.get()+"/"+month.get()+"/"+day.get(), '%Y/%m/%d')
		birthday = birthday.date()
	except Exception as ep:
		warning = ep
	# Check if birthday is less than today	
	try:
		if birthday >= today:
			warning = "Date out of range"
		else:
			birthday = birthday.strftime('%Y/%m/%d')
			check_counter += 1
	except UnboundLocalError:
		pass
	
	# Check for Last Name
	if last.get() != " " and last.get().isalpha():
		check_counter += 1
	else:
		warning = "Last Name Error"
	
	# Check for First Name
	if first.get() != " " and first.get().isalpha():
		check_counter += 1
	else:
		warning = "First Name Error"
	
	if check_counter == 7:
		new_user = [
		first.get(),
		last.get(),
		birthday,
		phone_number,
		email.get(),
		username.get(),
		password.get()]
		print(new_user)
		messagebox.showinfo(" ", "Saved")
		clear_all()
	else:
		messagebox.showerror("Error", warning)
			
# Limit number entry lengths
def validate2(P):
    if len(P) == 0:
        # empty Entry is ok
        return True
    elif len(P) <= 2 and P.isdigit():
        # Entry with 2 digit is ok
        return True
    else:
        # Anything else, reject it
        return False

def validate3(P):
    if len(P) == 0:
        return True
    elif len(P) <= 3 and P.isdigit():
        return True
    else:
        return False

def validate4(P):
    if len(P) == 0:
        return True
    elif len(P) <= 4 and P.isdigit():
        return True
    else:
        return False
        
main = Tk()
main.config(bg='#AAAAAA')

# Assign comand validations
vcmd2 = (main.register(validate2), '%P')
vcmd3 = (main.register(validate3), '%P')
vcmd4 = (main.register(validate4), '%P')

title = Label(main, text='Register' , font=('ubuntu',14,'bold'), bg='#4682B4', fg='white')#00458B
title.pack(fill=X, padx=5, pady=(5, 0))

# First name label and entry box
first_name_label = Label(main, text='First Name',anchor=W, font=('ubuntu',10), bg='#AAAAAA', fg='black')
first_name_label.pack(fill=X, padx=15, pady=(5, 0))

first = Entry(main, justify=LEFT, font=('ubuntu',10))
first.pack(fill=X, padx=15)

# Last name label and entry box
last_name_label = Label(main, text='Last Name',anchor=W, font=('ubuntu',10), bg='#AAAAAA', fg='black')
last_name_label.pack(fill=X, padx=15, pady=(5, 0))

last = Entry(main, justify=LEFT, font=('ubuntu',10))
last.pack(fill=X, padx=15)

# Birthday label and frames
birthday_label = Label(main, text='Birthday',anchor=W, font=('ubuntu',10), bg='#AAAAAA', fg='black')
birthday_label.pack(fill=X, padx=15, pady=(5, 0))

birthday_frame = Frame(main, bg='#AAAAAA')
birthday_frame.pack(fill=X, padx=5)

# Month frame, with label and entry box
month_frame = Frame(birthday_frame, bg='#AAAAAA')
month_frame.pack(side=LEFT, anchor=NW, fill=X, padx=5)

month_label = Label(month_frame, text='month', font=('ubuntu',8), bg='#AAAAAA', fg='black')
month_label.pack(fill=X, expand=TRUE, padx=5)

month = Entry(month_frame, justify=CENTER, font=('ubuntu',10), width=4, validate="key", validatecommand=vcmd2)
month.pack(padx=5)

# Day frame, with label and entry box
day_frame = Frame(birthday_frame, bg='#AAAAAA')
day_frame.pack(side=LEFT, anchor=NW, fill=X, padx=5)

day_label = Label(day_frame, text='day', font=('ubuntu',8), bg='#AAAAAA', fg='black')
day_label.pack(fill=X, expand=TRUE, padx=5)

day = Entry(day_frame,justify=CENTER, font=('ubuntu',10), width=4, validate="key", validatecommand=vcmd2)
day.pack(padx=5)

# Year frame, with label and entry box
year_frame = Frame(birthday_frame, bg='#AAAAAA')
year_frame.pack(side=LEFT, anchor=NW, fill=X, padx=5)

year_label = Label(year_frame, text='year', font=('ubuntu',8), bg='#AAAAAA', fg='black')
year_label.pack(fill=X, expand=TRUE, padx=5)

year = Entry(year_frame,justify=CENTER, font=('ubuntu',10), width=6, validate="key", validatecommand=vcmd4)
year.pack(padx=5)

# Phone Number label and frames
phone_number_label = Label(main, text='Phone Number',anchor=W, font=('ubuntu',10), bg='#AAAAAA', fg='black')
phone_number_label.pack(fill=X, padx=15, pady=(5, 0))

phone_number_frame = Frame(main, bg='#AAAAAA')
phone_number_frame.pack(fill=X, padx=5)

phone_1 = Entry(phone_number_frame,justify=CENTER, font=('ubuntu',10), width=4, validate="key", validatecommand=vcmd3)
phone_1.pack(side=LEFT, padx=(15,0))

tab_1 = Label(phone_number_frame, text='-',anchor=W, font=('ubuntu',10), bg='#AAAAAA', fg='black')
tab_1.pack(side=LEFT)

phone_2 = Entry(phone_number_frame,justify=CENTER, font=('ubuntu',10), width=4, validate="key", validatecommand=vcmd3)
phone_2.pack(side=LEFT)

tab_2 = Label(phone_number_frame, text='-',anchor=W, font=('ubuntu',10), bg='#AAAAAA', fg='black')
tab_2.pack(side=LEFT)

phone_3 = Entry(phone_number_frame,justify=CENTER, font=('ubuntu',10), width=5, validate="key", validatecommand=vcmd4)
phone_3.pack(side=LEFT)

# Email name label and entry box
email_label = Label(main, text='Email Address',anchor=W, font=('ubuntu',10), bg='#AAAAAA', fg='black')
email_label.pack(fill=X, padx=15, pady=(5, 0))

email = Entry(main, justify=LEFT, font=('ubuntu',10))
email.pack(fill=X, padx=15)

# Username name label and entry box
username_label = Label(main, text='Username',anchor=W, font=('ubuntu',10), bg='#AAAAAA', fg='black')
username_label.pack(fill=X, padx=15, pady=(5, 0))

username = Entry(main, justify=LEFT, font=('ubuntu',10))
username.pack(fill=X, padx=15)

# Password label and entry box
password_label = Label(main, text='Password',anchor=W, font=('ubuntu',10), bg='#AAAAAA', fg='black')
password_label.pack(fill=X, padx=15, pady=(5, 0))

password = Entry(main, justify=LEFT, font=('ubuntu',10), show='*')
password.pack(fill=X, padx=15)

# The buttons
save_button = Button(main, text=' SAVE ', font=('ubuntu',10), bg='#4682B4', fg='white',activebackground='#ABCDEF', command=save_new)
save_button.pack(side=LEFT, anchor=N, expand=TRUE, fill=X, padx=(25,10), pady=10)

cancel_button = Button(main, text='CANCEL', font=('ubuntu',10), bg='#4682B4', fg='white',activebackground='#ABCDEF', command=clear_all)
cancel_button.pack(side=LEFT, anchor=N, expand=TRUE, fill=X, padx=(10,25), pady=10)

if (__name__ == "__main__"):
	main.mainloop()