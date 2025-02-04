import customtkinter as ctk
from tkinter import filedialog

# Yeni not oluşturma fonksiyonu
def new_note():
    text_area.delete("1.0", "end")  # Metin kutusunu temizle

# Notu kaydetme fonksiyonu
def save_note():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get("1.0", "end"))  # Metin kutusundaki içeriği dosyaya kaydet

# Notu açma fonksiyonu
def open_note():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text_area.delete("1.0", "end")  # Mevcut metni temizle
            text_area.insert("1.0", file.read())  # Dosya içeriğini metin kutusuna yaz

# Arayüzü oluştur
ctk.set_appearance_mode("dark")  # Koyu mod
ctk.set_default_color_theme("blue")  # Mavi tema

app = ctk.CTk()
app.title("Notepad App")
app.geometry("600x500")

# Üst menü çubuğu
menu_bar = ctk.CTkFrame(app)
menu_bar.pack(fill="x")

new_button = ctk.CTkButton(menu_bar, text="New", command=new_note, width=80)
new_button.pack(side="left", padx=5, pady=5)

open_button = ctk.CTkButton(menu_bar, text="Open", command=open_note, width=80)
open_button.pack(side="left", padx=5, pady=5)

save_button = ctk.CTkButton(menu_bar, text="Save", command=save_note, width=80)
save_button.pack(side="left", padx=5, pady=5)

# Metin alanı
text_area = ctk.CTkTextbox(app, font=("Arial", 14), width=580, height=400)
text_area.pack(padx=10, pady=10, fill="both", expand=True)

# Copyright Bilgisi
copyright_label = ctk.CTkLabel(app, text="© 2024 Designed by Bektas", font=("Arial", 12), text_color="gray")
copyright_label.pack(pady=5)

app.mainloop()
