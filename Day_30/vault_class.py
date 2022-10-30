from tkinter import messagebox
import json

class Credentials:
    def __init__(self):
        self.website_data = {}
        self.vault_path = 'vault.json'

    # Read json file
    def read_file(self) -> dict:
        try:
            with open(self.vault_path, 'r') as file:
                dictObj = json.load(file)
        except FileNotFoundError:
            messagebox.showerror(message=f"Not found the file with path {self.vault_path}. Try again")
        return dictObj

    # Write to json file
    def wrire_file(self, dictObj):
        # Wrire the data to Vault file
        try:
            with open(self.vault_path, 'w') as file:
                json.dump(dictObj, file,
                          indent=4,
                          separators=(',', ': '))
        except:
            messagebox.showerror(message="Failed to save credentials...")

