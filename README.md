# Bloch Sphere Visualization Tool

## Overview
This project is a visualization tool for single qubit rotations on a Bloch Sphere, implemented using Qiskit and Python Tkinter.

# Images:
![Home]
<img src="https://github.com/sssshish/Bloch-Sphere-Visualizer/blob/main/images/app.png" alt="App Home" style="max-width:100%; height:auto;">
<img src="https://github.com/sssshish/Bloch-Sphere-Visualizer/blob/main/images/about.png" alt="About Section" style="max-width:100%; height:auto;">
<img src="https://github.com/sssshish/Bloch-Sphere-Visualizer/blob/main/images/parametrized.png" alt="For parametrized gates (example Rx)" style="max-width:100%; height:auto;">
<img src="https://github.com/sssshish/Bloch-Sphere-Visualizer/blob/main/images/rx_visualize.png" alt="Visualizer" style="max-width:100%; height:auto;">


# Quantum Gates used: 

- **X**: Flips the state of the qubit
- **Y**: Rotates the state vector about the Y-axis
- **Z**: Flips the phase by π radians
- **Rx**: Parametrized rotation about the X-axis
- **Ry**: Parametrized rotation about the Y-axis
- **Rz**: Parametrized rotation about the Z-axis
- **S**: Rotates the state vector about the Z-axis by π/2 radians
- **T**: Rotates the state vector about the Z-axis by π/4 radians
- **Sd**: Rotates the state vector about the Z-axis by -π/2 radians
- **Td**: Rotates the state vector about the Z-axis by -π/4 radians
- **H**: Creates a state of superposition 

# Notes: 

- For Rx, Ry and Rz: The allowed range for theta (rotation_angle) in the app is [-2*π, 2*π].
- In case of a visualization error, the app closes automatically. This indicates that visualization of the given circuit is not possible.
- At a time, only 10 operations can be visualized.


## Important Links and References
- [Qiskit](https://qiskit.org/) - An open-source quantum computing framework for leveraging today's quantum processors in research, education, and business.
- [Python Tkinter](https://docs.python.org/3/library/tkinter.html) - The standard GUI toolkit for Python.
