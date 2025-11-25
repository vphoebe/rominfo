from __future__ import annotations
import hashlib
import zlib


def get_hashes(file_path: str):
    file_name = file_path.split('/').pop()
    size = 0
    a = hashlib.sha256()
    b = hashlib.sha1()
    c = hashlib.md5()
    crc = 0
    with open(file_path, 'rb') as f:
        while (buf := f.read(1024)):
            size += len(buf)
            a.update(buf)
            b.update(buf)
            c.update(buf)
            crc = zlib.crc32(buf, crc)
        return {
            "name": file_name,
            "size": size,
            "sha256": a.hexdigest(),
            "sha1": b.hexdigest(),
            "md5": c.hexdigest(),
            "crc": hex(crc)[2:]
        }
