import json

from dtos.configurations.azure import AzureConfigurationDTO

from config import logger


class AzureConfiguration:
    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super(AzureConfiguration, cls).__new__(cls)
            cls._instance.config = {}
            cls._instance.load_config()
        return cls._instance

    def load_config(self):

        try:

            with open('config/azure/config.json', 'r') as file:
                self.config = json.load(file)

        except FileNotFoundError:
            logger.debug('Config file not found.')

        except json.JSONDecodeError:
            logger.debug('Error decoding config file.')

    def get_config(self):

        return AzureConfigurationDTO(
            entityid=self.config.get("entityid", ""),
            key_file=self.config.get("key_file", ""),
            cert_file=self.config.get("cert_file", ""),
            idp_metadata=self.config.get("idp_metadata", ""),
            xmlsec_binary=self.config.get("xmlsec_binary", ""),
            key_vault_url=self.config.get("key_vault_url", ""),
            key_vault_key=self.config.get("key_vault_key", "")
        )
