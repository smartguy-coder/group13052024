import random
import string

import pyotp


secret = 'kdfbjvhgdfjvjhdfhvdvfvdf'

class TimedOTPHelper:


    def generate_otp_uri(self) -> str:
        """
        Used to generate a URI for the OTP app
        based on the generate_otp_uri we can build valid QR code for Authenticator app
        """

        issuer_name = "Orderry"
        logo_url = "https://orderry.com/static/images/logo/orderry.svg"


        otp_uri = pyotp.totp.TOTP(secret).provisioning_uri(
            name='w.i.k.mailua@gmail.com',
            issuer_name=issuer_name,
        )
        # todo why direct image param in provisioning_uri broke the url?
        otp_uri_with_logo = f"{otp_uri}&image={logo_url}"
        return otp_uri_with_logo

    def is_time_otp_valid(self, otp: str) -> bool:
        """
        Check if the OTP is valid for the current time (30 seconds gap is allowed)
        """
        totp = pyotp.TOTP(secret)
        return totp.verify(otp)

    def _make_code_segment(self, length: int = 4) -> str:
        chars = string.ascii_lowercase + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    def _generate_code(self) -> str:
        segments = [self._make_code_segment() for _ in range(3)]
        code = '-'.join(segments)
        return code


    def generate_otp_for_employee(self) -> str:
        """Is used in testing functions to generate a valid OTP code for the employee"""

        totp = pyotp.TOTP(secret)
        return totp.now()

print(TimedOTPHelper().generate_otp_uri())