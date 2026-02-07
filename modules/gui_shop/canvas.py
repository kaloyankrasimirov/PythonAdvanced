import tkinter as tk


def create_app():
    root = tk.Tk()
    root.title("GUI Shop")
    root.geometry("1200x900+700+100")
    return root

app = create_app()