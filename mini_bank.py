import tkinter as tk
from tkinter import messagebox


class MiniBankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Bank Tizimi")
        self.root.geometry("600x500")
        self.root.configure(bg="#eaf4ff")

        self.username = ""
        self.balance = 0
        self.transactions = []

        title = tk.Label(
            root,
            text="Mini Bank Tizimi",
            font=("Arial", 20, "bold"),
            bg="#eaf4ff",
            fg="#003366"
        )
        title.pack(pady=10)

        # Foydalanuvchi ma'lumotlari
        user_frame = tk.Frame(root, bg="#eaf4ff")
        user_frame.pack(pady=10)

        tk.Label(
            user_frame,
            text="Foydalanuvchi ismi:",
            font=("Arial", 12),
            bg="#eaf4ff"
        ).grid(row=0, column=0, padx=5, pady=5)

        self.name_entry = tk.Entry(user_frame, font=("Arial", 12), width=20)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(
            user_frame,
            text="Boshlang'ich balans:",
            font=("Arial", 12),
            bg="#eaf4ff"
        ).grid(row=1, column=0, padx=5, pady=5)

        self.balance_entry = tk.Entry(user_frame, font=("Arial", 12), width=20)
        self.balance_entry.grid(row=1, column=1, padx=5, pady=5)

        create_btn = tk.Button(
            root,
            text="Hisob yaratish",
            font=("Arial", 12, "bold"),
            bg="#4caf50",
            fg="white",
            width=20,
            command=self.create_account
        )
        create_btn.pack(pady=10)

        # Amal bajarish qismi
        action_frame = tk.Frame(root, bg="#eaf4ff")
        action_frame.pack(pady=10)

        tk.Label(
            action_frame,
            text="Miqdor:",
            font=("Arial", 12),
            bg="#eaf4ff"
        ).grid(row=0, column=0, padx=5, pady=5)

        self.amount_entry = tk.Entry(action_frame, font=("Arial", 12), width=20)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5)

        deposit_btn = tk.Button(
            action_frame,
            text="Pul kirim qilish",
            font=("Arial", 11, "bold"),
            bg="#2196f3",
            fg="white",
            width=15,
            command=self.deposit_money
        )
        deposit_btn.grid(row=1, column=0, padx=5, pady=10)

        withdraw_btn = tk.Button(
            action_frame,
            text="Pul yechish",
            font=("Arial", 11, "bold"),
            bg="#f44336",
            fg="white",
            width=15,
            command=self.withdraw_money
        )
        withdraw_btn.grid(row=1, column=1, padx=5, pady=10)

        # Qoldiq
        self.balance_label = tk.Label(
            root,
            text="Qoldiq: 0 so'm",
            font=("Arial", 14, "bold"),
            bg="#eaf4ff",
            fg="#222"
        )
        self.balance_label.pack(pady=10)

        # Tarix
        tk.Label(
            root,
            text="Tranzaksiyalar tarixi",
            font=("Arial", 13, "bold"),
            bg="#eaf4ff",
            fg="#003366"
        ).pack()

        self.history_listbox = tk.Listbox(root, width=70, height=12, font=("Arial", 11))
        self.history_listbox.pack(pady=10)

    def create_account(self):
        name = self.name_entry.get().strip()
        balance_text = self.balance_entry.get().strip()

        if name == "" or balance_text == "":
            messagebox.showerror("Xatolik", "Barcha maydonlarni to'ldiring!")
            return

        try:
            balance = float(balance_text)
            if balance < 0:
                messagebox.showerror("Xatolik", "Balans manfiy bo'lishi mumkin emas!")
                return
        except:
            messagebox.showerror("Xatolik", "Balans son bo'lishi kerak!")
            return

        self.username = name
        self.balance = balance
        self.transactions.append(f"Hisob yaratildi: {self.username}, boshlang'ich balans = {self.balance} so'm")
        self.update_balance()
        self.update_history()

        messagebox.showinfo("Muvaffaqiyatli", "Hisob yaratildi!")

    def deposit_money(self):
        if self.username == "":
            messagebox.showwarning("Ogohlantirish", "Avval hisob yarating!")
            return

        amount_text = self.amount_entry.get().strip()

        try:
            amount = float(amount_text)
            if amount <= 0:
                messagebox.showerror("Xatolik", "Miqdor musbat bo'lishi kerak!")
                return
        except:
            messagebox.showerror("Xatolik", "To'g'ri miqdor kiriting!")
            return

        self.balance += amount
        self.transactions.append(f"Kirim: +{amount} so'm")
        self.update_balance()
        self.update_history()
        self.amount_entry.delete(0, tk.END)

        messagebox.showinfo("Muvaffaqiyatli", f"{amount} so'm hisobga qo'shildi.")

    def withdraw_money(self):
        if self.username == "":
            messagebox.showwarning("Ogohlantirish", "Avval hisob yarating!")
            return

        amount_text = self.amount_entry.get().strip()

        try:
            amount = float(amount_text)
            if amount <= 0:
                messagebox.showerror("Xatolik", "Miqdor musbat bo'lishi kerak!")
                return
        except:
            messagebox.showerror("Xatolik", "To'g'ri miqdor kiriting!")
            return

        if amount > self.balance:
            messagebox.showerror("Xatolik", "Hisobda yetarli mablag' yo'q!")
            return

        self.balance -= amount
        self.transactions.append(f"Chiqim: -{amount} so'm")
        self.update_balance()
        self.update_history()
        self.amount_entry.delete(0, tk.END)

        messagebox.showinfo("Muvaffaqiyatli", f"{amount} so'm yechildi.")

    def update_balance(self):
        self.balance_label.config(text=f"Qoldiq: {self.balance} so'm")

    def update_history(self):
        self.history_listbox.delete(0, tk.END)
        for item in self.transactions:
            self.history_listbox.insert(tk.END, item)


root = tk.Tk()
app = MiniBankApp(root)
root.mainloop()