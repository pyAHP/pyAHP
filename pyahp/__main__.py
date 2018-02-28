import argparse
import json

from pyahp import parse
from pyahp.errors import AHPConfigError


def parse_args():
    parser = argparse.ArgumentParser(description='Solver for Analytic Hierarchy Process models.')
    parser.add_argument('-f', '--file',
                        metavar='FILE',
                        type=str,
                        nargs='+',
                        required=True,
                        help='configuration file(s) for Analytic Hierarchy Process')

    return parser.parse_args()


def print_priorities(alternatives, priorities):
    for i in range(len(alternatives)):
        print('\t{}: {}'.format(alternatives[i], priorities[i]))


if __name__ == '__main__':
    args = parse_args()

    models = {}

    for file in args.file:
        models[file] = json.load(open(file))

    for name, model in models.items():
        try:
            print('[+] {}'.format(model.get('name', name)))
            ahp_model = parse(model)

            priorities, _ = ahp_model.get_priorities()
            alternatives = model['alternatives']

            print_priorities(alternatives, priorities)

        except AHPConfigError as e:
            print('\t[-] ERROR:AHPConfigError {}'.format(e))
        except Exception as e:
            print('\t[-] ERROR:{} {}'.format(e.__class__.__name__, e))

