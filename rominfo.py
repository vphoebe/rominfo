import sys
import zlib
import hashlib

import helpers.hashes as hashes


def get_file_string(file_path: str):
    with open(file_path, 'rb') as f:
        file = f.read()
        file_name = file_path.split('/').pop()
        return f"""--- {file_name} ---
Size: {hashes.get_size(file)} bytes
CRC32: {hashes.get_crc32(file)}
MD5: {hashes.get_md5(file)}
SHA-1: {hashes.get_sha1(file)}
SHA-256: {hashes.get_sha256(file)}\n\n"""


def read_file_args():
    if len(sys.argv) < 2:
        print(
            "Error: No files provided.\nUsage: python rominfo.py file1.rom [file2.rom ...]")
        sys.exit(1)

    strings = []
    for file_path in sys.argv[1:]:
        try:
            string = get_file_string(file_path)
            strings.append(string)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"Error reading '{file_path}': {str(e)}")

    with open('hashes.txt', 'w') as output:
        output.write(''.join(strings))
        print(f"Wrote {len(strings)} file(s) to hashes.txt")


if __name__ == "__main__":
    sys.exit(read_file_args())
