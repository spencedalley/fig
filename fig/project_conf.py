import os

def python_project(project_path, project_name):
	os.rename(project_path+'/NAME', project_path+'/'+project_name)
	os.rename(project_path+'/tests/NAME_tests.py',
			  project_path+'/tests/%s_tests.py' % project_name)

	# change the file contents
	test_contents = open(project_path+'/tests/%s_tests.py' % project_name).read()
	test_contents = test_contents.replace('NAME', project_name)

	with open(project_path+'/tests/%s_tests.py' % project_name, 'w') as f:
		f.write(test_contents)

	setup_contents = open(project_path+'/setup.py').read()
	setup_contents = setup_contents.replace('NAME', project_name)

	with open(project_path+'/setup.py', 'w') as f:
		f.write(setup_contents)

	return

def ruby_project(project_path, project_name):
	os.rename(project_path+'/bin/NAME', project_path+'/bin/%s' % project_name)
	os.rename(project_path+'/lib/NAME', project_path+'/lib/%s' % project_name)
	os.rename(project_path+'/lib/NAME.rb', project_path+'/lib/%s.rb' % project_name)
	os.rename(project_path+'/NAME.gemspec', project_path+'/%s.gemspec' % project_name)
	os.rename(project_path+'/tests/test_NAME.rb', project_path+'/tests/test_%s.rb' % project_name)

	test_contents = open(project_path+'/tests/test_%s.rb' % project_name).read()
	test_contents = test_contents.replace('NAME', project_name)

	# change file contents
	with open(project_path+'/tests/test_%s.rb' % project_name, 'w') as f:
		f.write(test_contents)

	gemspec = open(project_path+'/%s.gemspec' % project_name).read()
	gemspec = gemspec.replace('NAME', project_name)

	with open(project_path+'/%s.gemspec' % project_name, 'w') as f:
		f.write(gemspec)

	return

def c_project(project_path, project_name):
    os.rename(project_path+'/src/NAME.c', project_path+'/src/%s.c' % project_name)
    os.rename(project_path+'/src/NAME.h', project_path+'/src/%s.h' % project_name)
    os.rename(project_path+'/tests/lib_tests.c', project_path+'/tests/%s_tests.c' % project_name)

    test_contents = open(project_path+'/tests/%s_tests.c' % project_name).read()
    test_contents = test_contents.replace('NAME', project_name)

    with open(project_path+'/tests/%s_tests.c' % project_name, 'w') as f:
        f.write(test_contents)

    src_contents = open(project_path+'/src/%s.h' % project_name).read()
    src_contents = src_contents.replace('NAME', project_name)

    with open(project_path+'/src/%s.h' % project_name, 'w') as f:
        f.write(src_contents)

    makefile = open(project_path+'/Makefile').read()
    makefile = makefile.replace('NAME', project_name)

    with open(project_path+'/Makefile', 'w') as f:
        f.write(makefile)

    return
