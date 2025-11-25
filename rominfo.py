import sys
import argparse
from helpers.hashes import get_hashes
from helpers.format import get_file_string


def rominfo():
    parser = argparse.ArgumentParser(
        description='Generate common hashes for ROM files.')

    parser.add_argument(
        '-d',
        '--dat',
        help="Output as Redump DAT lines",
        action="store_true"
    )
    parser.add_argument(
        '-o',
        '--output_file',
        nargs="?",
        help="Specify output file path (defaults to hashes.txt)",
        default="hashes.txt",
        const="hashes.txt",
    )
    parser.add_argument(
        'file',
        nargs='+',
        help="path(s) to ROM file"
    )
    args = parser.parse_args()

    result = ""
    for file_path in args.file:
        try:
            print(f"Processing {file_path}...")
            hashes = get_hashes(file_path)
            line = get_file_string(hashes, args.dat)
            result += line
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"Error reading '{file_path}': {str(e)}")

    with open(args.output_file, 'w') as out:
        out.write(result)
        print(f"Wrote {len(args.file)} file(s) to {args.output_file}")


if __name__ == "__main__":
    sys.exit(rominfo())
