# FridayProject6Sub
This repository contains the contents for my Friday Project 6 submission.

For the Pack File:

Class Structure: The calculator functionality is encapsulated within a CalculatorApp class.

Entry Box: Utilizes a Text widget as the entry box at the top of the GUI, which remains disabled throughout.

Button Layout: Buttons are arranged in a grid layout, with numbers first and then geometric functions below.

Button Functionality: Each button has a corresponding command that triggers an action when clicked.

Button Commands: Numbers and operations buttons call the on_button_click method, while the "=" button triggers calculation and "C" clears the entry.

Calculations: The calculate method evaluates the equation using eval but handles errors without using try and except.

Clear Entry: The clear_entry method resets the equation and clears the entry box.

Main Function: Sets up the Tkinter root window and initializes the calculator app.


For the Grid File:

Uses the grid geometry manager from Tkinter for layout.

Organizes widgets in rows and columns.

Ideal for organizing widgets in a structured grid-like layout.

Suitable for creating complex user interfaces with multiple widgets.

Requires specifying row and column indices for each widget placement.

Offers better control over widget alignment and spacing.

Widgets can span multiple rows and columns.

Well-suited for forms and tables layout.


For the Place File:

Utilizes the place geometry manager from Tkinter for layout.

Allows absolute positioning of widgets using x and y coordinates.

Useful for creating custom layouts with precise control over widget positioning.

Ideal for simple layouts or designs where exact widget placement is required.

Offers flexibility in widget placement but may require manual adjustments for different screen sizes.

Widgets are placed relative to the top-left corner of the parent container.

Well-suited for creating custom graphical interfaces or canvas-based applications.

May require careful consideration of widget placement to ensure responsiveness across different screen resolutions.