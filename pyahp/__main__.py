# -*- coding: utf-8 -*-
"""pyahp.__main__

This module contains the common functions and methods to provide a CLI for the pyAHP package.
"""

import argparse
import json

from pyahp import parse
from pyahp.errors import AHPModelError


def parse_args():
    """Parse command line arguments.

    Returns:
         Command line arguments in form of a Namespace
    """
    parser = argparse.ArgumentParser(description='Solver for Analytic Hierarchy Process models.')
    parser.add_argument('-f', '--file',
                        metavar='FILE',
                        type=str,
                        nargs='+',
                        required=True,
                        help='configuration file(s) for Analytic Hierarchy Process')

    return parser.parse_args()


def print_priorities(alternatives, priorities):
    """Pretty print the alternatives and the priorities.

    Args:
        alternatives (list): List of alternatives.
        priorities (list): List of priorities corresponding to the alternatives.
    """
    print('\tResults:')
    for priority, alternative in zip(priorities, alternatives):
        print('\t\t{}: {}'.format(alternative, priority))
    idx = np.argmax(priorities)
    print('\tRecommanded is [%d]%s'%(idx, alternatives[idx]))


def main():
    """Main function of the script.

    This function parses the command line arguments, validates and creates the AHP models
    and prints the summary of all the AHP models.
    """
    args = parse_args()

    models = {file: json.load(open(file)) for file in args.file}

    for name, model in models.items():
        print('[+] {}'.format(model.get('name', name)))
        try:
            ahp_model = parse(model)
            print('\tMethod: {}'.format(model['method']))

            print_priorities(model['alternatives'], ahp_model.get_priorities())

        except AHPModelError as err:
            print('\t[-] ERROR:AHPConfigError {}'.format(err))

        except Exception as err:
            print('\t[-] ERROR:{} {}'.format(err.__class__.__name__, err))


if __name__ == '__main__':
    main()
