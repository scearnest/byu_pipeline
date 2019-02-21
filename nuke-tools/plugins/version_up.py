import nuke
import os

def go():



    filepath = nuke.toNode("root").name()

    if (filepath != "Root"):
        nuke.message("We need to save")
        nuke.scriptSave();

    else:
        nukeDir = os.environ['NUKE_TOOLS_DIR']
        path = os.path.join(nukeDir, "versions")
        os.chdir(path)

        if os.path.exists("shot_01"):

            nuke.message(filepath)
        else:
            nuke.message(os.getcwd())
