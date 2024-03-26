from tkinter import *
from tkinter import filedialog, messagebox
import os
import pyttsx3
import pdfplumber
file_path_load = []


class PDFPlayer:
    def __init__(self):
        self.engine = None

    def play_pdf(self, file_path):
        try:
            if not self.engine:
                self.engine = pyttsx3.init()
                self.engine.setProperty('rate', 150)
                self.engine.setProperty('volume', 0.9)

            with pdfplumber.open(file_path) as pdf_file:
                for page in pdf_file.pages:
                    text = page.extract_text()
                    self.engine.say(text)
                    self.engine.runAndWait()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while playing the PDF: {e}")

    def pause_pdf(self):
        try:
            if self.engine and self.engine.isBusy():
                self.engine.stop()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while pausing the PDF: {e}")


def open_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        file_path_load.append(file_path)
        # v1 = pdf.RenderPdf()
        # v2 = v1.view_pdf(root, pdf_location=file_path)
        # v2.grid(row=0, column=0, sticky="nsew")
    else:
        messagebox.showinfo("Info", "No PDF file selected.")


def read_pdf():
    if file_path_load:
        player.play_pdf(file_path_load[0])
    else:
        messagebox.showinfo("Info", "No PDF file selected.")


def pause_pdf():
    player.pause_pdf()


root = Tk()
root.title("PDF to Audiobook")
root.geometry("300x100+200+30")

player = PDFPlayer()

open_button = Button(root, text="Open PDF", command=open_pdf, bg='skyblue')
open_button.grid(row=1, column=0, padx=10, pady=10)

pause_button = Button(root, text="Pause", command=pause_pdf, bg='gray64')
pause_button.grid(row=1, column=1, padx=10, pady=10)

play_button = Button(root, text="Play", command=read_pdf, bg='seagreen')
play_button.grid(row=1, column=2, padx=10, pady=10)

quit_button = Button(root, text="Quit", command=root.destroy, bg='crimson')
quit_button.grid(row=1, column=3, padx=20, pady=50)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()