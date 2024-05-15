import tkinter as tk
import main
import pandas as pd
import misc
import static

headers = static.PropertyHeaders()

entry_rows = 20

date = "5-7-2024"

def main_function(entries, master_csv_chk, master_csv_name):
    
    li = []

    for entry in entries:
        url = entry["url"].get()
        csv_file_name = entry["text"].get()
        if url and csv_file_name:
            print(f"URL: {url}, CSV File Name: {csv_file_name}")
            csv_path = main.main(url, csv_file_name)

            df = pd.read_csv(csv_path, index_col=None, header=0)
            li.append(df)


    if master_csv_chk and len(li) > 1:
        print(misc.replace_after_last_slash(csv_path, f"{master_csv_name}.csv"))
        frame = pd.concat(li, axis=0, ignore_index=True)
        frame.to_csv(misc.replace_after_last_slash(csv_path, f"{master_csv_name}.csv"), index=False)

        frame_unique = frame.drop_duplicates(subset=[headers.tax_account_id_number, headers.legal_description, headers.address], keep='first')
        frame_unique.to_csv(misc.replace_after_last_slash(csv_path, f"Unique {master_csv_name}.csv"))

# Create the main window
root = tk.Tk()
root.title("URL and Text Entry")

# List to store entries
entries = []

# Default CSV file names
default_csv_names = [
    f"Brazoria Pre-Foreclosure {date}", f"Chamber Pre-Foreclosure {date}",
    f"Fort Bend Pre-Foreclosure {date}", f"Galveston Pre-Foreclosure {date}",
    f"Harris NE Pre-Foreclosure {date}", f"Harris NW Pre-Foreclosure {date}",
    f"Harris SE Pre-Foreclosure {date}", f"Harris SW Pre-Foreclosure {date}",
    f"Harris UK Pre-Foreclosure {date}", f"Montgomery Pre-Foreclosure {date}",

    f"Jefferson Pre-Foreclosure {date}", f"Liberty Pre-Foreclosure {date}",
    f"Pre-Foreclosure {date}", f"Pre-Foreclosure {date}",
    f"Pre-Foreclosure {date}", f"Pre-Foreclosure {date}",
    f"Pre-Foreclosure {date}", f"Pre-Foreclosure {date}",
    f"Pre-Foreclosure {date}", f"Pre-Foreclosure {date}"
]

# Create ten sets of URL and text entries
for i in range(entry_rows):
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=5, anchor='w')

    url_label = tk.Label(frame, text=f"URL {i+1}:")
    url_label.pack(side=tk.LEFT)
    url_entry = tk.Entry(frame, width=50)
    url_entry.pack(side=tk.LEFT)

    text_label = tk.Label(frame, text=f"CSV File Name {i+1}:")
    text_label.pack(side=tk.LEFT)
    text_entry = tk.Entry(frame, width=50)
    text_entry.insert(0, default_csv_names[i])  # Insert default CSV file name
    text_entry.pack(side=tk.LEFT)

    entries.append({"url": url_entry, "text": text_entry})

master_csv_chk_var = tk.BooleanVar()
master_csv_chk_var.set(True)

def toggle_entry_state(entry, var):
    if not var.get():
        entry.config(state="disabled")
        print("disabled")
    else:
        entry.config(state="normal")
        print("enabled")

                                                                                                                      
master_csv_chk = tk.Checkbutton(root, text="Create Master CSV", variable=master_csv_chk_var, command=lambda: toggle_entry_state(master_csv_entry, master_csv_chk_var))
master_csv_chk.pack(side=tk.LEFT)
master_csv_entry = tk.Entry(root, width=50)
master_csv_entry.pack(padx=entry_rows+1, side=tk.LEFT)
master_csv_entry.insert(0, f"Master Pre-Forclosure {date}")
master_csv_entry.pack(side=tk.LEFT)
\



# Button to process the entries
process_button = tk.Button(root, text="Process Entries", command=lambda: main_function(entries, master_csv_chk_var.get(), master_csv_entry.get()))
process_button.pack(padx=12)

# Start the GUI loop
root.mainloop()
