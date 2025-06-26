from saml2 import BINDING_HTTP_POST, BINDING_HTTP_REDIRECT
from saml2.client import Saml2Client
from saml2.config import Config as Saml2Config

from abstractions.utility import IUtility

from config import logger, azure_configuration


class SAMLUtility(IUtility):

    def __init__(self, urn: str = None) -> None:

        super().__init__(urn)
        self.urn = urn
        self.logger = logger

    def get_client(self):

        settings = {
            "entityid": azure_configuration.entityid,
            "metadata": {
                "local": ["idp_metadata.xml"],
            },
            "service": {
                "sp": {
                    "endpoints": {
                        "assertion_consumer_service": [
                            (
                                "http://localhost:8000/api/saml/callback",
                                BINDING_HTTP_POST
                            ),
                        ],
                        "single_logout_service": [
                            (
                                "http://localhost:8000/api/saml/logout",
                                BINDING_HTTP_REDIRECT
                            ),
                        ],
                    },
                    "required_attributes": ["displayName", "mail"],
                    "allow_unsolicited": True,
                    "authn_requests_signed": False,
                    "logout_requests_signed": False,
                    "want_assertions_signed": True,
                    "want_response_signed": False,
                },
            },

            "key_file": azure_configuration.key_file,
            "cert_file": azure_configuration.cert_file,
            "xmlsec_binary": azure_configuration.xmlsec_binary,
        }

        sp_config = Saml2Config()
        sp_config.load(settings)
        sp_config.allow_unknown_attributes = True

        return Saml2Client(config=sp_config)
