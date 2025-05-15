from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES



translator = Translator()

def translate_text():
    
    source_language = source_lang.get()
    target_language = target_lang.get()
    input_text = input_box.get("1.0", END).strip()

    
    if not input_text:
        messagebox.showwarning("Missing Text", "Please enter some text to translate.")
        return

    try:
        
        src_code = get_language_code(source_language)
        dest_code = get_language_code(target_language)

        
        translated = translator.translate(input_text, src=src_code, dest=dest_code)

        
        output_box.delete("1.0", END)
        output_box.insert(END, translated.text)

    except Exception as e:
        messagebox.showerror("Translation Error", f"Something went wrong:\n{e}")



def get_language_code(language_name):
    for code, name in LANGUAGES.items():
        if name.lower() == language_name.lower():
            return code
    return 'en'  



root = Tk()
root.title(" Language Translator")
root.geometry("600x600")
root.resizable(False, False)
root.configure(bg="#e6f2ff")  

Label(root, text="Language Translator", font=("Helvetica", 24, "bold"), bg="#e6f2ff", fg="#003366").pack(pady=20)

# dropdown frame
dropdown_frame = Frame(root, bg="#e6f2ff")
dropdown_frame.pack(pady=10)

# Language list sorted 
language_names = sorted(LANGUAGES.values())

# Source language 
source_lang = ttk.Combobox(dropdown_frame, values=language_names, font=("Helvetica", 12), state="readonly", width=22)
source_lang.set("english")
source_lang.grid(row=0, column=0, padx=20, pady=10)

# Target language 
target_lang = ttk.Combobox(dropdown_frame, values=language_names, font=("Helvetica", 12), state="readonly", width=22)
target_lang.set("hindi")
target_lang.grid(row=0, column=1, padx=20, pady=10)

Label(root, text="Enter text to translate:", font=("Helvetica", 14), bg="#e6f2ff").pack()
input_box = Text(root, font=("Helvetica", 12), wrap=WORD, width=60, height=6, bd=2, relief=GROOVE)
input_box.pack(pady=10)

translate_btn = Button(
    root, text="Translate", font=("Helvetica", 14, "bold"),
    bg="#4CAF50", fg="white", padx=20, pady=8, command=translate_text
)
translate_btn.pack(pady=15)

Label(root, text="Translated text:", font=("Helvetica", 14), bg="#e6f2ff").pack()
output_box = Text(root, font=("Helvetica", 12), wrap=WORD, width=60, height=6, bd=2, relief=GROOVE)
output_box.pack(pady=10)

root.mainloop()
