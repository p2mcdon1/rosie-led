from animation import Animation
from asciistripfactory import AsciiStripFactory
from parms import Parms
from pythreader import PyThreader
from keyreader import KeyReader
from runner import Runner
import time

Parms.count = 60

Animation.stripFactory = AsciiStripFactory()

pyThreader = PyThreader()
keyReader = KeyReader()
runner = Runner(keyReader, pyThreader)

print()
for x in range(10):
    print("Progress {:2.1%}".format(x / 10), end="\r")
    time.sleep(1)

runner.run()
