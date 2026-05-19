use md5::{Digest, Md5};
use sha1::Sha1;
use sha2::Sha256;
use std::path::Path;

use crate::file::read_buf;

pub struct RomInfo {
    pub filename: String,
    pub md5: String,
    pub sha1: String,
    pub sha256: String,
    pub crc32: String,
    pub size: usize,
}

fn get_md5(input: &Path) -> String {
    let mut hasher = Md5::new();
    read_buf(input, &mut |chunk| hasher.update(chunk));
    hasher
        .finalize()
        .as_slice()
        .iter()
        .map(|b| format!("{:02x}", b))
        .collect()
}

fn get_sha1(input: &Path) -> String {
    let mut hasher = Sha1::new();
    read_buf(input, &mut |chunk| hasher.update(chunk));
    hasher
        .finalize()
        .as_slice()
        .iter()
        .map(|b| format!("{:02x}", b))
        .collect()
}

fn get_sha256(input: &Path) -> String {
    let mut hasher = Sha256::new();
    read_buf(input, &mut |chunk| hasher.update(chunk));
    hasher
        .finalize()
        .as_slice()
        .iter()
        .map(|b| format!("{:02x}", b))
        .collect()
}

fn get_crc32(input: &Path) -> String {
    let crc = crc::Crc::<u32>::new(&crc::CRC_32_ISO_HDLC);
    let mut digest = crc.digest();
    read_buf(input, &mut |chunk| digest.update(chunk));
    format!("{:08x}", digest.finalize())
}

fn get_size(input: &Path) -> usize {
    let mut length = 0;
    read_buf(input, &mut |chunk| length += chunk.len());
    length
}

pub fn get_hashes(input: &Path) -> RomInfo {
    let filename = input
        .file_name()
        .and_then(|name| name.to_str())
        .unwrap_or("unknown")
        .to_string();

    RomInfo {
        filename,
        md5: get_md5(input),
        sha1: get_sha1(input),
        sha256: get_sha256(input),
        crc32: get_crc32(input),
        size: get_size(input),
    }
}
