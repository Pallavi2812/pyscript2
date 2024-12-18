import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from pyscript import Element

# Replace with your key vault URL and secret name
vault_url = "https://test-pyscript-new.vault.azure.net/"
secret_name = "test"

def fetch_secret():
    try:
        # Authenticate to Azure Key Vault
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=vault_url, credential=credential)

        # Fetch the secret value
        secret = client.get_secret(secret_name)
        return f"The value of the secret '{secret_name}' is: {secret.value}"
    except Exception as e:
        return f"An error occurred: {e}"

def display_secret(event):
    secret_value = fetch_secret()
    Element('output').write(secret_value)

