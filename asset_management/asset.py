

class Asset:

    def __init__(self, name, references, body_type, environment, file_path, pipeline_file):
        self.name = name
        self.references = references
        self.body_type = body_type
        self.environment = environment
        self.file_path = file_path
        self.pipeline_file = pipeline_file
    
    def default_departments(self):
        return  # TODO stuff

    def get_parent_directory(self):
        return  # TODO stuff

    def get_body_type(self):
        return self.body_type

    def get_element(self):
        return  # TODO stuff

    def create_element(self):
        return  # TODO stuff

    def list_elements(self):
        return  # TODO stuff

    def add_reference(self):
        return  # TODO stuff

    def remove_reference(self):
        return  # TODO stuff

    def set_description(self):
        return  # TODO stuff

    def get_references(self):
        return  # TODO stuff

    def has_relation(self):
        return  # TODO stuff

    def get_info(self):
        return  # TODO stuff

