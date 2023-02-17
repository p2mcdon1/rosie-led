from animation import Animation
from runner import Runner
from microthreader import MicroThreader
from momentarySwitch import MomentarySwitch
from neopixelstripfactory import NeoPixelStripFactory

Animation.stripFactory = NeoPixelStripFactory()

momentarySwitch = MomentarySwitch()
microThreader = MicroThreader()
runner = Runner(momentarySwitch, microThreader)

runner.run()
