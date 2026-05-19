# rominfo
A utility for generating hashes for ROM files, specifically for No-Intro submissions.

# Usage
``` shell
Usage: rominfo [OPTIONS] [INPUT_FILES]...

Arguments:
  [INPUT_FILES]...  Binary files to hash

Options:
  -o, --output-file <OUTPUT_FILE>  [default: hashes.txt]
  -d, --dat                        Output Redump DAT lines
  -h, --help                       Print help
  -V, --version                    Print version
```

## KDE/Dolphin service menu entry (for right-click context menu)
1. Place `rominfo.desktop` in `~/.local/share/kio/servicemenus` (Create if it doesn't exist yet)
2. Update the `Exec` paths to point to an absolute path for `rominfo`.

# Example outputs

## Standard (No-Intro)
```
--- Tetris Battle Gaiden (Japan).sfc ---
Size: 1048576 bytes
CRC32: b8f5f846
MD5: f21e1fefcb3187877060b3fafb53abd2
SHA-1: e455607b32b0adf14bf4af917cbf6561eccd1d0d
SHA-256: 7a96458b60507b60b581b7a1ba32f2855cff18d6f13bfeb45ad161dd469c5c61
```

## Redump DAT
```
<rom name="Shenmue - Isshou Yokosuka (Japan) (Disc 1) (Track 1).bin" size="24402000" crc="65ad246" md5="f6543c78c44a26bb133f68acf10291dc" sha1="4dd8b454abfc97ff0d2278035dbfdc0f9a8deee3" />
```
