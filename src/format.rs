use crate::hashes::RomInfo;

pub fn format_data(data: &RomInfo, is_dat: bool) -> String {
    match is_dat {
        false => format!(
            "--- {} ---\nSize: {} bytes\nCRC32: {}\nMD5: {}\nSHA-1: {}\nSHA-256: {}\n",
            data.filename, data.size, data.crc32, data.md5, data.sha1, data.sha256
        ),
        true => format!(
            "<rom name=\"{}\" size=\"{}\" crc=\"{}\" md5=\"{}\" sha1=\"{}\" />",
            data.filename, data.size, data.crc32, data.md5, data.sha1
        ),
    }
}
