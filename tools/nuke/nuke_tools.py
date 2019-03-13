import os
import nuke
from PySide import QtGui
from tools.tools import Tools


class NukeTools(Tools):

    def __init__(self):
        pass

    def checkout(self):
        global nuke_checkout_dialog
        parent = QtGui.QApplication.activeWindow()
        nuke_checkout_dialog = CheckoutWindow(parent, [Department.COMP])
        nuke_checkout_dialog_dialog.finished.connect(post_checkout)

        def post_checkout():
        	filepath = nuke_checkout_dialog.result

        	if filepath is not None:

        		if not os.path.exists(filepath):
        			print "new file "+filepath
        			nuke.scriptSaveAs(filepath+".nk")
        		else:
        			print "open file "+filepath
        			nuke.scriptOpen(filepath)


    def publish(self):
        parent = QtGui.QApplication.activeWindow()
    	filepath = nuke.toNode("root").name()
    	global nuke_publish_dialog
    	nuke_publish_dialog = PublishWindow(filepath, parent, [Department.COMP])
    	nuke_publish_dialog.finished.connect(post_publish)

        def post_publish():
        	element = nuke_publish_dialog.result

        	if nuke_publish_dialog.published:

        		nuke.scriptSave()


        		user = nuke_publish_dialog.user
        		src = nuke_publish_dialog.src
        		comment = nuke_publish_dialog.comment
        		dst = element.publish(user, src, comment)

        		try:
        			os.chmod(dst, 0660)
        		except:
        			pass

        		print "TODO: export playblast"
        		print nuke_publish_dialog.result.get_name()

    def rollback(self):
        parent = QtGui.QApplication.activeWindow()
    	filepath = nuke.toNode("root").name()
    	shot = os.path.basename(filepath)
    	index = shot.find("_comp")
    	if index > 0:
    		base_name = shot[:index]
    		print base_name
    	else:

    		global rollback_selection_window
    		rollback_selection_window = SelectionWindow(parent, dept_list=[Department.COMP])
    		rollback_selection_window.finished.connect(post_selection)
    		return

    	project = Project()
    	body = project.get_body(base_name)
    	element = body.get_element(Department.COMP)

    	global rollback_window
    	rollback_window = RollbackWindow(element, parent)
    	rollback_window.finished.connect(post_rollback)

        def post_rollback():
        	filepath = rollback_window.result

        	if filepath is not None:
        		nuke.scriptClose()
        		print "open file " + filepath
        		nuke.scriptOpen(filepath)

        def post_selection():
        	parent = QtGui.QApplication.activeWindow()
        	element = rollback_selection_window.result
        	if element is None:
        		return
        	global rollback_window
        	rollback_window = RollbackWindow(element, parent)
        	rollback_window.finished.connect(post_rollback)
