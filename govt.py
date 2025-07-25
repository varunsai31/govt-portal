import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser

# Translations for multiple Indian languages (extend with real translations)
translations = {
    "English": {
        "Aadhar": "Aadhar",
        "PAN Card": "PAN Card",
        "Passport": "Passport",
        "Voter ID": "Voter ID",
        "Income Tax": "Income Tax",
        "PM Kisan": "PM Kisan",
        "DigiLocker": "DigiLocker",
        "Scholarships": "Scholarships",
        "Electricity Bill": "Electricity Bill",
        "Water Bill": "Water Bill",
        "Gas Booking": "Gas Booking",
        "Driving License": "Driving License",
        "Vehicle Registration": "Vehicle Registration",
        "Rail Tickets": "Rail Tickets",
        "Health ID": "Health ID",
        "Ayushman Bharat": "Ayushman Bharat",
        "Birth Certificate": "Birth Certificate",
        "Marriage Certificate": "Marriage Certificate",
        "Land Records": "Land Records",
        "PMAY": "PMAY"
    },
    "Hindi": {
        "Aadhar": "आधार",
        "PAN Card": "पैन कार्ड",
        "Passport": "पासपोर्ट",
        "Voter ID": "वोटर आईडी",
        "Income Tax": "इनकम टैक्स",
        "PM Kisan": "पीएम किसान",
        "DigiLocker": "डिजीलॉकर",
        "Scholarships": "छात्रवृत्ति",
        "Electricity Bill": "बिजली बिल",
        "Water Bill": "पानी बिल",
        "Gas Booking": "गैस बुकिंग",
        "Driving License": "ड्राइविंग लाइसेंस",
        "Vehicle Registration": "वाहन पंजीकरण",
        "Rail Tickets": "रेल टिकट",
        "Health ID": "हेल्थ आईडी",
        "Ayushman Bharat": "आयुष्मान भारत",
        "Birth Certificate": "जन्म प्रमाणपत्र",
        "Marriage Certificate": "विवाह प्रमाणपत्र",
        "Land Records": "भूमि अभिलेख",
        "PMAY": "प्रधानमंत्री आवास योजना"
    }
    # Add more languages here...
}

services = {
    "Identity": {
        "Aadhar": "https://uidai.gov.in",
        "PAN Card": "https://www.onlineservices.nsdl.com/paam",
        "Passport": "https://www.passportindia.gov.in",
        "Voter ID": "https://www.nvsp.in"
    },
    "Finance": {
        "Income Tax": "https://www.incometax.gov.in",
        "PM Kisan": "https://pmkisan.gov.in",
        "DigiLocker": "https://www.digilocker.gov.in",
        "Scholarships": "https://scholarships.gov.in"
    },
    "Utilities": {
        "Electricity Bill": "https://www.bharatbillpay.com",
        "Water Bill": "https://www.india.gov.in/water-services",
        "Gas Booking": "https://my.ebharatgas.com"
    },
    "Transport": {
        "Driving License": "https://sarathi.parivahan.gov.in",
        "Vehicle Registration": "https://vahan.parivahan.gov.in",
        "Rail Tickets": "https://www.irctc.co.in"
    },
    "Health": {
        "Health ID": "https://healthid.ndhm.gov.in",
        "Ayushman Bharat": "https://pmjay.gov.in"
    },
    "Certificates": {
        "Birth Certificate": "https://crsorgi.gov.in",
        "Marriage Certificate": "https://india.gov.in/marriage-services"
    },
    "Land & Housing": {
        "Land Records": "https://bhulekh.gov.in",
        "PMAY": "https://pmaymis.gov.in"
    }
}

languages = list(translations.keys())
selected_lang = "English"

# Open service URL
def open_site(url):
    webbrowser.open(url)

# Build service grid
def build_grid():
    for widget in inner_frame.winfo_children():
        widget.destroy()

    query = search_var.get().lower()
    current_trans = translations.get(selected_lang, {})

    row = 0
    col = 0
    col_count = 3

    current_row = None
    for category, items in services.items():
        if col == 0:
            current_row = tk.Frame(inner_frame, bg="white")
            current_row.pack(fill='x', pady=10)

        card = tk.LabelFrame(current_row, text=category, font=("Arial", 13, 'bold'), padx=10, pady=10, bg="white")
        card.grid(row=0, column=col, padx=10, pady=5, sticky='n')

        for name, url in items.items():
            if query in name.lower() or not query:
                display_name = current_trans.get(name, name)
                btn = tk.Button(card, text=display_name, font=("Arial", 11), bg="#0078D7", fg="white",
                                command=lambda u=url: open_site(u), width=25)
                btn.pack(pady=3)

        col += 1
        if col >= col_count:
            col = 0
            row += 1

# Change language
def change_language(event=None):
    global selected_lang
    selected_lang = lang_dropdown.get()
    build_grid()

# Search filter
def search_filter(event=None):
    build_grid()

root = tk.Tk()
root.title("Bharat Sarkar Seva Portal")
root.geometry("1200x900")

# Title
title_label = tk.Label(root, text="Bharat Sarkar Seva Portal", font=("Arial", 24, "bold"), bg="#FF9933", fg="white")
title_label.pack(fill='x')

# Controls
top_controls = tk.Frame(root, bg="white")
top_controls.pack(fill='x', pady=10)

search_var = tk.StringVar()
tk.Label(top_controls, text="Search:", font=("Arial", 12), bg="white").pack(side='left', padx=(10, 5))
search_entry = tk.Entry(top_controls, textvariable=search_var, font=("Arial", 12), width=40)
search_entry.pack(side='left')
search_entry.bind("<KeyRelease>", search_filter)

tk.Label(top_controls, text="  Language:", font=("Arial", 12), bg="white").pack(side='left', padx=(20, 5))
lang_dropdown = ttk.Combobox(top_controls, values=languages, font=("Arial", 12), width=20)
lang_dropdown.set("English")
lang_dropdown.pack(side='left')
lang_dropdown.bind("<<ComboboxSelected>>", change_language)

# Scrollable area
canvas = tk.Canvas(root, bg="white")
scroll_y = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scroll_y.set)
scroll_y.pack(side='right', fill='y')
canvas.pack(side='left', fill='both', expand=True)

scrollable_frame = tk.Frame(canvas, bg="white")
canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

inner_frame = tk.Frame(scrollable_frame, bg="white")
inner_frame.pack(pady=20)

build_grid()
root.mainloop()