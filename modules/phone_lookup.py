import phonenumbers
from phonenumbers import geocoder, carrier

def get_phone_metadata(number):
    try:
        # Parse the number (expects format: +91XXXXXXXXXX)
        parsed_number = phonenumbers.parse(number)
        
        # Get basic info
        location = geocoder.description_for_number(parsed_number, "en")
        service_provider = carrier.name_for_number(parsed_number, "en")
        valid = phonenumbers.is_valid_number(parsed_number)
        
        return {
            "Valid": valid,
            "Location": location,
            "Carrier": service_provider,
            "International Format": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        }
    except Exception as e:
        return {"Error": str(e)}

# This can be expanded later to search specific phone-directory sites