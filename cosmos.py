#!/usr/bin/env python3

import argparse
import pycosmos

from pycosmos.game import Game


def main(args):
    game = Game()
    game.run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="cosmos",
        description="runs the cosmos pygame UI",
        epilog="please submit bugs on github.com/bbengfort/pycosmos"
    )

    parser.add_argument("--version", action="version", version=f"%(prog)s v{pycosmos.__version__}")

    args = parser.parse_args()
    main(args)
