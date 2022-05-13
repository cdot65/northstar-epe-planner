"""Data class for Northstar API."""
# pylint: disable=inconsistent-return-statements

# Standard library
from typing import Optional
import json
import urllib3

# Third Party
import requests

# Local
from pydantic import BaseModel

# Disable HTTPS local certificate warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Northstar(BaseModel):
    """Data class object for Northstar API."""

    baseurl: str
    headers: dict
    auth: dict
    token: Optional[str] = ""

    def create_token(self):
        """Create API token for our session."""

        try:
            response = requests.request(
                "POST",
                self.baseurl + "/oauth2/token",
                headers=self.headers,
                data=json.dumps(self.auth),
                verify=False,
            )
            response.raise_for_status()
            if response.status_code == 200:
                token_info = response.json()

                token = token_info["access_token"]
                self.token = token

                return token

        except requests.exceptions.RequestException as response_error:
            # catastrophic error
            raise SystemExit from response_error
