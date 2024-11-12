import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

def get_secret():
    key_vault_url = "https://test-pyscript.vault.azure.net/"
    secret_name = "YourSecretName"

    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=key_vault_url, credential=credential)
    secret = client.get_secret(secret_name)

    return secret.value

if __name__ == "__main__":
    secret_value = get_secret()
    print(secret_value)
