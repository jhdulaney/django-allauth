
from ..utils import email_address_exists
from ..account.utils import user_email


def existing_email(user):
    """
    Check to see if the social account user's email already exists.
    """
    email = user_email(user)
    if email:
        if email_address_exists(email):
            return True
    return False
