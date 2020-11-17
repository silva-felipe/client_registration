# Registration
import sqlite3
import view

from tkinter import ttk
from tkinter import *


def registro():
    def submeter():
        nome_db = nome.get()
        nascimento_db = nascimento.get()
        rg_db = rg.get()
        cpf_db = cpf.get()
        cell_db = cell.get()
        telefone_db = telefone.get()
        endereco_db = endereco.get()
        email_db = email.get()

        # conectando ao banco de dados
        conn = sqlite3.connect('clients.db')
        cursor = conn.cursor()

        # inserindo dados na tabela
        cursor.execute("""
        INSERT INTO clients (nome, nascimento, rg, cpf, cell, fone, endereco, email)
        VALUES (?,?,?,?,?,?,?,?)
        """, (nome_db, nascimento_db, rg_db, cpf_db, cell_db, telefone_db, endereco_db, email_db))

        conn.commit()

        # Close connection
        conn.close()

        # Clear entry boxes
        nome.delete(0, END)
        nascimento.delete(0, END)
        rg.delete(0, END)
        cpf.delete(0, END)
        cell.delete(0, END)
        telefone.delete(0, END)
        endereco.delete(0, END)
        email.delete(0, END)

    def visualizar():
        root.destroy()
        view.view()

    root = Tk()
    root.title('Registration')
    width_root = 420
    height_root = 350

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_coordinate = int((screen_width / 2) - (width_root / 2))
    y_coordinate = int((screen_height / 2) - (height_root / 2))

    root.geometry('{}x{}+{}+{}'.format(width_root, height_root, x_coordinate, y_coordinate))
    root.resizable(0, 0)

    # Entry box fields
    nome = Entry(root, width=35)
    nome.grid(row=1, column=1, padx=20)
    nascimento = Entry(root, width=35)
    nascimento.grid(row=2, column=1)
    rg = Entry(root, width=35)
    rg.grid(row=3, column=1)
    cpf = Entry(root, width=35)
    cpf.grid(row=4, column=1)
    cell = Entry(root, width=35)
    cell.grid(row=5, column=1)
    telefone = Entry(root, width=35)
    telefone.grid(row=6, column=1)
    endereco = Entry(root, width=35)
    endereco.grid(row=7, column=1)
    email = Entry(root, width=35)
    email.grid(row=8, column=1)

    # Fields label
    header_label = Label(root, text='Registration', font=("Times", "25", 'bold'))
    header_label.grid(row=0, column=0, columnspan=2, ipady=15)
    nome_label = Label(root, text='Full Name:', anchor='e')
    nome_label.grid(row=1, column=0, sticky='e')
    nascimento_label = Label(root, text='Date of Birth:', anchor='e')
    nascimento_label.grid(row=2, column=0, sticky='e')
    rg_label = Label(root, text='ID:', anchor='e')
    rg_label.grid(row=3, column=0, sticky='e')
    cpf_label = Label(root, text='CPF:', anchor='e')
    cpf_label.grid(row=4, column=0, sticky='e')
    cell_label = Label(root, text='Cell:', anchor='e')
    cell_label.grid(row=5, column=0, sticky='e')
    telefone_label = Label(root, text='Telephone:', anchor='e')
    telefone_label.grid(row=6, column=0, sticky='e')
    endereco_label = Label(root, text='Address:', anchor='e')
    endereco_label.grid(row=7, column=0, sticky='e')
    email_label = Label(root, text='Email:', anchor='e')
    email_label.grid(row=8, column=0, sticky='e')

    # Create submit button
    submit_btn = ttk.Button(root, text='Save', command=submeter)
    submit_btn.grid(row=9, column=1, padx=20, pady=15, sticky='e')

    # Create view button
    view_btn = ttk.Button(root, text='View', command=visualizar)
    view_btn.grid(row=9, column=1, padx=20, pady=15)

    root.mainloop()


if __name__ == '__main__':
    registro()
