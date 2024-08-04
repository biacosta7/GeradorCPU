
# from tkinter import filedialog as fd
# from tkinter import *
# import customtkinter as ctk
# from customtkinter import *

# root = ctk.CTk()
# root.title("Top Construtora")
# root.geometry("700x650")

# # Theme e cor 
# ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
# ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# #Título 
# title_label = ctk.CTkLabel(root, text="Gerador de Planilha CPU", font=ctk.CTkFont(size=20, weight="bold"))
# title_label.pack(padx=5, pady=(40, 20))

# #Frame
# frame = ctk.CTkFrame(master=root, width=600, height=500)
# frame.pack(padx=5, pady=5)

# open_button = ctk.CTkButton(frame, text='Selecionar Tabela', command=select_sheet2, font=ctk.CTkFont(size=14))
# open_button.configure(width=450, height=30)  
# open_button.grid(column=0, row=1, padx=17, pady=(15, 10), sticky="nsew")


# # Input Códigos Label
# codigos_label = ctk.CTkLabel(frame, text="Códigos", font=ctk.CTkFont(size=13, weight="bold"))
# codigos_label.grid(row=2, column=0, padx=2, pady=2, sticky="ew")

# # Input Códigos
# codigos_entry = ctk.CTkTextbox(frame, height=100)
# codigos_entry.grid(row=3, column=0, padx=20, pady=(0,5), sticky="ew")

# # Nome da nova planilha
# # Input Name Label
# namesheet_label = ctk.CTkLabel(frame, text="Nome", font=ctk.CTkFont(size=13, weight="bold"))
# namesheet_label.grid(row=4, column=0, padx=5, pady=(0,5), sticky="ew")

# name_entry = ctk.CTkEntry(frame)
# name_entry.insert(0, "Digite o nome da planilha")
# name_entry.bind("<FocusIn>", lambda e: name_entry.delete(0, "end"))
# name_entry.grid(row=5, column=0, padx=20, pady=(0,5), sticky="ew")

# # Nome do banco
# # Input Name Label
# namebanco_label = ctk.CTkLabel(frame, text="Banco", font=ctk.CTkFont(size=13, weight="bold"))
# namebanco_label.grid(row=6, column=0, padx=5, pady=(0,5), sticky="ew")

# namebanco_entry = ctk.CTkEntry(frame)
# namebanco_entry.insert(0, "Digite o nome do banco/fonte")
# namebanco_entry.bind("<FocusIn>", lambda e: namebanco_entry.delete(0, "end"))
# namebanco_entry.grid(row=7, column=0, padx=20, pady=(0,5), sticky="ew")

# open_newsheet = ctk.CTkButton(frame, text='Abrir CPU', command=newsheet_button, font=ctk.CTkFont(size=14))
# open_button.configure(width=450, height=30)  # Set width and height directly
# open_newsheet.grid(row=10, column=0, padx=20, pady=(5, 5), sticky="ew")


# # Run Button
# run_button = ctk.CTkButton(frame, text='Executar', command=process_run, font=ctk.CTkFont(size=14))
# run_button.configure(width=450, height=30)
# run_button.grid(row=8, column=0, padx=17, pady=(30, 7), sticky="nsew")


# # Status label
# status_label = ctk.CTkLabel(frame, textvariable=status_text)
# status_label.grid(row=9, column=0, padx=20, pady=(5, 0), sticky="ew")


# # Unmatched numbers label
# unmatched_label = ctk.CTkLabel(frame, textvariable=unmatched_numbers_text, wraplength=300)
# unmatched_label.grid(row=11, column=0, padx=20, pady=(5, 5), sticky="ew")

