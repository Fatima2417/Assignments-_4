#importing libraries
import tkinter as tk
import time

# Set canvas dimensions
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

# Set grid cell size and eraser size
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    """Erase objects in contact with the eraser"""

    # Get the current mouse position relative to the canvas
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    
    # Calculate the coordinates of the eraser's area
    left_x = mouse_x - ERASER_SIZE // 2
    top_y = mouse_y - ERASER_SIZE // 2
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    # Find all objects on the canvas that overlap with the eraser's area
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    # Change the color of the overlapping objects to 'white' (erase them)
    for overlapping_object in overlapping_objects:
        canvas.itemconfig(overlapping_object, fill='white')

def main():
    # Initialize the tkinter window and canvas
    root = tk.Tk()
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)

    canvas.pack()

    # Calculate the number of rows and columns based on cell size
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE

    cells = []
    


    # Create a grid of blue cells
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            
            # Draw each cell as a rectangle on the canvas
            cell = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill='blue')
            cells.append(cell)
    # Function to handle mouse click and create the eraser
    def on_click(event):
        last_click_x, last_click_y = event.x, event.y
        
        # Create the eraser at the click position
        eraser = canvas.create_rectangle(
            last_click_x - ERASER_SIZE // 2,
            last_click_y - ERASER_SIZE // 2,
            last_click_x + ERASER_SIZE // 2,
            last_click_y + ERASER_SIZE // 2,
            fill='pink'
        )

        # Function to move the eraser with the mouse and erase overlapping cells
        def move_eraser(event):
            mouse_x, mouse_y = event.x, event.y
            # Move the eraser rectangle to the mouse position
            canvas.moveto(eraser, mouse_x - ERASER_SIZE // 2, mouse_y - ERASER_SIZE // 2)
            # Call erase_objects function to erase any cells that overlap with the eraser
            erase_objects(canvas, eraser)
        
        # Bind the mouse motion event to move the eraser
        canvas.bind("<Motion>", move_eraser)

    # Wait for a click to place the eraser
    canvas.bind("<Button-1>", on_click)

    # Run the tkinter event loop
    root.mainloop()

if __name__ == '__main__':
    main()
