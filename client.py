from tkinter import *
from tkinter import messagebox
from socket import *
from threading import *


host="127.0.0.1"
port=2000


def recive_messages(client,chat_entry):
    while True:
        message=client.recv(2048).decode("utf-8")
        chat_entry.delete(0, END)
        chat_entry.insert(0, message)


def send_messages(client,client_entry):
    while True:
        message = client_entry.get()
        client.send(bytes(message,"utf-8"))
        break


def start_client():
    global client 
    while True:
        recv = Thread(target=recive_messages, args=(client, chat_entry))
        recv.start()



client=socket(AF_INET,SOCK_STREAM)
client.connect((host,port))



window = Tk()
window.geometry("400x500")
window.title("Client")

lable_chat = Label(window, text="Chat", bg="green", fg="white", width=20)
lable_chat.place(x=130, y=50)

server_label = Label(window, text="server :", fg="black")
server_label.place(x=30, y=100)
chat_entry = Entry(window, width=40)
chat_entry.place(x=90, y=100)

enter_label = Label(window, text="You :", fg="black")
enter_label.place(x=30, y=150)
client_entry = Entry(window, width=40)
client_entry.place(x=90, y=150)

client_button = Button(window, text="Send", bg="green", fg="white", width=10, command=lambda: send_messages( client, client_entry))
client_button.place(x=160, y=200)


server_thread = Thread(target=start_client)
server_thread.start()


window.mainloop()