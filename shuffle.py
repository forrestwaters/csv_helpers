from random import randint
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='csv shuffler', usage='%(prog)s input.csv')
    parser.add_argument('input', help='Source csv file to shuffle.')
    parser.add_argument('num_shuffles', default=1, nargs='?', type=int, help='Source csv file to shuffle.')
    return parser.parse_args()


def shuffle(contents):
    c = [line for line in contents.readlines()]
    # pull the header out
    newcsv = c.pop(0)
    while len(c) is not 0:
        # This maintains the \n chars from the original file
        newcsv += c.pop(randint(0, len(c) - 1))
    return newcsv


if __name__ == '__main__':
    args = parse_args()
    for i in range(0, args.num_shuffles):
        with open(args.input, 'r') as f:
            new = shuffle(f)
        with open(args.input, 'w') as f:
            f.write(new)
