import phonenumbers
from phonenumbers import geocoder, carrier

def get_phone_metadata(number):
    try:
        
        parsed_number = phonenumbers.parse(number)
        
        
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

