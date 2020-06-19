import clientV2
import tkinter
from threading import Thread
from tkinter import ttk
import rpyc
c = rpyc.connect('localhost', 1235)

lista_usuarios = []

cliente = clientV2.sender("224.1.1.1", 5007,2)
name = input("Introduzca su nombre: ")


def send(event=None):
    dest = combo.get()
    msg = my_msg.get()
    my_msg.set("") 
    cliente.sock.sendto((name +": "+msg +"+"+dest).encode(), (cliente.mcast_g, cliente.mcast_pt))
    if msg == "{quit}":
        lista_usuarios = c.root.list_clients()
        print(lista_usuarios)
        cliente.sock.close()
        top.quit()

def recv():
    while True:
        lista_usuarios = c.root.list_clients()
        combo["values"] = [elem for elem in lista_usuarios]       #update the list of active users
        try:
            recived = cliente.sock.recv(10240).decode()
            msg_list.insert(tkinter.END, recived)
        except OSError:
            break

def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    combo.set("")
    send()

top = tkinter.Tk()
top.title("CHAT")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("Type your messages here.")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=20, width=60, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
combo = ttk.Combobox(top, state="readonly")
#combo["values"] = lista_usuarios
combo.pack()

messages_frame.pack()
my_msg.set("{hi}")
send()


entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

receive_thread = Thread(target=recv)
receive_thread.daemon = True
receive_thread.start()
tkinter.mainloop()
