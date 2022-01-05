#!/usr/bin/env python3
"""
OCAbox: list observatory devices.

Lists all observatory devices in active configuration.
The kind, sys_id and comment are taken from config file.
Other data is taken from telescope if connection works.
"""
import argparse
import logging

from tabulate import tabulate
from tqdm import tqdm

from ocaboxapi import Observatory
from ocaboxapi.config import Config
from ocaboxapi.exceptions import DeviceResponseError, RequestConnectionError


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__, epilog=f'Config files:{" ".join(Config.default_files)}')
    parser.add_argument('-p', '--preset', help='configuration preset; if not provided, program will lookup for preset '
                                               'named "default" in configuration file(s)')
    parser.add_argument('-N', '--noprogress', action='store_true',
                        help='do not show progress bar')
    # parser.add_argument('-c', '--config', metavar='FILE',
    #                     help='configuration file; if provided will be parsed after default config files')
    parser.add_argument('-v', '--verbose', action="count", default=0,
                        help='print more info (loglevel=INFO); (-vv for DEBUG)')
    return parser.parse_args()

def main():
    # 1. Basic CLI (Command Line Interface) stuff, parsing arguments, setting loglevel
    args = parse_args()
    logging.basicConfig(level=logging.WARN - 10 * args.verbose)  # 30=WARN, 20=INFO, 10=DEBUG...

    # 2. Standard Observatory initialization
    obs = Observatory()
    obs.connect(preset=args.preset)

    # 3. Iteration of all children of Observatory object
    children = []

    #  tqdm creates progressbar, obs.children_tree_iter() is an iterator
    for c in tqdm(obs.children_tree_iter(),
                  total=obs.children_count() + 1, leave=False, colour='green', disable=args.noprogress):
        row_part1 = [c.kind, c.sys_id]
        try:  # connection may fail, Component may not be a Device
            row_part2 = [
                c.name(),
                c.connected(),
                c.description(),
                c.driverversion(),
            ]
        except AttributeError:  # c is not a Device (so lacks those methods)
            row_part2 = ['', '', '', '']
        except (RequestConnectionError, DeviceResponseError):  # connection to telescope failed
            row_part2 = ['<con-err>', '<con-err>', '<con-err>', '<con-err>']
        row_part2.append(c.component_options.get('comment', ''))  # one more column – optional 'comment' option
        children.append(row_part1 + row_part2)

    # 4. Printing tabulated results
    print(tabulate(children, headers=(
        'kind', 'sys_id', 'name', 'connected', 'description', 'drv ver', 'comment',
    )))


if __name__ == '__main__':
    main()
