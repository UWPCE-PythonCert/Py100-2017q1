
import signal
import sys


def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')


signal.signal(signal.SIGINT, signal_handler)
line = sys.stdin.readline()
if line:
    print('hie')
else:
    print('you pressed Ctrl+D')
signal.pause()