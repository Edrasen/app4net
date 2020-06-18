import clientV2
import tkinter
from threading import Thread

cliente = clientV2.sender("224.1.1.1", 5007,2)
name = input("Introduzca su nombre: ")

def send(event=None):
    msg = my_msg.get()
    my_msg.set("") 
    cliente.sock.sendto((name +": "+msg).encode(), (cliente.mcast_g, cliente.mcast_pt))
    if msg == "{quit}":
        cliente.sock.close()
        top.quit()

def recv():
    while True:
        try:
            recived = cliente.sock.recv(10240).decode()
            msg_list.insert(tkinter.END, recived)
        except OSError:
            break

def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
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
messages_frame.pack()

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