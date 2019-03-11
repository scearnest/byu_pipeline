import glob
import json
import os
import stat
import re
import smtplib
import time


def read_file(filepath):
	with open(filepath, "r") as json_file:
		json_data = json.load(json_file)

	return json_data


def write_file(some_arg):
	pass


def mkdir(dirpath):
	try:
		os.mkdir(dirpath)
		os.chmod(dirpath, stat.S_IRWXO | stat.S_IRWXG | stat.S_IRWXU)  # read, write, execute by all
	except OSError as e:
		print(e)
		return False  # file already exists
	return True


def version_file(filepath):
	padding = 4

	dirpath, filename = os.path.split(filepath)
	base, ext = os.path.splitext(filename)
	searchpath = os.path.join(dirpath, "*")

	files = glob.glob(searchpath)
	versions = []

	for f in files:
		tmpname = os.path.basename(f)
		if re.match(base+"[0-9]{%d}"%padding+ext, tmpname):
			versions.append(tmpname)

	versions.sort()
	version_num = 0

	if len(versions) > 0:
		latest = versions[-1]
		latest_name = os.path.splitext(latest)[0]
		idx = len(latest_name) - padding
		num_str = latest_name[idx:]
		version_num = int(num_str)+1

	return os.path.join(dirpath, base+str(version_num).zfill(padding)+ext)


# def version_dir():
#     pass


def alphanumeric(name):
	seq = []
	for char in name:
		if not char.isalnum():
			seq.append('_')
		else:
			seq.append(char)

	return ''.join(seq).lower()


def timestamp():
	return time.strftime("%a, %d %b %Y %I:%M:%S %p", time.localtime())


# def send_mail():
#     pass
#