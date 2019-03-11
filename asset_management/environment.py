import getpass
import os
#import pwd

import pipelineUtility

#from . import pipelineUtility


def test():
	print(pipelineUtility.timestamp())


class Environment():

    PROJECT_ENV = 'BYU_PROJECT_DIR'
    PIPELINE_FILENAME = '.project'

    PROJECT_NAME = 'name'
    PRODUCTION_DIR = 'production_dir'
    ASSETS_DIR = 'assets_dir'
    SHOTS_DIR = 'shots_dir'
    TOOLS_DIR = 'tools_dir'
    CROWDS_DIR = 'crowds_dir'
    USERS_DIR = 'users_dir'
    HDA_DIR = 'hda_dir'
    EMAIL_ADDRESS = 'email_address'
    EMAIL_PASSWORD = 'email_password'

    def _init_(self):
        pass

    def getProjectName(self):
        '''
        return the name of the current project
        '''
        pass

    def getProjectDir(self):
        '''
        return the absolute filepath to the directory of the current project
        '''
        pass

    def getAssetsDir(self):
        '''
        return the absolute filepath to the assets directory of the current project
        '''
        pass

    def getShotsDir(self):
        '''
        return the absolute filepath to the shots directory of the current project
        '''
        pass

    def getToolsDir(self):
        '''
        return the absolute filepath to the tools directory of the current project
        '''
        pass

    def getCrowdsDir(self):
        '''
        return the absolute filepath to the crowds directory of the current project
        '''
        pass

    def getHdaDir(self):
        '''
        return the absolute filepath to the assembly directory of the current project
        (in a houdini pipeline, this is the otls directory)
        '''
        pass

    def createUser(self, username):
        pass

    def getUser(self, username=None):
        pass

    def getUsersDir(self):
        '''
        :return the absolute filepath to the users directory of the current project
        '''
        return None

    def getCurrentUsername(self):

        return self._current_username

    def getUserWorkspace(self, username=None):
        '''
        :return the given users workspace. If no user is given, return the current user's workspace.
        '''