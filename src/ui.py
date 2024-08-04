import customtkinter as ctk
from tkinter import filedialog
from data_controller import DataController
import pandas as pd

file_path = None

def setup_ui(root):

    ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
    ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
    title_label = ctk.CTkLabel(root, text="Gerador de Planilha CPU", font=ctk.CTkFont(size=20, weight="bold"))
    title_label.pack(padx=5, pady=(40, 20))

    #Frame
    frame = ctk.CTkFrame(master=root, width=600, height=500)
    frame.pack(padx=5, pady=5)

    #Load planilha
    open_button = ctk.CTkButton(frame, text='Selecionar Tabela', font=ctk.CTkFont(size=14), command=load_sheet)
    open_button.configure(width=450, height=30)  
    open_button.grid(column=0, row=1, padx=17, pady=(15, 10), sticky="nsew")

    # Input Códigos Label
    codigos_label = ctk.CTkLabel(frame, text="Códigos", font=ctk.CTkFont(size=13, weight="bold"))
    codigos_label.grid(row=2, column=0, padx=2, pady=2, sticky="ew")

    # Input Códigos
    codigos_entry = ctk.CTkTextbox(frame, height=100)
    codigos_entry.grid(row=3, column=0, padx=20, pady=(0,5), sticky="ew")

    # Nome da nova planilha
    # Input Name Label
    namesheet_label = ctk.CTkLabel(frame, text="Nome", font=ctk.CTkFont(size=13, weight="bold"))
    namesheet_label.grid(row=4, column=0, padx=5, pady=(0,5), sticky="ew")

    name_entry = ctk.CTkEntry(frame)
    name_entry.insert(0, "Digite o nome da planilha")
    name_entry.bind("<FocusIn>", lambda e: name_entry.delete(0, "end"))
    name_entry.grid(row=5, column=0, padx=20, pady=(0,5), sticky="ew")

    # Nome do banco
    # Input Name Label
    namebanco_label = ctk.CTkLabel(frame, text="Banco", font=ctk.CTkFont(size=13, weight="bold"))
    namebanco_label.grid(row=6, column=0, padx=5, pady=(0,5), sticky="ew")

    namebanco_entry = ctk.CTkEntry(frame)
    namebanco_entry.insert(0, "Digite o nome do banco/fonte")
    namebanco_entry.bind("<FocusIn>", lambda e: namebanco_entry.delete(0, "end"))
    namebanco_entry.grid(row=7, column=0, padx=20, pady=(0,5), sticky="ew")

    # Run Button
    run_button = ctk.CTkButton(frame, text='Executar', font=ctk.CTkFont(size=14))
    run_button.configure(width=450, height=30)
    run_button.grid(row=8, column=0, padx=17, pady=(30, 7), sticky="nsew")

def load_sheet():
    global file_path
    file_path = filedialog.askopenfilename() #abrir arquivo
    
    

def submit():
    if file_path:
        DataController.load_data(file_path)
        print(f"File path: {file_path}")
        # TODO - Atualizar a interface com os dados carregados
    else:
        print("Nenhum arquivo selecionado.")




def save_sheet(root):
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        # Obter dados da interface
        name = root.name_entry.get()
        codes = root.codigos_entry.get("1.0", "end-1c")
        bank = root.namebanco_entry.get()
        
        # Criar um DataFrame com os dados obtidos
        data = pd.DataFrame({
            "Nome": [name],
            "Códigos": [codes],
            "Banco": [bank]
        })

        data = pd.DataFrame()  # Placeholder for actual data
        DataController.save_data(data, file_path)