from random import randint
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='csv shuffler', usage='%(prog)s input.csv')
    parser.add_argument('input', help='Source csv file to shuffle.')
    return parser.parse_args()


def shuffle(contents):
    c = [line for line in contents.readlines()]
    newcsv = c.pop(0)
    while len(c) is not 0:
        newcsv += c.pop(randint(0, len(c) - 1))
    return newcsv


if __name__ == '__main__':
    args = parse_args()
    with open(args.input, 'r') as f:
        new = shuffle(f)
    with open(args.input, 'w') as f:
        f.write(new)
