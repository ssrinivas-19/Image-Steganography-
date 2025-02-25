# encrypt.py
import cv2
import os
import tkinter as tk
from tkinter import filedialog, simpledialog

def encrypt():
    filepath = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    if not filepath:
        return
    
    img = cv2.imread(filepath)
    msg = simpledialog.askstring("Input", "Enter secret message:")
    password = simpledialog.askstring("Input", "Enter a passcode:", show='*')

    d = {chr(i): i for i in range(255)}

    n, m, z = 0, 0, 0
    for char in msg:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3
    
    output_path = os.path.join(os.path.dirname(filepath), "encryptedImage.png")
    cv2.imwrite(output_path, img)
    os.system(f"start {output_path}")
    
    with open("key.txt", "w") as f:
        f.write(password)
    print("Encryption Done! Image saved as 'encryptedImage.png'")

if __name__ == "__main__":
    encrypt()
