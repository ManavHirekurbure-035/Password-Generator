import tkinter as tk
import random

root = tk.Tk()
root.title("Password Generator")
root.geometry("500x500")
root.resizable(False, False)
root.configure(bg = "#373737")

password_label = None


def generate_password() :
    global password_label

    char_list=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '`', '~']

    if password_label:        
        password_label.grid_forget() 

    password=""

    size = entry.get()
    if size.isdigit() :
        size = int(size)
        if(size > 0) :
            for i in range(size) :
                password = password + random.choice(char_list)            
            
            tk.Label(root , text = "", bg="#373737").grid(row = 3, column = 0, columnspan = 4, pady = 10)
            tk.Label(
                root,
                text = "Your Password is ", 
                pady = 5, 
                padx = 5, 
                font = ("Comic Sans MS", 16), 
                fg = "#FFFFFF", 
                bg="#373737"
                ).grid(row = 4, column = 0, columnspan = 4, padx = 20)  
     
            password_label = tk.Label(
                root,
                text = password, 
                pady = 5, 
                padx = 5, 
                font = ("Ariel", 24), 
                fg = "#F2AD10", 
                bg="#373737"
                )
            password_label.grid(row = 5, column = 0, columnspan = 4, padx = 20)  
    
    

        
    


# Page heading 
tk.Label(
    root,
    text = "Generate Unique Password", 
    pady = 15, 
    padx = 15, 
    font = "Ariel 20 bold",
    fg = "#373737", 
    bg="#F2AD10"
    ).grid(row = 0, column = 0, columnspan = 4, padx = 55, pady = 30)


# Ask for number of characters in the Password
tk.Label(
    root,
    text = "Enter number of characters", 
    pady = 5, 
    padx = 5, 
    font = ("Comic Sans MS", 16), 
    fg = "#FFFFFF", 
    bg="#373737"
    ).grid(row = 1, column = 0, columnspan = 2, padx = 20, pady = 40)

# Take input size of Password
entry = tk.Entry(
    root, 
    width = 10, 
    font = ("Comic Sans MS", 16), 
    justify = tk.CENTER
    )
entry.focus_set()
entry.grid(row = 1, column = 2, columnspan = 2)

# Button to create random Password
tk.Button(
    root, 
    text = "Generate", 
    padx = 5, 
    font = ("Comic Sans MS", 16), 
    bg = "#F2AD10", 
    activebackground = "#7D5C10",     
    cursor = "hand2",
    command = generate_password
    ).grid(row = 2, column = 0,columnspan = 4)





root.mainloop()
