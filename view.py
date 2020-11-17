from tkinter import *
import sqlite3
import registro
from tkinter import ttk, messagebox


# Funcao para pegar inserir na Treeview
def view():
    # Criando janela
    view_window = Tk()
    view_window.title('Records')

    width_root = 1400
    height_root = 300

    screen_width = view_window.winfo_screenwidth()
    screen_height = view_window.winfo_screenheight()

    x_coordinate = int((screen_width / 2) - (width_root / 2))
    y_coordinate = int((screen_height / 2) - (height_root / 2))

    view_window.geometry('{}x{}+{}+{}'.format(width_root, height_root, x_coordinate, y_coordinate))
    view_window.resizable(0, 0)

    # Criando LabelFrame para visualizacao
    records = LabelFrame(view_window, text='Records')
    records.pack(fill='both', expand='no', padx=10, ipadx=10)

    # Criando Treeview
    trv = ttk.Treeview(records, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), show='headings')
    trv.pack(side='left')

    # Criando scrollbar
    vsb = ttk.Scrollbar(records, orient="vertical", command=trv.yview)
    trv.configure(yscrollcommand=vsb.set)
    vsb.pack(side='right', fill='y')

    # Criando LabelFrame para update e delete
    search = LabelFrame(view_window, text='Search')
    search.pack(fill='both', expand='yes', padx=10, ipadx=10)

    # Criando Search box
    search_label = Label(search, text='ID:')
    search_label.grid(row=0, column=0)

    id_db = Entry(search, width=15)
    id_db.grid(row=0, column=1, padx=20)

    def deletar():
        # Conectando com o banco de dados
        conn = sqlite3.connect('clients.db')
        cursor = conn.cursor()

        customer_id = id_db.get()

        query = "DELETE FROM clients WHERE id =" + customer_id
        query2 = cursor.execute("SELECT nome FROM clients WHERE id = " + customer_id)
        query_nome = str(query2.fetchone())[2:-3]

        if messagebox.askyesno('Confirm Delete?', 'Are you sure you want to delete ' + query_nome + ' ?'):
            cursor.execute(query)
            id_db.delete(0, END)

            conn.commit()

            #     Close connection
            conn.close()

            view_window.destroy()
            view()
        else:
            return TRUE

        conn.commit()

        #     Close connection
        conn.close()

    def atualizar():

        def update_table():
            conn = sqlite3.connect('clients.db')
            cursor = conn.cursor()

            cursor.execute("""
            UPDATE clients SET 
            nome = ?, 
            nascimento = ?, 
            rg = ?, 
            cpf = ?, 
            cell = ?, 
            fone = ?,
            endereco = ?,
            email = ?
            WHERE id = ?
            """, (
                nome.get(), nascimento.get(), rg.get(), cpf.get(), cell.get(), telefone.get(), endereco.get(),
                email.get(),
                customer_id))

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

            update_window.destroy()
            view()

        update_window = Tk()
        update_window.title('Update Records')
        width_root = 420
        height_root = 400

        screen_width = update_window.winfo_screenwidth()
        screen_height = update_window.winfo_screenheight()

        x_coordinate = int((screen_width / 2) - (width_root / 2))
        y_coordinate = int((screen_height / 2) - (height_root / 2))

        update_window.geometry('{}x{}+{}+{}'.format(width_root, height_root, x_coordinate, y_coordinate))
        update_window.resizable(0, 0)


        nome = Entry(update_window, width=35)
        nome.grid(row=1, column=1, padx=20)
        nascimento = Entry(update_window, width=35)
        nascimento.grid(row=2, column=1)
        rg = Entry(update_window, width=35)
        rg.grid(row=3, column=1)
        cpf = Entry(update_window, width=35)
        cpf.grid(row=4, column=1)
        cell = Entry(update_window, width=35)
        cell.grid(row=5, column=1)
        telefone = Entry(update_window, width=35)
        telefone.grid(row=6, column=1)
        endereco = Entry(update_window, width=35)
        endereco.grid(row=7, column=1)
        email = Entry(update_window, width=35)
        email.grid(row=8, column=1)

        # Fields label
        header_label = Label(update_window, text='Update Record', font=("Times", "25", 'bold'))
        header_label.grid(row=0, column=0, columnspan=2, ipady=15)
        nome_label = Label(update_window, text='Full Name:', anchor='e')
        nome_label.grid(row=1, column=0, sticky='e')
        nascimento_label = Label(update_window, text='Date of Birth:', anchor='e')
        nascimento_label.grid(row=2, column=0, sticky='e')
        rg_label = Label(update_window, text='ID:', anchor='e')
        rg_label.grid(row=3, column=0, sticky='e')
        cpf_label = Label(update_window, text='CPF:', anchor='e')
        cpf_label.grid(row=4, column=0, sticky='e')
        cell_label = Label(update_window, text='Cell:', anchor='e')
        cell_label.grid(row=5, column=0, sticky='e')
        telefone_label = Label(update_window, text='Telephone:', anchor='e')
        telefone_label.grid(row=6, column=0, sticky='e')
        endereco_label = Label(update_window, text='Address:', anchor='e')
        endereco_label.grid(row=7, column=0, sticky='e')
        email_label = Label(update_window, text='Email:', anchor='e')
        email_label.grid(row=8, column=0, sticky='e')

        # Conectando com o banco de dados
        conn = sqlite3.connect('clients.db')
        cursor = conn.cursor()

        customer_id = id_db.get()

        cursor.execute("SELECT * FROM clients WHERE id =" + customer_id)

        records = cursor.fetchall()

        for record in records:
            nome.insert(0, record[1])
            nascimento.insert(0, record[2])
            rg.insert(0, record[3])
            cpf.insert(0, record[4])
            cell.insert(0, record[5])
            telefone.insert(0, record[6])
            endereco.insert(0, record[7])
            email.insert(0, record[8])

        conn.commit()

        # Close connection
        conn.close()

        # Create save button
        save_btn = ttk.Button(update_window, text='Save', command=update_table)
        save_btn.grid(row=9, column=0, columnspan=2, padx=20, pady=15)

        def back():
            update_window.destroy()
            view()


        # Create back button
        back_btn = ttk.Button(update_window, text='Back', command=back)
        back_btn.grid(row=10, column=0, columnspan=2, padx=20, pady=15)

        view_window.destroy()

        update_window.mainloop()

    # Criando botao delete
    delete_btn = ttk.Button(search, text='Delete', command=deletar)
    delete_btn.grid(row=0, column=2, padx=20, pady=15, sticky='e')

    # Criando botao update
    update_btn = ttk.Button(search, text='Update', command=atualizar)
    update_btn.grid(row=0, column=3, padx=20, pady=15, sticky='e')


    def back():
        view_window.destroy()
        registro.registro()

    # Criando botao back
    back_btn = ttk.Button(search, text='Back', command=back)
    back_btn.grid(row=0, column=4, padx=20, pady=15, sticky='e')

    # Conectando com o banco de dados
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    # lendo os dados
    cursor.execute("""
        SELECT * FROM clients;
        """)

    rows = cursor.fetchall()
    for i in rows:
        trv.insert('', 'end', values=i)

    # Pegando os Headings da tabela do Banco de dados
    nome_tabela = 'clients'

    cursor.execute('PRAGMA table_info({})'.format(nome_tabela))

    colunas = [tupla[1] for tupla in cursor.fetchall()]
    trv.heading(1, text=str(colunas[0]).upper())
    trv.heading(2, text=str(colunas[1]).upper())
    trv.heading(3, text=str(colunas[2]).upper())
    trv.heading(4, text=str(colunas[3]).upper())
    trv.heading(5, text=str(colunas[4]).upper())
    trv.heading(6, text=str(colunas[5]).upper())
    trv.heading(7, text=str(colunas[6]).upper())
    trv.heading(8, text=str(colunas[7]).upper())
    trv.heading(9, text=str(colunas[8]).upper())
    trv.column(1, width=30)
    trv.column(2, width=250)
    trv.column(3, width=105)
    trv.column(4, width=105)
    trv.column(5, width=120)
    trv.column(6, width=120)
    trv.column(7, width=120)
    trv.column(8, width=285)
    trv.column(9, width=220)

    conn.commit()

    # Close connection
    conn.close()

    view_window.mainloop()


if __name__ == '__main__':
    view()
