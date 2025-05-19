import argparse
from . import converter


def main():
    parser = argparse.ArgumentParser(description="Convert Armenian orthography")
    parser.add_argument('input', help='Input text file')
    parser.add_argument('output', help='Output text file')
    parser.add_argument('--direction', choices=['to_mashtots', 'to_soviet'], required=True,
                        help='Conversion direction')
    parser.add_argument('--show-path', action='store_true', help='Show intermediate steps')
    args = parser.parse_args()

    with open(args.input, encoding='utf-8') as f:
        text = f.read()

    if args.direction == 'to_mashtots':
        result = converter.soviet_to_mashtots(text, show_path=args.show_path)
    else:
        result = converter.mashtots_to_soviet(text, show_path=args.show_path)

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(result)


if __name__ == '__main__':
    main()
