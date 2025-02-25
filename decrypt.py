import cv2
import os
import tkinter as tk
from tkinter import filedialog, simpledialog

def decrypt():
    filepath = filedialog.askopenfilename(title="Select Encrypted Image", filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    if not filepath:
        return
    
    img = cv2.imread(filepath)
    
    try:
        with open("key.txt", "r") as f:
            correct_password = f.read().strip()
    except FileNotFoundError:
        print("No key found!")
        return
    
    password = simpledialog.askstring("Input", "Enter passcode:", show='*')
    
    if password == correct_password:
        c = {i: chr(i) for i in range(255)}
        n, m, z = 0, 0, 0
        message = ""
        
        while True:
            try:
                message += c[img[n, m, z]]
                n += 1
                m += 1
                z = (z + 1) % 3
            except KeyError:
                break
        
        print("Decryption Message:", message)
    else:
        print("Incorrect passcode!")

if __name__ == "__main__":
    decrypt()

