#!/usr/bin/env python3

""" Functionality for handling data. """

import sys

class Data(dict):
    def __init__(self):
        dict.__init__(self)
        self.vocab_src = self.vocab_tgt = {}
        self.train_src = self.train_tgt = []
        self.dev_src = self.dev_tgt = []

    def load(self, train_src_filename=None, train_tgt_filename=None,
            dev_src_filename=None, dev_tgt_filename=None):
        # Refactor this later
        if train_src_filename:
            try:
                with open(train_src_filename) as f:
                    self.train_src = f.read().split('\n')
                    self.train_src.pop()
            except OSError as err:
                print(err)

        # For language models, train_tgt can come from stdin
        if train_tgt_filename:
            if train_tgt_filename is sys.stdin:
                self.train_tgt = sys.stdin.read().split('\n')
                self.train_tgt.pop()
            else:
                try:
                    with open(train_tgt_filename) as f:
                        self.train_tgt = f.read().split('\n')
                        self.train_tgt.pop()
                except OSError as err:
                    print(err)

        if dev_src_filename:
            try:
                with open(dev_src_filename) as f:
                    self.dev_src = f.read().split('\n')
                    self.dev_src.pop()
            except OSError as err:
                print(err)

        if dev_tgt_filename:
            try:
                with open(dev_tgt_filename) as f:
                    self.dev_tgt = f.read().split('\n')
                    self.dev_tgt.pop()
            except OSError as err:
                print(err)


    def __repr__(self):
        s = []
        s.append("vocab-src: %i entries\n" % len(self.vocab_src))
        s.append("vocab-tgt: %i entries\n" % len(self.vocab_tgt))
        s.append("train-src: %i sentences\n" % len(self.train_src))
        s.append("train-tgt: %i sentences\n" % len(self.train_tgt))
        s.append("dev-src:   %i sentences\n" % len(self.dev_src))
        s.append("dev-tgt:   %i sentences" % len(self.dev_tgt))
        return ''.join(s)


def main():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    main()
