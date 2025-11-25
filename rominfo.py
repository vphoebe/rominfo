import sys
import argparse
from helpers.outputs import get_dat_string
from helpers.outputs import get_file_string


def read_file_args():
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

    strings = []
    for file_path in args.file:
        try:
            print(f"Processing {file_path}...")
            string = ''
            if args.dat:
                string = get_dat_string(file_path)
            else:
                string = get_file_string(file_path)
            strings.append(string)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"Error reading '{file_path}': {str(e)}")

    with open(args.output_file, 'w') as output:
        output.write(''.join(strings))
        print(f"Wrote {len(strings)} file(s) to {args.output_file}")


if __name__ == "__main__":
    sys.exit(read_file_args())
