#! /usr/bin/env python3

import git
import os
import shutil
import sys

from fig import project_conf

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))[:-4]

PATHS = PATHS = {
	'c': ROOT_PATH + '/skeletons/c-skeleton',
	'python': ROOT_PATH + '/skeletons/python-skeleton',
	'ruby': ROOT_PATH + '/skeletons/ruby-skeleton',
}

def main():
	if len(sys.argv) < 3:
		print('USAGE: app.py <language> <project_name>')
		sys.exit(0)

	language = sys.argv[1]
	project_name = sys.argv[2]
	project_path = os.getcwd() + '/' + project_name
	project_skeleton = PATHS.get(language, None)

	if project_skeleton == None:
		print('Invalid language specified. Currently supported languages are:')
		for key in PATHS.keys():
			print('- %s' % key)
		exit(0)

	if os.path.isdir(project_path) == True:
		print('There is already a a directory with the project name specified in the current directory')
		print('Choose a different name for you project.')
		sys.exit(0)

	# copy over the skeleton and do version control
	shutil.copytree(project_skeleton, project_path)
	git.Repo.init(project_path)

	if language == 'python':
		project_conf.python_project(project_path, project_name)
	elif language == 'ruby':
		project_conf.ruby_project(project_path, project_name)
	elif language == 'c':
		project_conf.c_project(project_path, project_name)
	else:
		pass

if __name__ == '__main__':
	main()
