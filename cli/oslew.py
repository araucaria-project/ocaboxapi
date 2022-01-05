#!/usr/bin/env python3
"""
OCAbox: slew the telescope to position

"""
import argparse
import logging

from tqdm import tqdm

from ocaboxapi import Observatory
from ocaboxapi.config import Config
from ocaboxapi.observatory import Telescope

logger = logging.getLogger('slew')

def parse_args():
    parser = argparse.ArgumentParser(description=__doc__, epilog=f'Config files:{" ".join(Config.default_files)}')
    coo_grp = parser.add_mutually_exclusive_group(required=True)
    coo_grp.add_argument('-r', '--equatorial', nargs=2, metavar=('RA', 'DEC'))
    coo_grp.add_argument('-a', '--horizontal', nargs=2, metavar=('AZ', 'ALT'))
    parser.add_argument('-t', '--telescope', metavar='TELESCOPE',
                         help='Specify telescope to operate; if there is only one telescope in config preset, this'
                              'parameter can be omitted; e.g. "obs.my_telesocpe"; use olist command'
                              'to list sys_id of all devices')
    parser.add_argument('-p', '--preset', help='configuration preset; if not provided, program will lookup for preset '
                                               'named "default" in configuration file(s)')
    parser.add_argument('-n', '--nowait', action='store_true',
                        help='exit immediately - do not block until slew completes (send asynchronous command)')
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

    # 3. Find the telescope object
    tel = None
    if args.telescope:
        try:
            tel = obs.component_by_absolute_sys_id(args.telescope)
        except LookupError:
            ts = []
            for c in obs.children_tree_iter():
                if c.kind == 'telescope':
                    ts.append(c)
            logger.error('Can not find telescope sys_id="%s". Check parameter or active preset in config file. '
                         'Telescopes in config preset: %s', args.telescope, ', '.join([t.sys_id for t in ts]))
            exit(1)
        if tel.kind != 'telescope':
            logger.error('Device referred by sys_id="%s is not of kind "telescope"', args.telescope)
            exit(1)
    else:
        ts = []
        for c in obs.children_tree_iter():
            if c.kind == 'telescope':
                ts.append(c)
        if len(ts) == 0:
            logger.error('Can not find any telescopes in configuration preset')
            exit(1)
        elif len(ts) > 1:
            logger.error('Specify telescope with -t option. Telescopes in config preset: %s',
                         ', '.join([t.sys_id for t in ts]))
            exit(1)
        else:
            tel = ts[0]
    tel: Telescope = tel  # set the type just to make editor happy

    # 4. Slew telescope
    logger.info('Slewing telescope "%s"', tel.sys_id)
    if args.equatorial:
        if args.nowait:
            tel.slewtocoordinatesasync(*args.equatorial)
        else:
            tel.slewtocoordinates(*args.equatorial)
            logger.info('Done')
    else:
        if args.nowait:
            tel.slewtoaltazasync(*args.horizontal)
        else:
            tel.slewtoaltaz(*args.horizontal)
            logger.info('Done')



if __name__ == '__main__':
    main()
