import argparse


class View:
    def __init__(self):
        self.parser = argparse.ArgumentParser()

        self.parser.add_argument(
            "file_length",
            type=int,
            help="the number of characters to be written to the file",
        )

        self.parser.add_argument("file_path", type=str, help="the path to write the file to")

    def args(self):
        return self.parser.parse_args()
