import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Health Disease Prediction App")
        self.geometry("1280x720")