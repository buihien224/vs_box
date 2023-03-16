import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("VS Tool")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        self.main_frame =customtkinter.CTkFrame(master=self, width=270, height=550)
        self.main_frame.grid(row=0, column=0, padx=(10,5), pady=5, sticky="nsew")

        self.console_frame = customtkinter.CTkFrame(master=self)
        self.console_frame.grid(row=0, column=1, padx=(5,10), pady=5, sticky="nsew")
        
        self.console = customtkinter.CTkTextbox(master=self.console_frame)
        self.console.grid(row=0, column=0,sticky="nsew")
        



if __name__ == "__main__":
    app = App()
    app.mainloop()