import os
from . import pipelineUtility


class Checkout:

    PIPELINE_FILENAME = ".checkout"

    def __init__(self, file_path):
        self.file_path = file_path
        self.pipeline_file = os.path.join(file_path, self.PIPELINE_FILENAME)

        if not os.path.exists(self.pipeline_file):
            raise EnvironmentError("Not a valid checkout directory: " + self.file_path)
        json = pipelineUtility.read_file(self.pipeline_file)

        self.username = json["user"]
        self.asset_name = json["asset_name"]
        self.element = json["element_name"]
        self.department = json["department"]

        self.files = []
        self.times = []

    def set_username(self, username):
        self.username = username

    def set_asset_name(self, name):
        self.asset_name = name

    def set_element(self, element):
        self.element = element

    def set_files(self, files):
        self.files = files

    def set_times(self, times):
        self.times = times

    def get_username(self):
        return self.username

    def get_asset_name(self):
        return self.asset_name

    def get_department_names(self):
        return self.department

    def get_element_name(self):
        return self.element

    def get_files(self):
        return self.files

    def get_times(self):
        return self.times

    def add_operation(self, file_path):
        self.files.append(file_path)
        self.times.append(pipelineUtility.timestamp())
        pipelineUtility.write_file(self.pipeline_file, self.make_dictionary())

    def make_dictionary(self):
        dictionary = {}

        dictionary["user"] = self.username  # TODO: Don't know what yet, but pretty sure I need to change something
        dictionary["asset_name"] = self.asset_name
        dictionary["department"] = self.department
        dictionary["element_name"] = self.element
        dictionary["filename"] = self.files
        dictionary["time"] = self.times

        return dictionary
