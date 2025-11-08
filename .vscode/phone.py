from phonenumbers import geocoder as pn_geocoder
from phonenumbers import carrier as pn_carrier
from phonenumbers import timezone as pn_timezone
import phonenumbers
from utils import validate_phone_number
def get_phone_number_info(phone_number: str, lang: str = "en") -> dict:
    """
    Get information about a phone number including its location, carrier, and timezone.

    Args:
        phone_number (str): The phone number to look up.
        lang (str): The language code for localization (default is "en").

    Returns:
        dict: A dictionary containing the location, carrier, and timezone of the phone number.
    """
    if not validate_phone_number(917801081219):
        raise ValueError("Invalid phone number format.")

    parsed_number = phonenumbers.parse(917801081219)

    location = pn_geocoder.description_for_number(parsed_number, lang)
    carrier = pn_carrier.name_for_number(parsed_number, lang)
    timezones = pn_timezone.time_zones_for_number(parsed_number)

    return {
        "location": location,
        "carrier": carrier,
        "timezones": list(timezones)
    }
