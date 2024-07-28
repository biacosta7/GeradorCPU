import customtkinter as ctk
from ui import setup_ui

def main():
    root = ctk.CTk()
    root.title("Gerenciador de Planilhas")
    root.geometry("700x650")
    setup_ui(root)
    root.mainloop()

if __name__ == "__main__":
    main()