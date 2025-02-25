import tkinter as tk
from encrypt import encrypt
from decrypt import decrypt

root = tk.Tk()
root.title("Image Steganography")

tk.Button(root, text="Encrypt Message", command=encrypt).pack(pady=10)
tk.Button(root, text="Decrypt Message", command=decrypt).pack(pady=10)

root.mainloop()
