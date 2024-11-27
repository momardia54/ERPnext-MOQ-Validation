import frappe
from frappe import _

def validate_moq(doc, method):
    """
    Validate if all items in the document have a quantity >= MOQ.
    This function applies to all DocTypes but only acts on documents
    that have a valid 'items' child table.
    """
    # Ensure the document has an 'items' attribute
    if not hasattr(doc, "items"):
        return  # Exit if there is no 'items' attribute

    # Ensure the 'items' attribute is a valid list
    if not isinstance(doc.items, list) or not doc.items:
        return  # Exit if 'items' is not a list or is empty

    # Iterate through the items and validate MOQ
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
