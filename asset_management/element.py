

class Element():
    def __init__(self, pipeline_filename, default_name, parent, default_cache_dir, status, latest_version, assigned_user, publishes, start_date, end_date, app_ext, cache_ext, cache_filepath, checkout_users, notes):
        self.pipeline_filename = pipeline_filename
        self.default_name = default_name
        self.parent = parent
        self.default_cache_dir = default_cache_dir
        self.status = status
        self.latest_version = latest_version
        self.assigned_user = assigned_user
        self.published = publishes
        self.start_date = start_date
        self.end_date = end_date
        self.app_ext = app_ext
        self.cache_ext = cache_ext
        self.cache_filepath = cache_filepath
        self.checkout_users = checkout_users
        self.notes = notes
        pass

    def load_pipeline_filepath(self):
        return  # TODO stuff

    def update_pipeline_file(self):
        return  # TODO stuff

    def checkout(self):
        return  # TODO stuff

    def publish(self):
        return  # TODO stuff

    def get_shot_name(self):
        return  # TODO stuff

    def get_last_publish(self):
        return  # TODO stuff

    def update_cache(self):
        return  # TODO stuff

class ElementFactory():
    def __init__(self):
        pass


