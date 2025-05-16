import tkinter as tk
from tkinter import *
import webbrowser
from tkinter import messagebox

class ParentWindow(tk.Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master.title("Web Page Generator")
        self.master.geometry("600x150")
        self.master.resizable(False,False)

        # Add label
        label = tk.Label(root, text="Enter custom text or click the Default HTML page button", font=("Arial", 10))
        label.pack(pady=10)

        # Entry field
        self.entry = tk.Entry(self.master, width=80)
        self.entry.pack(pady=5)

        # Button frame
        button_frame = tk.Frame(self.master)
        button_frame.pack(pady=10)

         #Buttons
        self.btn = tk.Button(self.master, text="Submit Custom Text", width=25, command=self.customHTML)
        self.btn.pack(side=tk.RIGHT, padx=10)
        
        self.btn = tk.Button(self.master, text="Default HTML Page", width=25, command=self.defaultHTML)
        self.btn.pack(side=tk.RIGHT, padx=10)


    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    # Function to generate custom HTML page
    def customHTML(self):
        custom_text = self.entry.get()
        if not custom_text.strip():
            messagebox.showwarning("Warning", "Please enter some text.")
            return
        htmlFile = open("customPage.html", "w")
        htmlContent = f"<html><head><title>Custom Page</title></head><body><h1>{custom_text}</h1></body></html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("customPage.html")

                

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
