from tkinter import *
import customtkinter 
import openai
import os
import pickle


# General Settings
root = customtkinter.CTk()
root.title("ChatGPT Bot")
root.geometry("600x430")
root.iconbitmap("ai_lt.ico")

# Color Settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def speak():
    pass

def clear():
    
    my_text.delete(1.0, END)
    chat_entry.delete(0, END)

def key():
    fileName = "api_key"

    try:
        if os.path.isfile(fileName):
            input_file = open(fileName,"rb")
            # file read
            apiPassword = pickle.load(input_file)
            api_entry.insert(END, apiPassword)
        else:
            input_file = open(fileName,"wb")
            # file write
            input_file.close()
    except Exception as e:
        my_text.insert(END, f"\n\n Error!: {e}")

    root.geometry("600x600")
    api_frame.pack(pady=10)


def save_key():

    file_name = "api_key"

    try:
        output_file = open(file_name,"wb")
        pickle.dump(api_entry.get(),output_file)
        api_entry.delete(0, END)
        api_frame.pack_forget()

    except Exception as e:
        my_text.insert(END, f"\n\n Error!: {e}")

    root.geometry("600x430")

# text frame
text_frame = customtkinter.CTkFrame(root)
text_frame.pack(pady = 20)

my_text = Text(text_frame,bg="#343638",width=65,bd=1,relief="flat",wrap=WORD,selectbackground="#1f538d")
my_text.grid(row=0,column=0)

# scrollbar
text_scroll = customtkinter.CTkScrollbar(text_frame, command=my_text.yview)
text_scroll.grid(row=0,column=1,sticky="ns")

my_text.configure(yscrollcommand=text_scroll.set)

# entry
chat_entry = customtkinter.CTkEntry(root, placeholder_text="What would you like to ask gpt?",width=495,height=50,border_width=1)
chat_entry.pack(pady=10)

# button frame
button_frame = customtkinter.CTkFrame(root, fg_color="#242424")
button_frame.pack(pady=10)

# submit button
submit_button = customtkinter.CTkButton(button_frame, text="Ask gpt",command=speak)
submit_button.grid(row=0,column=0,padx=20)

# clear button
clear_button = customtkinter.CTkButton(button_frame, text="Clear answers",command=clear)
clear_button.grid(row=0,column=1,padx=20)

# api button
api_button = customtkinter.CTkButton(button_frame, text="Update api key",command=key)
api_button.grid(row=0,column=2,padx=20)

# api key frame
api_frame = customtkinter.CTkFrame(root,border_width=1)
api_frame.pack(pady=10)

api_entry = customtkinter.CTkEntry(api_frame,placeholder_text="Enter new api key",width=300,height=50,border_width=1)
api_entry.grid(row=0,column=0,padx=20,pady=20)

api_save_button = customtkinter.CTkButton(api_frame,text="Save key",command=save_key)
api_save_button.grid(row=0,column=1,padx=10)

root.mainloop()
