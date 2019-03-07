from enum import Enum
import os

from .environment import Environment
from . import pipelineUtility


class Asset:

	PIPELINE_FILENAME = ".asset"

	# TODO: WE NEED A BETTER CONSTRUCTOR. ONE THAT DOESN'T REQUIRE SO MANY ARGUMENTS.
	def __init__(self, name, references=None, asset_type=None, environment=None, file_path=None, pipeline_file=None, assets=None):
		if references is not None:
			self.name = name
			self.references = references
			self.type = asset_type
			self.environment = environment
			self.file_path = file_path
			self.pipeline_file = pipeline_file
			self.assets = assets
		else:
			# name is file path of an asset
			self.file_path = name
			self.env = Environment()
			self.pipeline_file = os.path.join(name, Asset.PIPELINE_FILENAME)
			if not os.path.exists(self.pipeline_file):
				raise EnvironmentError('not a valid asset: ' + self.pipeline_file + ' does not exist')
			self._datadict = pipelineUtility.read_file(self.pipeline_file)

	def default_departments(self):
		return  # TODO stuff

	def get_parent_directory(self):
		return  # TODO stuff

	def get_type(self):
		return self.type

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


class AssetType(Enum):
	Character_Group = 1
	Prop = 2
	Environment = 3
	Set = 4
	Shot = 5
	Character = 6
	Tool = 7
	Crowd_Cycle = 8
