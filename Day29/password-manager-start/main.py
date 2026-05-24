from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
   website = website_entry.get() # getting info from entry
   email = email_entry.get()
   password = password_entry.get()
   
   if len(website) == 0 or len(password) == 0: 
     messagebox. showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
   else : 
     is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password} \nIs it ok to save?")
     if is_ok :
        with open("data.txt","a") as data_file : 
            data_file.write(f"{website} | {email} | {password} \n") # append
            website_entry.delete(0,END) # delete entry info from 0 to End
            password_entry.delete(0,END) # delete entry info from 0 to End 



# ---------------------------- UI SETUP ------------------------------- #

window = Tk() # Window object
window.title("password Manager")
window.config(padx=20,pady=20) # add padding


canvas = Canvas( height= 200, width= 200 ) # canvas size
logo_img = PhotoImage(file = "logo.png") # load the image
canvas.create_image(100,100,image = logo_img) # loaded image on the canvas
canvas.grid(row=0,column=1) # location in Grid

#labels
website_label = Label(text= "Website:")
website_label.grid(row=1,column=0 ) # location in Grid
email_label = Label(text= "Email/Username:")
email_label.grid(row=2,column=0) # location in Grid
password_label = Label(text= "Password:")
password_label.grid(row=3,column=0) # location in Grid

#entries
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1, columnspan=2, sticky="w") # location in Grid

email_entry = Entry(width=35)
email_entry.grid(row=2,column=1, columnspan=2, sticky="w") # location in Grid
email_entry.insert(0,"abcd@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3,column=1, sticky="w") # location in Grid

#buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3,column=2)

add_button = Button(text="Add", width=36 , command=save) # calling function "save"
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()