from helpers import hashes


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


def get_dat_string(file_path: str):
    with open(file_path, 'rb') as f:
        file = f.read()
        file_name = file_path.split('/').pop()
        return f"<rom name=\"{file_name}\" size=\"{hashes.get_size(file)}\" crc=\"{hashes.get_crc32(file)}\" md5=\"{hashes.get_md5(file)}\" sha1=\"{hashes.get_sha1(file)}\" />\n"
