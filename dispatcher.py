import argparse

def _get_args():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--host',
        help='dispatcher\'s host, by default localhost',
        default='localhost',
        action='store'
    )

    parser.add_argument(
        '--port',
        help='dispatcher\'s port, by default 8888',
        default=8888,
        action='store'
    )

    args = parser.parse_args()
    return args
