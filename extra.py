import tkinter as tk
from tkinter import LEFT, END, DISABLED, NORMAL
import qiskit
from qiskit import QuantumCircuit
from qiskit.visualization import visualize_transition

class BlochSphereApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Bloch Sphere')
        self.root.geometry('399x410')
        self.root.resizable(0,0) # Blocking the resizing feature

        # Colors and fonts
        self.background = '#e5e4e2'
        self.buttons = '#f0f8ff'
        self.special_buttons = '#ADDFFF'
        self.button_font = ('Arial',18)
        self.display_font = ('Arial',24)

        self.initialize_circuit()
        self.theta = 0
        self.create_widgets()

    def initialize_circuit(self):
        self.circuit = QuantumCircuit(1)

    def create_widgets(self):
        # Display Frame Layout
        self.display_frame = tk.LabelFrame(self.root)
        self.display_frame.pack()
        self.display = tk.Entry(self.display_frame, width=120, font=self.display_font, bg=self.background, borderwidth=10, justify=LEFT)
        self.display.pack(padx=3, pady=4)

        # Button Frame Layout
        self.button_frame = tk.LabelFrame(self.root, bg=self.background)
        self.button_frame.pack(fill='both', expand=True)

        self.create_buttons()

    def create_buttons(self):
        gate_buttons = [
            ('X', self.circuit.x),
            ('Y', self.circuit.y),
            ('Z', self.circuit.z),
            ('Rx', lambda: self.user_input('x')),
            ('Ry', lambda: self.user_input('y')),
            ('Rz', lambda: self.user_input('z')),
            ('S', self.circuit.s),
            ('SD', self.circuit.sdg),
            ('T', self.circuit.t),
            ('TD', self.circuit.tdg),
            ('H', self.circuit.h)
        ]

        for i, (text, command) in enumerate(gate_buttons):
            button = tk.Button(self.button_frame, text=text, font=self.button_font, bg=self.buttons, command=lambda cmd=command, txt=text: self.on_gate_click(cmd, txt), width=8)
            button.grid(row=i // 3, column=i % 3, pady=1)

        self.visualize_button = tk.Button(self.button_frame, text='Visualize', font=self.button_font, bg=self.special_buttons, command=self.visualize)
        self.visualize_button.grid(row=4, column=2, columnspan=1, sticky='WE', ipadx=8, pady=1)

        self.clear_button = tk.Button(self.button_frame, text='Clear', font=self.button_font, bg=self.special_buttons, command=self.clear)
        self.clear_button.grid(row=4, column=0, columnspan=2, sticky='WE', ipadx=5, pady=1)

        self.quit_button = tk.Button(self.button_frame, text='Quit', font=self.button_font, bg=self.special_buttons, command=self.root.destroy)
        self.quit_button.grid(row=5, column=0, columnspan=3, sticky='WE')

        self.about_button = tk.Button(self.button_frame, text='About', font=self.button_font, bg=self.special_buttons, command=self.about)
        self.about_button.grid(row=6, column=0, columnspan=3, sticky='WE')

    def on_gate_click(self, gate_func, gate_text):
        self.display_gate(gate_text)
        gate_func(0)

    def display_gate(self, gate_input):
        self.display.insert(END, gate_input)
        num_gates_pressed = len(self.display.get().replace('Rx', '').replace('Ry', '').replace('Rz', ''))
        if num_gates_pressed == 10:
            for button in self.button_frame.winfo_children():
                button.config(state=DISABLED)

    def clear(self):
        self.display.delete(0, END)
        self.initialize_circuit()
        for button in self.button_frame.winfo_children():
            button.config(state=NORMAL)

    def visualize(self):
        try:
            visualize_transition(circuit=self.circuit)
        except qiskit.visualization.exceptions.VisualizationError:
            self.root.destroy()

    def user_input(self, key):
        get_input = tk.Tk()
        get_input.title('Get Theta')
        get_input.geometry('360x160')
        get_input.resizable(0,0)
        # UI for user input here

    def about(self):
        info = tk.Tk()
        info.title('About')
        info.geometry('650x470')
        info.resizable(0,0)
        # UI for about section here

if __name__ == "__main__":
    root = tk.Tk()
    app = BlochSphereApp(root)
    root.mainloop()
