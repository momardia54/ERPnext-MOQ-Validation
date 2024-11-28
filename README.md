Moq Validation

ERPNext MOQ (Minimum Order Quantity) App

This app adds Minimum Order Quantity (MOQ) functionality to ERPNext, ensuring that sales processes respect the MOQ for items.

Current Features:

Automatic Custom Field Creation:

The app now automatically creates the custom_moq field in the Item DocType during installation, eliminating the need for manual setup.
This field stores the minimum order quantity for each item and is set to mandatory with a default value of 1.

MOQ Validation:

During sales processes (e.g., Quotations, Sales Orders), if the item's quantity is less than the specified MOQ, the app displays an error message and blocks the transaction until the correct quantity is entered.
License:
AGPL-3.0
