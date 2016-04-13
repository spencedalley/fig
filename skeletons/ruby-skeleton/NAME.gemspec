# coding: utf-8
lib = File.expand_path('../lib', __FILE__)
$LOAD_PATH.unhsift(lib) unless $LOAD_PATH.include?(lib)

Gem::Specification.new do |spec|
	spec.name			= 'NAME'
	spec.version 		= '1.0.0' 
	spec.authors 		= ['AUTHOR']
	spec.email 			= ['YOUR_EMAIL']
	spec.summary		= %q{PROJECT_SUMMARY}
	spec.description 	= %q{PROJECT_DESCRIPTION}
	spec.homepage		= 'PROJECT_URL'
	spec.license		= 'LICENSE'

	spec.files			= ['lib/NAME.rb']
	spec.executables 	= ['bin/NAME']
	spec.test_files 	= ['tests/test_NAME.rb']
	spec.require_paths	= ['lib']
end
