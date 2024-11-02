import hashlib, os
from argparse import ArgumentParser

def calculate_file_hash(filepath, algorithm):
    """Calculates the hash of a file using the specified algorithm.

    Args:
        filepath (str): The path to the file.
        algorithm (str): The hash algorithm to use.

    Returns:
        str: The calculated hash in hexadecimal format, or None if an error occurs.
    """
    try:
        with open(filepath, 'rb') as f:
            hash_obj = hashlib.new(algorithm)
            hash_obj.update(f.read())
            return hash_obj.hexdigest().lower()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except ValueError as e:
        if "unsupported hash type" in str(e):
            supported_algorithms = ", ".join(sorted(hashlib.algorithms_available))
            print(f"Invalid hash algorithm: {algorithm}. Supported algorithms are: {supported_algorithms}")
        else:
            raise e


def get_signature_from_file(filepath):
    """Reads the hash from a signature file.

    Args:
        filepath (str): The path to the signature file.

    Returns:
        str: The hash read from the file, or None if an error occurs.
    """
    try:
        with open(filepath, 'r') as f:
            return f.readline().strip().split()[0].lower()
    except FileNotFoundError:
        print(f"Signature file not found: {filepath}")


def main():
    parser = ArgumentParser(description="Calculate and compare file hashes.")
    parser.add_argument("file", type=str, help="Path to the file")
    parser.add_argument("signature", type=str, help="Path to the signature file")
    parser.add_argument("algorithm", type=str, help=f"Hash algorithm to use (e.g., {', '.join(sorted(hashlib.algorithms_available))})")

    args = parser.parse_args()

    file_hash = calculate_file_hash(args.file, args.algorithm)
    signature_hash = get_signature_from_file(args.signature)

    if file_hash and signature_hash:
        if file_hash == signature_hash:
            print("[✓] Hashes match.")
        else:
            print("[✕] Hashes do not match.")


if __name__ == "__main__":
    main()
