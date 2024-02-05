import tkinter as tk
from tkinter import filedialog
from rembg import remove
from PIL import Image

def remove_background():
    input_path = filedialog.askopenfilename(title="Select Image File")
    if input_path:
        output_path = filedialog.asksaveasfilename(title="Save Output Image As", defaultextension=".png")
        if output_path:
            input_image = Image.open(input_path)
            output_image = remove(input_image)
            output_image.save(output_path)
            print("Background removed successfully!")

root = tk.Tk()
root.title("Remove Background")
remove_button = tk.Button(root, text="Remove Background", command=remove_background)
remove_button.pack(pady=20)
root.mainloop()
