from operator import itemgetter


def get_file_string(hashes: dict[str, str], dat: bool):
    name, size, crc, md5, sha1, sha256 = itemgetter(
        'name', 'size', 'crc', 'md5', 'sha1', 'sha256')(hashes)
    return f"<rom name=\"{name}\" size=\"{size}\" crc=\"{crc}\" md5=\"{md5}\" sha1=\"{sha1}\" />\n" if dat else f"""--- {name} ---
Size: {size} bytes
CRC32: {crc}
MD5: {md5}
SHA-1: {sha1}
SHA-256: {sha256}
"""
