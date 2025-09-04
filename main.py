from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes

num_wallets = int(input("Enter the number of wallets to create: "))

file_name = "wallets_info.txt"

with open(file_name, "w") as file:
    for i in range(num_wallets):
        mnemonic = Bip39MnemonicGenerator().FromWordsNumber(12)
        seed = Bip39SeedGenerator(mnemonic).Generate()
        bip44_ctx = Bip44.FromSeed(seed, Bip44Coins.ETHEREUM)
        account = bip44_ctx.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
        private_key = account.PrivateKey().Raw().ToHex()
        address = account.PublicKey().ToAddress()

        file.write(f"Wallet {i+1}:\n")
        file.write(f"SRP: {mnemonic}\n")
        file.write(f"Private Key: {private_key}\n")
        file.write(f"Address: {address}\n\n")

        print(f"Wallet {i+1}:")
        print(f"Private Key: {private_key}")
        print(f"Address: {address}\n")

print(f"\nWallets information has been saved to {file_name}")
