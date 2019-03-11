import os
import shutil

from .asset import Asset, AssetType
# from .department import Department
from .element import Element
from .checkout import Checkout
from .environment import Environment
from .user import User
from . import pipelineUtility
from .registry import Registry

# FIXME: This class is pointless for the most part. It's just referring to Environment class for everything


class Project():
	def __init__(self):
		self.env = Environment()

	def get_name(self):
		return self.env.get_project_name()

	def get_project_dir(self):
		return self.env.get_project_dir()

	def get_assets_dir(self):
		return self.env.get_assets_dir()

	def get_users_dir(self):
		return self.env.get_users_dir()

	def get_user(self, username):
		return self.env.get_user(username)

	def get_current_username(self):
		return self.env.get_current_username()

	'''
	:name:      name of the object
	:return:    Asset object with the given name
	'''
	def get_asset(self, name):  # TODO: WE MAY NEED TO ADD MORE TO THIS FUNCTION BASED ON AssetType
		file_path = os.path.join(self.get_assets_dir(), name)
		if not os.path.exists(file_path):
			return None
		return Asset(file_path)

	'''
	:name:      the name of the new asset to create
	:asset_type: type of asset to create
	:return:    a new asset with the given name
	'''
	def create_asset(self, name, asset_type):
		name = pipelineUtility.alphanumeric(name)
		file_path = os.path.join(Asset.get_parent_directory(), name)

		if name in self.list_assets():
			raise EnvironmentError('asset already exists: ' + file_path)
		if not pipelineUtility.mkdir(file_path):
			raise OSError('couldn\'t create body directory: ' + file_path)
		# datadict = Asset.create_new_dict(name)

		pipelineUtility.write_file(os.path.join(file_path, Asset.PIPELINE_FILENAME), datadict)  # TODO: NEED A BETTER WAY TO WRITE FILES
		new_asset = Asset(file_path)  # TODO: ADD AN ASSET TYPE TO CONSTRUCTOR

		for dept in Asset.default_departments():
			pipelineUtility.mkdir(os.path.join(file_path, dept))
			new_asset.create_element(dept, Element.DEFAULT_NAME)  # FIXME

		return new_asset

	'''
	:return:        a list of strings containing the names of all assets in this project
	:filter:        a tuple containing an attribute (string) relation (operator) and value
				e.g. (Asset.TYPE, operator.eq, AssetType.CHARACTER). Only returns assets whose
				given attribute has the relation to the given desired value. Defaults to None.
	'''
	def list_assets(self, file_path=None, filter=None):
		if file_path is None:
			file_path = self.get_assets_dir()
			
		directory_list = os.listdir(file_path)
		asset_list = []

		for directory in directory_list:
			abspath = os.path.join(file_path, directory)
			if os.path.exists(os.path.join(abspath, Asset.PIPELINE_FILENAME)):
				asset_list.append(directory)

		asset_list.sort()

		if filter is not None and len(filter) == 3:  # TODO: Do something with filter. At least filter by asset type
			filtered_asset_list = []
			for asset in asset_list:
				obj = self.get_asset(asset)
				if obj.has_relation(filter[0], filter[1], filter[2]):  # TODO: learn more
					filtered_asset_list.append(asset)
			asset_list = filtered_asset_list

		return asset_list

	def list_users(self):
		users_dir = self.get_users_dir()
		dir_list = os.listdir(users_dir)
		user_list = []

		for username in dir_list:
			user_file = os.path.join(users_dir, username, User.PIPELINE_FILENAME)
			if os.path.exists(user_file):
				user_list.append(username)

		user_list.sort()
		return user_list

	def is_checkout_dir(self, path):
		return os.path.exists(os.path.join(path, Checkout.PIPELINE_FILENAME))

	def get_checkout(self, path):
		if not self.is_checkout_dir(path):
			return None
		return Checkout(path)

	def get_checkout_element(self, path):
		checkout = self.get_checkout(path)
		if checkout is None:
			return None

		asset = self.get_asset(checkout.get_asset_name())
		element = asset.get_element(checkout.get_department_name(), checkout.get_element_name())  # TODO: Finish asset class
		return element

	def delete_asset(self, asset):
		if asset in self.list_assets():
			shutil.rmtree(os.path.join(self.get_assets_dir(), asset))
