## Moq Validation

ERPNext MOQ (Minimum Order Quantity) App

This ERPNext app introduces the Minimum Order Quantity (MOQ) functionality to ensure sales processes respect the minimum quantity requirements for items.

Current Features

Manual Setup Required:

You need to manually add a custom field named custom_moq in the Item DocType for the app to function correctly.
This field should store the minimum order quantity for each item.


MOQ Validation:

During sales processes (e.g., Quotations, Sales Orders), if an item's quantity is less than the specified MOQ, the app will display an error message and block the transaction until the correct quantity is entered.


Planned Updates

In future versions, the app will automatically create the custom_moq field during installation, simplifying the setup process.



#### License

agpl-3.0
