from dataclasses import dataclass


@dataclass
class AzureConfigurationDTO:

    entityid: str
    key_file: str
    cert_file: str
    idp_metadata: str
    xmlsec_binary: str
    key_vault_url: str
    key_vault_key: str
