# REST API Test:
* Please automate tests for the API Resource http://jsonplaceholder.typicode.com/posts
* Operation to be covered:  Create, Update, View, Delete, List
* For further details refer to: https://github.com/typicode/jsonplaceholder
* Explain your framework architecture and design considerations


# Framework architecture and design:
* Using layered architecture with configurable OOP (Python) framework which include the required test methods and utilities to run the backend tests with documented steps and simple time stamped logging mechanism.

# api-testing
API test-suite using Python (unittest, requests) 

# Files and Folders:
--------------------
* config.cfg: The test-suite configuration file.
* requirements: The test-suite python packages requirements file.
* testsuite: The test-suite folder holding test cases files and test-framework.
* testsuite/test_posts.py: The test case file for the task.
* testframework: The test-framework folder for base test case class and utilities.
* testframework/base.py: The test framework base file for test case classes and utilities.


# Requirements:
* If you don't have python use this link: https://www.python.org/download/releases/


Install Python Packages:
------------------------
Windows
```
C:\Users\a.ali\Repos\api_testing>c:\Python27\Scripts\pip.exe install requirements
```

Linux
```
python$> sudo apt-get install python-pip
python$> pip install -r requirements
```

or use local packages
```
pip install -r wheelhouse/requirements --no-index --find-links wheelhouse
```

Run the tests:
--------------
Windows
```
C:\Users\a.ali\Repos\api_testing>c:\Python27\Scripts\nosetests.exe -v testsuite --tc-file config.ini
```

Linux
```
python$> nosetests -v testsuite --with-xunitmp --nocapture --tc-file config.ini
```

See test results:
-----------------
```
C:\Users\a.ali\Repos\api_testing>c:\Python27\Scripts\nosetests.exe -v testsuite --tc-file config.ini
TestCase-1: Test case for test create post using POST /posts/.* ... ok
TestCase-2: Test case for test view post using GET /posts/{id}.* ... ok
TestCase-3: Test case for test list posts using GET /posts.* ... ok
TestCase-4: Test case for test update post using PUT /posts/{id}.* ... ok
TestCase-5: Test case for test delete post using DELETE /posts/{id}.* ... ok

----------------------------------------------------------------------
Ran 5 tests in 3.248s

OK
```
To run specific test case:
---------------------------
Windows
```
C:\Users\a.ali\Repos\api_testing>c:\Python27\Scripts\nosetests.exe -v testsuite.test_posts:TestPosts.test001_create --tc-file config.ini
TestCase-1: Test case for test create post using POST /posts/.* ... ok

----------------------------------------------------------------------
Ran 1 test in 0.819s

OK
```

See test logs open file api_testsuite.log
