from tkinter import *
from PIL import Image , ImageTk
from tkinter import filedialog

# def select_folder():
#     folder_path = filedialog.askdirectory(title="Select a folder for video files")
#     if folder_path:  
#         print("Selected folder for video files:", folder_path)
#         folder_entry.delete(0, END)  
#         folder_entry.insert(0, folder_path)  

# # Create a tkinter window
# root = Tk()
# root.title("Select Folder")

# def get_text():
#     text = folder_entry.get()
#     print("Text from entry widget:", text)

# # Create a label
# label = Label(root, text="Selected Folder Path:")
# label.pack(pady=5)

# # Create an entry widget to display the selected folder path
# folder_entry = Entry(root, width=50)
# folder_entry.pack(pady=5)

# # Create a button to trigger folder selection
# select_button = Button(root, text="Select Folder", command=select_folder)
# select_button.pack(pady=5)
# button = Button(root, text="Get Text", command=get_text)
# button.pack(pady=5)

# # Keep the tkinter event loop running
# root.mainloop()
from tkinter import *

# Create a Tkinter window
window = Tk()
window.title("Entry Widget with Format")

# Define a validation function to check the format and count the number of "start-end" pairs
def validate_timepoints(text):
    # Allow empty input
    if not text:
        return True, 0
    
    # Split the text by commas
    parts = text.split(',')
    count = 0  # Initialize the count of valid pairs
    
    # Check if each part matches the format "start-end"
    for part in parts:
        # Strip leading and trailing whitespace from each part
        part = part.strip()
        
        # Split each part by the hyphen
        times = part.split('-')
        
        # Check if there are exactly two elements separated by a hyphen
        if len(times) != 2:
            return False, count
        
        # Check if both elements are integers
        if not times[0].isdigit() or not times[1].isdigit():
            return False, count
        
        # Increment the count of valid pairs
        count += 1
    
    return True, count

# Define a function to handle the "Submit" button click
def submit_timepoints():
    # Get the text from the entry widget
    text = timepoints.get()
    
    # Validate the text using the validation function
    valid, count = validate_timepoints(text)
    
    if valid:
        # If the text is valid, print it and the count of valid pairs
        print("Submitted text:", text)
        print("Number of 'start-end' pairs:", count)
        # Clear the error message
        error_label.config(text="")
    else:
        # If the text is not valid, display an error message
        error_label.config(text="Invalid format. Please use the format: start-end, start-end, ...")

# Create a label
label4 = Label(window, text="Time Points (start-end, start-end, ...) :")
label4.grid(row=3, column=0)

# Create an Entry widget
timepoints = Entry(window)
timepoints.grid(row=3, column=1)

# Create a Submit button
submit_button = Button(window, text="Submit", command=submit_timepoints)
submit_button.grid(row=4, column=0, columnspan=2, pady=5)

# Create a label to display error messages
error_label = Label(window, fg="red")
error_label.grid(row=5, column=0, columnspan=2)

# Run the Tkinter event loop
window.mainloop()
