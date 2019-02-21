import nuke
import Hello_World


menubar = nuke.menu("Nuke")
# Custom Lab Tools
toolbar = nuke.toolbar("Nodes")
m = toolbar.addMenu("Hello_World", icon="y.svg")
m.addCommand("hello_world", 'Hello_World.go()', icon="checkout.svg")
