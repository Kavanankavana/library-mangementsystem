from frappe.model.document import Document
from datetime import datetime

class LibraryTransaction(Document):

    def before_save(self):
        self.calculate_fine()

    def on_submit(self):
        # When book is issued
        if self.status == "Issued":
            frappe.db.set_value("Book", self.book, "status", "Issued")

    def on_cancel(self):
        # When transaction is cancelled / returned
        frappe.db.set_value("Book", self.book, "status", "Available")

    def calculate_fine(self):
        if self.return_date and self.due_date:
            due = datetime.strptime(str(self.due_date), "%Y-%m-%d")
            ret = datetime.strptime(str(self.return_date), "%Y-%m-%d")

            delay = (ret - due).days

            if delay > 0:
                self.fine = delay * 10  # ₹10 per day
            else:
                self.fine = 0
