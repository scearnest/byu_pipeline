import os


class Asset:

    def __init__(self, name, references, asset_type, environment, file_path, pipeline_file, assets):
        self.name = name
        self.references = references
        self.type = asset_type
        self.environment = environment
        self.file_path = file_path
        self.pipeline_file = pipeline_file
        self.assets = assets
    
    def getDepartments(self):
        return  # TODO stuff

    def getParentDirectory(self):
        return  # TODO stuff

    def getType(self):
        return self.type

    def getElement(self):
        return  # TODO stuff

    def createElement(self):
        return  # TODO stuff

    def listElements(self):
        return  # TODO stuff

    def addReference(self):
        return  # TODO stuff

    def removeReference(self):
        return  # TODO stuff

    def setDescription(self):
        return  # TODO stuff

    def getReferences(self):
        return  # TODO stuff

    def hasRelation(self):
        return  # TODO stuff

    def getInfo(self):
        return  # TODO stuff

