#!/usr/bin/env python3

""" Functionality for handling data. """

import sys

class Data(dict):
    def __init__(self):
        dict.__init__(self)
        self.vocab_src = self.vocab_tgt = {}
        self.train_src = self.train_tgt = []
        self.dev_src = self.dev_tgt = []
        self.train_src_file = self.train_tgt_file = self.dev_src_file = self.dev_tgt_file = None

    def load(self, train_src=None, train_tgt=None, dev_src=None, dev_tgt=None):
        # Refactor this later
        if train_src:
            try:
                self.train_src_file = open(train_src)
            except OSError as err:
                print(err)

        # For language models, train_tgt can come from stdin
        if train_tgt:
            if train_tgt is sys.stdin:
                self.train_tgt_file = sys.stdin
            else:
                try:
                    self.train_tgt_file = open(train_tgt)
                except OSError as err:
                    print(err)

        if dev_src:
            try:
                self.dev_src_file = open(dev_src)
            except OSError as err:
                print(err)

        if dev_tgt:
            try:
                self.dev_tgt_file = open(dev_tgt)
            except OSError as err:
                print(err)


    def unload(self, all=False, file=None):
        # Close all open data files
        if all:
            for file in [self.train_src_file, self.train_tgt_file, self.dev_src_file, self.dev_tgt_file]:
                if file is not None:
                    try:
                        file.close()
                    except OSError as err:
                        print(err)

        # Close an individual file
        else:
            if file is not None:
                try:
                    file.close()
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
