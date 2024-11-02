# 🔐 HashGard: Verify Your Files with Confidence
**HashGard** is a Python script that safeguards file integrity by comparing calculated hashes with expected values stored in signature files.

## 🎯 Key Features:
- Calculates file hashes using various algorithms.
- Compares calculated hashes with signatures for verification.
- Provides clear messages indicating hash match/mismatch. ✔️  / ❌

## 🔧 Usage:

### 1. Dependencies:
Install required libraries using requirements.txt
`pip install -r requirements.txt`

### 2. Run the Scritp, Providing Arguments:
- file: Path to the file for verification.
- signature: Path to the signature file containing the expected hash.
- algorithm: Hash algorithm to use.

#### Example:
`python hashgard.py my_file.iso my_file.sha256 sha256`

This verifies the `sha256` hash of `my_file.iso` against the hash stored in `my_file.sha256`.

Tip: Tab completion (if supported) can assist with file paths during argument input.


## ℹ️  Help Flag (-h)
Use the `-h` or `--help` flag to view usage instructions and supported arguments.

## 🖥️  Cross-Platform Compatibility
HashGard is designed to work on most operating systems that support Python (either `python` or `python3` depending on your system).

## ⚖️  License
This project is licensed under the MIT License, a permissive open-source license that allows for free commercial and non-commercial use.
