import nuke
import os

def go():

    nukeDir = os.environ['NUKE_TOOLS_DIR']
    os.chdir(nukeDir)

    if not os.path.exists("Shots"):
        os.mkdir("Shots")

    path = os.path.join(nukeDir, "Shots")
    os.chdir(path)
    filepath = nuke.toNode("root").name()


    if (filepath == "Root"):
        nuke.message("We need to save")
        nuke.scriptSave();
    else:
        if not os.path.exists("Versions"):
            os.mkdir("Versions")

        shotName = os.path.basename(filepath)
        shotName = shotName[:-3]
        path = os.path.join(path, "Versions/")
        os.chdir(path)

        x = 0;
        found = False
        while not found:
            x += 1
            shot = shotName + "_v" + str(x) + ".nk"
            if not os.path.exists(shot):
                found = True
                break



        nuke.scriptSave(path + shot);
