## Fig 
Fig is a command-line tool for scaffolding new Python, C/C++, and Ruby projects easily. 

### Setup: 
Running the Fig requires one of the following versions of python: 

* python 2.7
* python 3.4 or above

To install fig onto your system, download the project, cd to the project root, and run the setup.py file with the following command. 

```
$ python setup.py install 
```

This will install Fig onto your system and create a runnable script to use from the terminal for creating new project scaffolds. 

### Usage: 
Python, C/C++, and Ruby are the only languages that the scaffolding supports at the moment. 

To create a new project use the following command with yout language and project_name passed in as parameters: 

```
$ fig <language> <project_name>
```

Here's an example of running the command: 

```
$ fig python example_project
```

### Running Tests: 
All the tests for this module are located in the `tests/fig_tests.py` file. 

To run the tests, open up a terminal, cd to the root of the project, and type `nosetests`. You should get an output like the section below: 

```
$ nosetests

.....
----------------------------------------------------------------------
Ran 5 tests in 0.010s

OK
```

All tests should pass. 

## Implementation Notes: 
[Add notes]


