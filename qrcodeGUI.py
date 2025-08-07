import qrcode
import tkinter as tk
from tkinter import messagebox

def generate_qr():
    data = entry_data.get()
    qrname = entry_name.get()

    if data.strip() == "" or qrname.strip() == "":
        messagebox.showerror("Error", "Please fill in both fields.")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    img.save(f"{qrname}.png")
    messagebox.showinfo("Done", f"✅ QR code saved as {qrname}.png")

# --- GUI Setup ---
root = tk.Tk()
root.title("QR Code Generator")

# Data input
tk.Label(root, text="Enter data or URL:").pack(pady=5)
entry_data = tk.Entry(root, width=40)
entry_data.pack(pady=5)

# Filename input
tk.Label(root, text="Enter filename (without .png):").pack(pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.pack(pady=5)

# Generate button
tk.Button(root, text="Generate QR Code", command=generate_qr).pack(pady=10)

root.mainloop()
