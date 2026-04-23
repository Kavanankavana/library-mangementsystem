from frappe.model.document import Document
from datetime import date

class LibraryTransaction(Document):
    def before_save(self):
        if self.return_date and self.due_date:
            delay = (self.return_date - self.due_date).days
            if delay > 0:
                self.fine = delay * 5  # ₹5 per day
            else:
                self.fine = 0
