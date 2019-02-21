import nuke

nuke.message('Hello_World')

def go():
    nuke.createNode("Cube")
    nuke.createNode("Scene")
