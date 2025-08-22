import tkinter as tk

class PhoebeGUI:
    """Minimal 2D GUI placeholder.

    Displays a circle representing Phoebe and simple text I/O fields.
    """

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Phoebe")
        self.canvas = tk.Canvas(self.root, width=200, height=200, bg="black")
        self.canvas.pack()
        self.sphere = self.canvas.create_oval(50, 50, 150, 150, fill="blue")
        self.log = tk.Text(self.root, height=10, width=40)
        self.log.pack()
        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack()

    def display_message(self, sender: str, text: str) -> None:
        self.log.insert(tk.END, f"{sender}: {text}\n")

    def run(self) -> None:
        self.root.mainloop()
