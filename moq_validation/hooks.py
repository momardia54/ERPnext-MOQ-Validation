app_name = "moq_validation"
app_title = "Moq Validation"
app_publisher = "Momar Dia	"
app_description = "Validata the minimum order quantity for any item added to a sale process"
app_email = "momar@boostwaydigital.com"
app_license = "agpl-3.0"

# Apps
# ------------------
# create the required fields in the database and add them to the form
after_install = "moq_validation.setup.setup_custom_fields.setup_custom_fields"

# run the script for all doctypes before save. PS: Script is designed to know which doctype to ignore
doc_events = {
    "*": {
        "before_save": "moq_validation.moq_validation.validation_script.validate_moq",
    }
}





