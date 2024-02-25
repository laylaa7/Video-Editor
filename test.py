import tkinter as tk
from tkinter import filedialog

def browse_file():
    filename = filedialog.askopenfilename() # Open file dialog
    if filename:  # Check if a file was selected
        print("Selected file:", filename)
        # Do something with the selected file, such as displaying its path or loading its content

# Create Tkinter window
root = tk.Tk()
root.title("File Browser")

# Create a button to browse files
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=10)

# Run Tkinter event loop
root.mainloop()
