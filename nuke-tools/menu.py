import nuke
import Hello_World
import version_up


menubar = nuke.menu("Nuke")
# Custom Lab Tools
toolbar = nuke.toolbar("Nodes")
m = toolbar.addMenu("Sam's Menu", icon="y.svg")
m.addCommand("hello_world", 'Hello_World.go()', icon="checkout.svg")
m.addCommand("Version Up", 'version_up.go()', icon = "checkout.svg")
