# Ethereum Wallet Generator

This Python script generates Ethereum wallets using BIP39 mnemonics and BIP44 derivation paths. It creates multiple wallets based on user input and saves the wallet information (mnemonic, private key, and address) to a JSON file.

## Features

- Generate multiple Ethereum wallets in one run
- Support for 12, 15, or 24-word mnemonics
- BIP39 compliant mnemonic generation
- BIP44 derivation path for Ethereum (`m/44'/60'/0'/0/0`)
- Save wallet information to JSON file
- Display wallet details in console

## Requirements

- Python 3.6+
- bip_utils library

## Installation

1. Clone this repository or download the script
2. Install the required dependency:

```bash
pip install bip_utils
```

## Usage

1. Run the script:
```bash
python wallet_generator.py
```

2. Enter the number of wallets you want to create
3. Enter the mnemonic length (12, 15, or 24 words)
4. The script will generate the wallets and display:
   - Wallet number
   - Mnemonic phrase
   - Private key (hex format)
   - Ethereum address

5. All wallet information will be saved to `wallets_info.json`

## Output Example

```
Enter the number of wallets to create: 2
Enter mnemonic length (12 / 15 / 24): 12

Wallet 1:
Mnemonic: abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about
Private Key: 0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
Address: 0x1234567890abcdef1234567890abcdef12345678

Wallet 2:
Mnemonic: ...

✅ Wallets information has been saved to wallets_info.json
```

## JSON Output Format

```json
[
    {
        "wallet": 1,
        "mnemonic": "word1 word2 word3 ...",
        "private_key": "0x...",
        "address": "0x..."
    },
    ...
]
```

## Security Notes

- 🔐 Keep your mnemonics and private keys secure and never share them
- 💾 Store the generated JSON file in a safe, offline location
- ⚠️ This tool is for educational purposes. Use at your own risk
- 🔑 Never use generated wallets for mainnet without proper security measures

## Important Warnings

- The mnemonics and private keys are displayed in the console - make sure no one is watching
- Delete the JSON file after backing up your wallets securely
- Consider using hardware wallets for storing significant amounts
- Always verify addresses before sending transactions

## License

MIT License - feel free to use and modify for your needs

## Disclaimer

This tool is provided for educational purposes only. The developers are not responsible for any loss of funds or misuse of generated wallets. Always do your own research and use proper security measures when dealing with cryptocurrency wallets.

---

**Note**: For production use, consider adding encryption to the output file and implementing additional security measures.
