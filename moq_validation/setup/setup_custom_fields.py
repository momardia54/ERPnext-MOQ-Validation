import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_field

def setup_custom_fields():
    """Create the `custom_moq` field in the Item doctype and ensure it's in the form."""
    field_name = "custom_moq"
    field_label = "Minimum Order Quantity"
    
    # Define field properties
    field_properties = {
        "fieldname": field_name,
        "label": field_label,
        "fieldtype": "Int",
        "insert_after": "stock_uom",  # Adjust based on where it should appear
        "default": 1,
        "reqd": 1,
        "in_list_view": 1,
        "description": "Minimum Order Quantity for Items",
    }
    
    # Check if the field already exists
    if not frappe.db.exists("Custom Field", {"fieldname": field_name, "dt": "Item"}):
        # Create the custom field
        create_custom_field("Item", field_properties)
        frappe.msgprint(f"{field_label} has been added to the Item doctype.")

    # Add the field to the form layout
    ensure_field_in_form(field_name, field_label)


def ensure_field_in_form(fieldname, label):
    """Ensure the custom field is part of the Item form layout."""
    customize_form = frappe.get_doc("Customize Form", {"doc_type": "Item"})
    
    # Check if the field is already present in the form
    if not any(f.fieldname == fieldname for f in customize_form.fields):
        customize_form.append("fields", {
            "fieldname": fieldname,
            "label": label,
            "fieldtype": "Int",
            "insert_after": "stock_uom",
            "reqd": 1,
        })
        customize_form.save()
        frappe.msgprint(f"{label} has been added to the Item form layout.")
