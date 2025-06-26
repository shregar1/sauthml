from utilities.saml import SAMLUtility


def get_saml_service():

    saml_utility: SAMLUtility = SAMLUtility()
    return saml_utility.get_client()
