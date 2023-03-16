from animations.animationbase import AnimationBase
from buttons.keyreader import KeyReader
from parms import Parms
from runner import Runner
from strips.asciistripfactory import AsciiStripFactory
from threads.pythreader import PyThreader

Parms.count = 80
Parms.refresh = 0.2

AnimationBase.stripFactory = AsciiStripFactory()

pyThreader = PyThreader()
keyReader = KeyReader()
runner = Runner(keyReader, pyThreader)

print()
runner.run()
