import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
import Inference
import Blackboard
import DeltaVGraph

# create the main window
root = tk.Tk()
root.title("Delta V Calculator")
root.geometry("300x600")

# create a label for the title above the frame
title_label = tk.Label(root, wraplength=200, text="Enter your Delta V per stage or simply enter your total Delta V:")
title_label.pack()

# create a frame for the entries with a functinal scrollbar
frame = tk.Frame(root)
scrollbar = tk.Scrollbar(frame, orient="vertical")
entry_list = tk.Listbox(frame, yscrollcommand=scrollbar.set, justify="center")
scrollbar.config(command=entry_list.yview)
scrollbar.pack(side="right", fill="y")
entry_list.pack(side="left", fill="both", expand=True)
frame.pack(fill="both", expand=True)

# create a label for the total number of stages entered
total_label = tk.Label(root, text="Total stages: 0")
total_label.pack()

# create a label for the total amount of all values entered for the total delta v
total_amount_label = tk.Label(root, text="Total Delta V: 0")
total_amount_label.pack()

# create a label for the textbox
label = tk.Label(root, text="Enter your Delta V:")
label.pack()

# create an entry textbox to grab the input
entry = tk.Entry(root, validate="key")      # ints only
entry.config(validatecommand=(entry.register(lambda char: char.isdigit()), "%S"))
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

# create a "Add" button to add the input value to the list
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

# datatype of menu text
clicked = tk.StringVar()

nameList = Blackboard.GetNameList()

# Create Dropdown menu
drop = tk.OptionMenu( root , clicked , *nameList )
drop.pack()

# create an checkbutton to see if total deltav needs to be cut in haft 
is_checked = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Round trip", onvalue=1, offvalue=0, variable=is_checked)
checkbutton.pack()


# function to generate an array with the values in the list and pass on the checkbutton
def generate_array():
    array = []
    for i in range(entry_list.size()):
        value = int(entry_list.get(i).split(": ")[1])
        array.append(value)
    # ######################################################### change prints to return values
    print(array)
    print(is_checked.get())
    # root.quit()

# function to add the input value to the list
def DisplayGraph():
    nameList = Blackboard.GetNameList()

    nameList = {x: v.replace(' ', '\n')
            for x, v in nameList.items()}

    AvailableNodes = []
    AvailableNodesNames = {}
    color_map = []
    AvailableNodes = Inference.FindAvailableNodeFromDeltaV(AvailableNodes, 300, [4500], 0, 0, 0)

    for Nodes in AvailableNodes:
        AvailableNodesNames[Nodes] = nameList[Nodes]

    G = DeltaVGraph.GraphGivenNodes(AvailableNodes)

    color_map = ['green' if node == AvailableNodes[0] else 'blue' for node in G] 

    pos = nx.get_node_attributes(G, "pos")
    plt.figure(3,figsize=(18,9))
    nx.draw(G, pos, with_labels = True, labels=AvailableNodesNames, node_color=color_map, font_color='whitesmoke', node_size=2500, node_shape="s", font_size=10, arrowstyle="-")
    plt.show()

# create a "Graph" button to Graph the list and array
graph_button = tk.Button(root, text="Graph", command=DisplayGraph)
graph_button.pack()

# create a "Calculate" button to generate the array and start the expert system
calculate_button = tk.Button(root, text="Calculate", command=generate_array)
calculate_button.pack()

# run the main loop
root.mainloop()