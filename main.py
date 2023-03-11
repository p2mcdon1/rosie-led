from animation import Animation
from asciistripfactory import AsciiStripFactory
from parms import Parms
from pythreader import PyThreader
from keyreader import KeyReader
from runner import Runner

Parms.count = 80
Parms.refresh = 0.2

Animation.stripFactory = AsciiStripFactory()

pyThreader = PyThreader()
keyReader = KeyReader()
runner = Runner(keyReader, pyThreader)

print()
runner.run()
