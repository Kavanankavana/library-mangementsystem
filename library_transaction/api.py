import frappe

@frappe.whitelist()
def get_books():
    return frappe.get_all("Book", fields=["name", "book_name", "status"])

@frappe.whitelist()
def issue_book(book, student):
    doc = frappe.get_doc({
        "doctype": "Library Transaction",
        "book": book,
        "student": student,
        "status": "Issued"
    })
    doc.insert()
    return "Book Issued"
