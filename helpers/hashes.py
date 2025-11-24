import hashlib
import zlib


def get_size(file: bytes):
    return len(file)


def get_crc32(file: bytes):
    val = zlib.crc32(file)
    return hex(val)[2:]


def get_hashlib_hex(file: bytes, m: hashlib._Hash):
    m.update(file)
    return m.hexdigest()


def get_md5(file: bytes):
    m = hashlib.md5()
    return get_hashlib_hex(file, m)


def get_sha1(file: bytes):
    m = hashlib.sha1()
    return get_hashlib_hex(file, m)


def get_sha256(file: bytes):
    m = hashlib.sha256()
    return get_hashlib_hex(file, m)
