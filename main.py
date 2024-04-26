# Extra colors 
# Icon blue = #0098F9
# Darkest = #41B5FF, Dark = #7FCDFF, Med = #ADDFFF, Very light = #F2FAFF
# Pink = #ffb3de
# Grey = #e5e4e2
# White = #f5f5f5
# White Blue = #f0f8ff
import warnings
import numpy as np
import qiskit
from qiskit import QuantumCircuit
from qiskit.visualization import visualize_transition
import tkinter
from tkinter import LEFT, END, DISABLED, NORMAL

import qiskit.visualization

# Ignore warnings
warnings.simplefilter('ignore')

# Define Window
root = tkinter.Tk()
root.title('Bloch Sphere')

# Setting an icon
root.iconbitmap(default='logo.ico')
root.geometry('399x410')
root.resizable(0,0) # Blocking the resizing feature

# Colors and fonts
background = '#e5e4e2'
buttons = '#f0f8ff'
special_buttons = '#ADDFFF'
button_font = ('Arial',18)
display_font = ('Arial',24)

def initialize_circuit():
    global circuit
    circuit = QuantumCircuit(1)
initialize_circuit()
theta = 0

def display_gate(gate_input):
    """
    Adds a corresponding gate notation in the display to track the operations.
    If the number of operations reaches ten, all gate buttons are disabled.
    """
    
    display.insert(END,gate_input)
    input_gates = display.get()
    num_gates_pressed = len(input_gates)
    list_input_gates = list(input_gates)
    search_word = ["R","D"]
    count_double_valued_gates = [list_input_gates.count(i) for i in search_word]
    num_gates_pressed -= sum(count_double_valued_gates)
    if num_gates_pressed==10:
        gates = [x_gate,y_gate,z_gate,Rx_gate,Ry_gate,Rz_gate,s_gate,sd_gate,t_gate,td_gate,h_gate]
        for gate in gates:
            gate.config(state=DISABLED)
    
def clear(circuit):
    """
    Clears the display.
    Reinitializes the Quantum Circuit for fresh calculations.
    Check if the gate buttons are disabled, if so, then enables them
    """

    display.delete(0,END)
    initialize_circuit()    
    if x_gate['state']==DISABLED:
        gates = [x_gate,y_gate,z_gate,Rx_gate,Ry_gate,Rz_gate,s_gate,sd_gate,t_gate,td_gate,h_gate]
        for gate in gates:
            gate.config(state=NORMAL)
def visualize_circuit(circuit,window):
    """
    Visualizes the single qubit rotations corresponding to applied gates in a separate window.
    Handles any visualization error.
    """
    try:
        visualize_transition(circuit=circuit)
    except qiskit.visualization.exceptions.VisualizationError:
        window.destroy()
    
# About
def about():
    info = tkinter.Tk()
    info.title('About')
    info.geometry('650x470')
    info.resizable(0,0)
    
    text = tkinter.Text(info,height=20,width=20)
    
    label = tkinter.Label(info,text='About this Project')
    label.config(font=('Arial',14))
    text_to_display = """
    About: Visualization tool for Single Qubit Rotation on a Block Sphere.
    Made with Qiskit and Tkinter.
    
    # Quantum Gates: 
    
    X = flips the state of the qubit
    Y = rotates the state vector about Y-axis
    Z = flips the phase by PI radians
    Rx = parametrized rotation about the X-axis
    Ry = parametrized rotation about the Y-axis
    Rz = parametrized rotation about the Z-axis
    S = rotates the state vector about the Z-axis by PI/2 radians
    T = rotates the state vector about the Z-axis by PI/4 radians
    Sd = rotates the state vector about the Z-axis by -PI/2 radians
    Td = rotates the state vector about the Z-axis by -PI/4 radians
    H = creates a state of superposition 
    
    # Notes: 
    
    - For Rx, Ry and Rz, 
      The allowed range for theta(rotation_angle) in the app is [ -2*PI, 2*PI]
    
    - In case of a visualization error, the app closes automatically.
      This indicates that visualization of the given circuit is not possible. 
    
    - At a time, only 10 operations can be visualized.
    """
    
    label.pack()
    text.pack(fill='both',expand=True)
    
    text.insert(END,text_to_display)
    
    info.mainloop()
 
def change_theta(num,window,circuit,key):
    """
    Changes the global variable theta and destroys the window
    """
    
    global theta 
    theta = num*np.pi
    if key=='x':
        circuit.rx(theta,0)
        theta=0
    elif key=='y':
        circuit.ry(theta,0)
        theta=0
    else:
        circuit.rz(theta,0)
        theta=0
    window.destroy()

def user_input(circuit,key):
    """
    Taking user input for theta for Rx, Ry, Rz
    """
    
    get_input = tkinter.Tk()
    get_input.title('Get Theta')
    get_input.geometry('360x160')
    get_input.resizable(0,0)
    
    val1 = tkinter.Button(get_input, height=2, width=10, bg="#ffb3de", font=('Arial',10), text='PI/4',command=lambda:change_theta(0.25,get_input,circuit,key))
    val1.grid(row=0, column=0)
    
    val2 = tkinter.Button(get_input, height=2, width=10, bg="#ffb3de", font=('Arial',10), text='PI/2',command=lambda:change_theta(0.5,get_input,circuit,key))
    val2.grid(row=0, column=1)
    
    val3 = tkinter.Button(get_input, height=2, width=10, bg="#ffb3de", font=('Arial',10), text='PI',command=lambda:change_theta(1.0,get_input,circuit,key))
    val3.grid(row=0, column=2)
    
    val4 = tkinter.Button(get_input, height=2, width=10, bg="#ffb3de", font=('Arial',10), text='2*PI',command=lambda:change_theta(2.0,get_input,circuit,key))
    val4.grid(row=0, column=3, sticky='W')
    
    nval1 = tkinter.Button(get_input, height=2, width=10, bg="#ffb3de", font=('Arial',10), text='-PI/4',command=lambda:change_theta(-0.25,get_input,circuit,key))
    nval1.grid(row=1, column=0)
    
    nval2 = tkinter.Button(get_input, height=2, width=10, bg="#ffb3de", font=('Arial',10), text='-PI/2',command=lambda:change_theta(-0.5,get_input,circuit,key))
    nval2.grid(row=1, column=1)
    
    nval3 = tkinter.Button(get_input, height=2, width=10, bg="#ffb3de", font=('Arial',10), text='-PI',command=lambda:change_theta(-1.0,get_input,circuit,key))
    nval3.grid(row=1, column=2)
    
    nval4 = tkinter.Button(get_input, height=2, width=10, bg="#ffb3de", font=('Arial',10), text='-2*PI',command=lambda:change_theta(-2.0,get_input,circuit,key))
    nval4.grid(row=1, column=3, sticky='W')
    
    text_object = tkinter.Text(get_input, height=20, width=20, bg="#F2FAFF")
    note = """
    Give the value for theta
    Range = [-2*PI, 2*PI]
    """
    text_object.grid(sticky='WE',columnspan=4)
    text_object.insert(END,note)
    get_input.mainloop()
    
       

# Layout
# Frames
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root,bg='#F2FAFF')
display_frame.pack()
button_frame.pack(fill='both',expand=True)

# Display Frame Layout
display = tkinter.Entry(display_frame, width=120,font=display_font,bg=background, borderwidth=10,justify=LEFT)
display.pack(padx=3,pady=4)

# Button Frame Layout
x_gate = tkinter.Button(button_frame,font=button_font,bg=buttons,text='X',command=lambda:[display_gate('x'),circuit.x(0)])
y_gate = tkinter.Button(button_frame,font=button_font,bg=buttons,text='Y',command=lambda:[display_gate('y'),circuit.x(0)])
z_gate = tkinter.Button(button_frame,font=button_font,bg=buttons,text='Z',command=lambda:[display_gate('z'),circuit.x(0)])
x_gate.grid(row=0,column=0,ipadx=45,pady=1)
y_gate.grid(row=0,column=1,ipadx=45,pady=1)
z_gate.grid(row=0,column=2,ipadx=53,pady=1,sticky='E') # E = East

Rx_gate = tkinter.Button(button_frame,font=button_font,bg=buttons,text='Rx',command=lambda:[display_gate('Rx'),user_input(circuit,'x')])
Ry_gate = tkinter.Button(button_frame,font=button_font,bg=buttons,text='Ry',command=lambda:[display_gate('Ry'),user_input(circuit,'y')])
Rz_gate = tkinter.Button(button_frame,font=button_font,bg=buttons,text='Rz',command=lambda:[display_gate('Rz'),user_input(circuit,'z')])
Rx_gate.grid(row=1, column=0, columnspan=1, sticky='WE',pady=1)
Ry_gate.grid(row=1, column=1, columnspan=1, sticky='WE',pady=1)
Rz_gate.grid(row=1, column=2, columnspan=1, sticky='WE',pady=1)

s_gate = tkinter.Button(button_frame,font=button_font,bg=buttons,text='S',command=lambda:[display_gate('s'),circuit.s(0)])
sd_gate = tkinter.Button(button_frame,font=button_font,bg=buttons,text='SD',command=lambda:[display_gate('SD'),circuit.sdg(0)])
h_gate = tkinter.Button(button_frame,font=button_font,bg=buttons,text='H',command=lambda:[display_gate('H'),circuit.h(0)])
s_gate.grid(row=2, column=0, columnspan=1, sticky='WE',pady=1)
sd_gate.grid(row=2, column=1, sticky='WE',pady=1)
h_gate.grid(row=2, column=2, rowspan=2, sticky='WENS',pady=1)

t_gate = tkinter.Button(button_frame,font=button_font,bg=buttons,text='T',command=lambda:[display_gate('t'),circuit.t(0)])
td_gate = tkinter.Button(button_frame,font=button_font,bg=buttons,text='TD',command=lambda:[display_gate('TD'),circuit.tdg(0)])
t_gate.grid(row=3, column=0, sticky='WE',pady=1)
td_gate.grid(row=3, column=1, sticky='WE',pady=1)

quit = tkinter.Button(button_frame,font=button_font,bg=special_buttons,text='Quit',command=root.destroy)
visualize = tkinter.Button(button_frame,font=button_font,bg=special_buttons,text='Visualize',command=lambda:visualize_circuit(circuit,root))
quit.grid(row=6,column=0,columnspan=3,sticky='WE')

visualize.grid(row=4,column=2,columnspan=1,sticky='WE',ipadx=8,pady=1)

clear_button = tkinter.Button(button_frame,font=button_font,bg=special_buttons,text='Clear',command=lambda:clear(circuit))
clear_button.grid(row=4,column=0,columnspan=2,sticky='WE',ipadx=5,pady=1)

about_button = tkinter.Button(button_frame,font=button_font,bg=special_buttons,text='About',command=about)
about_button.grid(row=5,column=0,columnspan=3,sticky='WE')

root.mainloop()

