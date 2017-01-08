#!/usr/bin/env python3

"""
...
"""

import sys
import match.data.io as io


def main():
    """ ... """
    import argparse
    parser = argparse.ArgumentParser(description='...')

    parser.add_argument('--batch_size', type=int, default=16, help="Batch size")
    parser.add_argument('-d', '--dev', type=str, help="Load dev/tuning file")
    parser.add_argument('--epochs', type=int, default=20, help="Maximum number of epochs")
    parser.add_argument('-i', '--in', dest='input', type=str, default=sys.stdin,
            help="Load input training file")
    parser.add_argument('--learning_rate', type=float, default=0.001, help="Learning rate")
    parser.add_argument('-m', '--model', help="Filename of model to load and/or save")
    parser.add_argument('-o', '--out', dest='output', type=str, default=sys.stdout, help="")
    parser.add_argument('--opt', type=str, default='adam', help="Optimizer")
    parser.add_argument('-v', '--verbose', action='count', default=0, help="Increase verbosity. You can use multiple of these.")
    args = parser.parse_args()
    print("Config: %s" % args, file=sys.stderr)


    # Load input data
    data = io.Data()
    data.load(train_tgt_filename=args.input)
    print("Input sentences:", len(data.train_tgt), file=sys.stderr)
    print("Alphabet size:  ", len(data.vocab_tgt), file=sys.stderr)

    # Build model
    #model = model.Model(arch='lm', args=args)

    # Train model
    #model.train()


if __name__ == '__main__':
    main()
