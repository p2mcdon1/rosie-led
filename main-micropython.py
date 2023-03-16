from animations.animationbase import AnimationBase
from buttons.momentary import Momentary
from runner import Runner
from strips.neopixelstripfactory import NeoPixelStripFactory
from threads.microthreader import MicroThreader

AnimationBase.stripFactory = NeoPixelStripFactory()

momentarySwitch = Momentary()
microThreader = MicroThreader()
runner = Runner(momentarySwitch, microThreader)

runner.run()
