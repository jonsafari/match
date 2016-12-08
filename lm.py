#!/usr/bin/env python3

"""
...
"""

import sys
import numpy as np
import tensorflow as tf


def main():
    import argparse
    parser = argparse.ArgumentParser(description='...')

    parser.add_argument('--batch_size', type=int, default=16, help="Batch size")
    parser.add_argument('-d', '--dev', type=str, help="Load dev/tuning file")
    parser.add_argument('--epochs', type=int, default=20, help="Maximum number of epochs")
    parser.add_argument('-i', '--in', type=str, default=sys.stdin, help="Load input training file")
    parser.add_argument('--learning_rate', type=float, default=0.001, help="Learning rate")
    parser.add_argument('-m', '--model', help="Filename of model to load and/or save")
    parser.add_argument('-o', '--out', type=str, default=sys.stdout, help="")
    parser.add_argument('--opt', type=str, default='adam', help="Optimizer")
    args = parser.parse_args()
    ...

if __name__ == '__main__':
    main()
