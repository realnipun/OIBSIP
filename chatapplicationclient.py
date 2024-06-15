# client.py
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                chat_window.config(state=tk.NORMAL)
                chat_window.insert(tk.END, message + "\n")
                chat_window.config(state=tk.DISABLED)
                chat_window.yview(tk.END)
        except:
            print("An error occurred!")
            client_socket.close()
            break

def send_message():
    message = message_entry.get()
    client.send(message.encode('utf-8'))
    message_entry.delete(0, tk.END)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))

root = tk.Tk()
root.title("Chat Application")

chat_window = scrolledtext.ScrolledText(root, state='disabled')
chat_window.pack(padx=10, pady=10)

message_entry = tk.Entry(root, width=50)
message_entry.pack(padx=10, pady=10)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=10)

receive_thread = threading.Thread(target=receive_messages, args=(client,))
receive_thread.start()

root.mainloop()
