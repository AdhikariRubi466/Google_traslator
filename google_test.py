from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator

root = Tk()
root.title("Smart Translator")
root.geometry("700x600")
root.config(bg="#1E1E2F")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Nepali": "ne",
    "French": "fr",
    "German": "de"
}

title = Label(root,
              text="Smart Translator",
              font=("Segoe UI", 24, "bold"),
              bg="#1E1E2F",
              fg="white")
title.pack(pady=20)

lang_frame = Frame(root, bg="#1E1E2F")
lang_frame.pack(pady=10)

Label(lang_frame, text="From:",
      font=("Segoe UI", 12),
      bg="#1E1E2F",
      fg="white").grid(row=0, column=0, padx=10)

from_lang = ttk.Combobox(lang_frame,
                         values=list(languages.keys()),
                         width=15)
from_lang.grid(row=0, column=1, padx=10)
from_lang.set("English")

Label(lang_frame, text="To:",
      font=("Segoe UI", 12),
      bg="#1E1E2F",
      fg="white").grid(row=0, column=2, padx=10)

to_lang = ttk.Combobox(lang_frame,
                       values=list(languages.keys()),
                       width=15)
to_lang.grid(row=0, column=3, padx=10)
to_lang.set("Nepali")

Label(root,
      text="Source Text",
      font=("Segoe UI", 14, "bold"),
      bg="#1E1E2F",
      fg="white").pack(anchor="w", padx=50, pady=5)

input_text = Text(root,
                  height=6,
                  font=("Segoe UI", 12))
input_text.pack(padx=50, pady=10, fill=X)

def translate_text():
    try:
        text = input_text.get("1.0", END).strip()
        if text == "":
            return

        src = languages[from_lang.get()]
        dest = languages[to_lang.get()]

        translated = GoogleTranslator(source=src, target=dest).translate(text)

        output_text.delete("1.0", END)
        output_text.insert(END, translated)

    except Exception:
        output_text.delete("1.0", END)
        output_text.insert(END, "Translation failed. Check internet connection.")

def handle_enter(event):
    if event.state & 0x0001:
        return

    translate_text()
    return "break"  

input_text.bind("<Return>", handle_enter)

translate_btn = Button(root,
                       text="Translate",
                       font=("Segoe UI", 12, "bold"),
                       bg="#6C63FF",
                       fg="white",
                       activebackground="#5848E5",
                       relief=FLAT,
                       padx=20,
                       pady=5,
                       command=translate_text)
translate_btn.pack(pady=15)

Label(root,
      text="Translated Text",
      font=("Segoe UI", 14, "bold"),
      bg="#1E1E2F",
      fg="white").pack(anchor="w", padx=50, pady=5)

output_text = Text(root,
                   height=6,
                   font=("Segoe UI", 12))
output_text.pack(padx=50, pady=10, fill=X)

root.mainloop()