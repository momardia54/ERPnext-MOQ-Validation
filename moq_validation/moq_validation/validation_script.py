import frappe
from frappe import _

def validate_moq(doc, method):
    """
    Validate if all items in the Quotation have a quantity >= MOQ.
    """
    for item in doc.items:
        # Fetch the item's custom MOQ value
        custom_moq = frappe.db.get_value("Item", item.item_code, "custom_moq")

        # Check if the quantity is less than the MOQ
        if custom_moq and item.qty < custom_moq:
            frappe.throw(
                _("Item {0} has a quantity ({1}) less than the MOQ ({2}).").format(
                    item.item_code, item.qty, custom_moq
                )
            )

