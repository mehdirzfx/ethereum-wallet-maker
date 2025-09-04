from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes
import json

num_wallets = int(input("Enter the number of wallets to create: "))

words_num = int(input("Enter mnemonic length (12 / 15 / 24): "))
if words_num not in [12, 15, 24]:
    print("Invalid choice, defaulting to 12 words.")
    words_num = 12

wallets = []

for i in range(num_wallets):
    mnemonic = Bip39MnemonicGenerator().FromWordsNumber(words_num)
    seed = Bip39SeedGenerator(mnemonic).Generate()
    bip44_ctx = Bip44.FromSeed(seed, Bip44Coins.ETHEREUM)
    account = bip44_ctx.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)

    private_key = account.PrivateKey().Raw().ToHex()
    address = account.PublicKey().ToAddress()

    wallets.append({
        "wallet": i + 1,
        "mnemonic": mnemonic,
        "private_key": private_key,
        "address": address
    })

    print(f"Wallet {i+1}:")
    print(f"Mnemonic: {mnemonic}")
    print(f"Private Key: {private_key}")
    print(f"Address: {address}\n")

file_name = "wallets_info.json"
with open(file_name, "w") as f:
    json.dump(wallets, f, indent=4)

print(f"\n✅ Wallets information has been saved to {file_name}")
