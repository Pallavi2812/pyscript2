import subprocess
import sys

# Function to install packages
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install required packages
install("azure-identity")
install("azure-keyvault-secrets")

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

vault_url = "https://test-pyscript-new.vault.azure.net/"
secret_name = "test"

# Authenticate to Azure Key Vault
credential = DefaultAzureCredential()
client = SecretClient(vault_url=vault_url, credential=credential)

# Fetch the secret value
secret = client.get_secret(secret_name)
print(f"The value of the secret '{secret_name}' is: {secret.value}")
