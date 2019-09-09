import argparse
import os
import socket
import subprocess

def _get_args():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--dispatcher-server',
        dest='dispatcher_server',
        help='dispatcher host:port, by default localhost:8888',
        default='localhost:8888',
        action='store'
    )

    parser.add_argument(
        'repo',
        metavar='REPO',
        type=str,
        help='path to the target repo to monitor'
    )

    args = parser.parse_args()
    return args


def _dispatch(host, port):

    if os.path.isfile('.commit_id'):

        try:
            resp = helpers.msg(host, int(port), 'status')
        except socket.error as e:
            raise Exception(f'Could not communicate with dispatcher server: {e}')

        if resp == 'OK':
            commit = ''
            with open ('.commit_id', 'r') as f:
                commit = f.readline()
            resp = helpers.msg(host, int(port), f'dispatch:{commit}')

            if resp != 'OK':
                raise Exception(f'Could not dispatch test: {resp}')

            print(f'Dispatched to {host}:{port}')
        else:
            raise Exception(f'Could not dispatch test: {resp}')





def poll_repo(args):

    repo       = args.repo
    host, port = args.dispatcher_server.split(':')

    while True:

        try:
            # call script that updates and checks repo
            #     - if changes, create a .commit_id file with latest commit in CWD
            #     - use a bash script to do the filesystem actions; cleaner/easier than python
            subprocess.check_output(['./scripts/update_repo.sh', repo])
        except subprocess.CalledProcessError as e:
            raise Exception(
                f'Could not update and check repository. '
                f'Reason: {e.output}'
            )

        _dispatch(host, port)
        time.sleep(5)


if __name__ == '__main__':

    args = _get_args()
    poll_repo(args)
