import json


class Department:

	def __init__(self,name, nice_name, has_cache, file_formats):
		self.name = name
		self.nice_name = nice_name
		self.has_cache = has_cache
		self.file_formats = file_formats

	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	def setNiceName(self, nice_name):
		self.nice_name = nice_name

	def getNiceName(self):
		return self.nice_name

	def setHasCache(self, has_cache):
		self.has_cache = has_cache

	def isHasCache(self):
		return self.name

	def getNiceName(self, nice_name):
		self.nice_name = nice_name

	def setNiceName(self):
		return self.nice_name