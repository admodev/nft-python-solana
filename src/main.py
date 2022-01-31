import base58
import json
import os
import metaplex_api
from cryptography.fernet import Fernet

# Mint NFT
SERVER_DECRYPTION_KEY = Fernet.generate_key().decode("ascii")
TEST_PRIVATE_KEY = os.environ['TEST_PRIVATE_KEY']
TEST_PUBLIC_KEY = "MsE5TofYuKtxgboqwzbLxjFbaNwK41b3YYfX6gyxfcD"
cfg = {
    "PRIVATE_KEY": TEST_PRIVATE_KEY,
    "PUBLIC_KEY": TEST_PUBLIC_KEY,
    "DECRYPTION_KEY": SERVER_DECRYPTION_KEY
}
api = metaplex_api.MetaplexAPI(cfg)
account = metaplex_api.Account(list(base58.b58decode(cfg["PRIVATE_KEY"]))[:32])
api_endpoint = "https://api.devnet.solana.com/"
