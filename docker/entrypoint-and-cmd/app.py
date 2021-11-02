import argparse


def main(direction: str):
    print(f"About to move in the {direction} direction")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Awesome app')
    parser.add_argument('--direction', choices=['up', 'down', 'left', 'right'], required=True)
    args = parser.parse_args()

    main(args.direction)
