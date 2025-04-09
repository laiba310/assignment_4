import tkinter as tk

cell_size = 40 
rows, cols = 10, 10  

class EraserCanvas:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=cols*cell_size, height=rows*cell_size, bg="white")
        self.canvas.pack()
        
        # Draw grid of blue rectangles
        self.rectangles = []
        for row in range(rows):
            row_rects = []
            for col in range(cols):
                x1 = col * cell_size
                y1 = row * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
                row_rects.append(rect)
            self.rectangles.append(row_rects)
        
        # Bind mouse motion to eraser function
        self.canvas.bind("<B1-Motion>", self.erase)

    def erase(self, event):
        # Size of eraser (can be adjusted)
        eraser_size = 40
        x1 = event.x - eraser_size//2
        y1 = event.y - eraser_size//2
        x2 = event.x + eraser_size//2
        y2 = event.y + eraser_size//2

        # Check which rectangles are under the eraser
        overlapping = self.canvas.find_overlapping(x1, y1, x2, y2)
        for item in overlapping:
            self.canvas.itemconfig(item, fill="white")

# Run the app
root = tk.Tk()
root.title("Eraser Canvas")
app = EraserCanvas(root)
root.mainloop()
