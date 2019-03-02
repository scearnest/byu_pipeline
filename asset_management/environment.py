import getpass
import os
import pwd

import pipelineUtility

# from . import pipelineUtility


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

    def get_project_name(self):
        '''
        return the name of the current project
        '''
        pass

    def get_project_dir(self):
        '''
        return the absolute filepath to the directory of the current project
        '''
        pass

    def get_assets_dir(self):
        '''
        return the absolute filepath to the assets directory of the current project
        '''
        pass

    def get_shots_dir(self):
        '''
        return the absolute filepath to the shots directory of the current project
        '''
        pass

    def get_tools_dir(self):
        '''
        return the absolute filepath to the tools directory of the current project
        '''
        pass

    def get_crowds_dir(self):
        '''
        return the absolute filepath to the crowds directory of the current project
        '''
        pass

    def get_hda_dir(self):
        '''
        return the absolute filepath to the assembly directory of the current project
        (in a houdini pipeline, this is the otls directory)
        '''
        pass

    def _create_user(self, username):
        pass

    def get_user(self, username=None):
        pass

    def get_users_dir(self):
        '''
        :return the absolute filepath to the users directory of the current project
        '''
        return None

    def get_current_username(self):

        return self._current_username

    def get_user_workspace(self, username=None):
        '''
        :return the given users workspace. If no user is given, return the current user's workspace.
        '''