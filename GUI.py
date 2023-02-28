import tkinter as tk

# create the main window
root = tk.Tk()
root.title("Delta V Calculator")
root.geometry("300x375")

# create a label for the title above the frame
title_label = tk.Label(root, wraplength=200, text="Enter your Delta V per stage or simply enter your total Delta V:")
title_label.pack()

# create a frame for the entries with a scrollbar
frame = tk.Frame(root)
scrollbar = tk.Scrollbar(frame, orient="vertical")
entry_list = tk.Listbox(frame, yscrollcommand=scrollbar.set, justify="center")
scrollbar.config(command=entry_list.yview)
scrollbar.pack(side="right", fill="y")
entry_list.pack(side="left", fill="both", expand=True)
frame.pack(fill="both", expand=True)

# create a label for the total number of values entered
total_label = tk.Label(root, text="Total stages: 0")
total_label.pack()

# create a label for the total amount of all values entered
total_amount_label = tk.Label(root, text="Total Delta V: 0")
total_amount_label.pack()

# create a label and entry widget for the input
label = tk.Label(root, text="Enter your Delta V:")
label.pack()
entry = tk.Entry(root, validate="key")
entry.config(validatecommand=(entry.register(lambda char: char.isdigit() or char == "-"), "%S"))
entry.pack()

# function to add the input value to the list
def add_entry():
    index = entry_list.size()
    value = int(entry.get())
    entry_list.insert(tk.END, f"Stage {index+1}: {value}")
    entry.delete(0, tk.END)
    total_entries = entry_list.size()
    total_label.config(text=f"Total stages: {total_entries}")
    total_amount = sum(int(entry_list.get(i).split(": ")[1]) for i in range(total_entries))
    total_amount_label.config(text=f"Total Delta V: {total_amount}")

# create a button to add the input value to the list
button = tk.Button(root, text="Add", command=add_entry)
button.pack()

# function to clear the list and array
def clear_list():
    entry_list.delete(0, tk.END)
    total_label.config(text="Total stages: 0")
    total_amount_label.config(text="Total Delta V: 0")

# create a "Clear" button to clear the list and array
clear_button = tk.Button(root, text="Clear", command=clear_list)
clear_button.pack()

# function to generate an array with the values in the list
def generate_array():
    array = []
    for i in range(entry_list.size()):
        value = int(entry_list.get(i).split(": ")[1])
        array.append(value)
    print(array)

# create an "End" button to generate the array
end_button = tk.Button(root, text="Calculate", command=generate_array)
end_button.pack()

# run the main loop
root.mainloop()