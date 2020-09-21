Birdseye - dynamic calcs documentation
======================================

This is a fork of the original **Birdseye** package and adjusted for calculation mapping purposes.

For the original package see https://github.com/alexmojaki/birdseye

For the original documentation see https://birdseye.readthedocs.io/en/latest/

What is this fork for?
----------------------

The original Birdseye package is set up more as a *static debug* tool.  It records the steps in the calculation and allows the user to navigate the code and state of the variables.

For our purposes we want to use the calculation trace as a form of documentation of specific sample calculations.  Therefore we want to be able to *publish* calculation traces to birdseye server which can be accessed by other users that want to explore these sample calculations in detail.


Key modifications in this fork
--------------------------

*   Forcing explicit use of the environment variable `BIRDSEYE_DB` to direct the output of the calculation stack to a database URL (Postgres or similar) or file (SQLite database).  This enables users to do Calculation Log trials on a local database, and then when ready to publish to the official Birdseye server, switch the `BIRDSEYE_DB`.

*   Added the concept of a **Job** to the Birdseye data and database which is set as an environment variable `BIRDSEYE_JOB`.  A **Job** links together the different function calls for one calculation or sample policy.  This allows all the calls for one calculation to be bundled together and explored more easily.  The Name set is the `BIRDSEYE_JOB` variable so that it can be given a meaningful name for users.  Various modifications to the front-end app views and templates have been made for this.

*   (WORK IN PROGRESS) Added database features so that data deletes in cascade when the **Job** is deleted.  This will allow us to more easily remove Calculation Runs posted in error.

*   Adding the concept of a call tree to show visually which functions call other functions.  Uses indentation to make the call stack hierarchy more understandable to the user.

*   Made Tracing always optional and by default OFF so that to get a trace to work you need to set the `trace_call=True` parameter on the `@eye` decorator.


Getting started
---------------

Install the package from the package Wheel file (in the *dist* folder) in the python virtual environment:

    pip install [package_name_and_version].whl

Set your environment variables so that the server knows where to look for the birdseye traces:

    export BIRDSEYE_DB=full_path_and_file_for_sqlite_database.sqlite 

Spin up the birdseye server to check all works.  From the command line:

    birdseye -p [port_number]

The Birdseye server will now be available on localhost:port_number

Now you are ready to run you first trace ... 


Your first calculation trace
----------------------------

To include functions in the calculation trace add the `@eye` decorator to each of these functions.

The tracing of runs will only run when the `trace_call` parameters is passed with `True` value.  To do this and link globally to the environment variables, use `@eye(trace_call=os.environ['BIRDSEYE_ENABLED'])`.

    import os
    from birdseye import eye
    
    ...

    @eye(trace_call=os.environ['BIRDSEYE_ENABLED'])
    def my_function_to_track():
        ...
        return something
    
When you run code, and a function with the decorator is called, AND the trace_call is True, then it will write all calls to the Birdseye Database.

Note that this can get very slow with big complex calcluations.


Environment variables
~~~~~~~~~~~~~~~~~~~~~

*   `BIRDSEYE_ENABLED` this should be set to `False` normally and only set to `True` when you want a calculation to push the trace to the Birdseye database.

*   `BIRDSEYE_DB` is either a filename (in which case it will create a SQLite database if one does not exist at this location), or is a database URL.  When pushing a calculation to the postgres server to *publish* a calculation, switch this to the Postgres URL.

*   `BIRDSEYE_JOB` is any text that you wish to use to name this particular job.  All this does is group all the function calls under this job name so that it can be viewed as a job in Birdseye.  Note that if you run the calculation more than once, then all those runs will be grouped under the same job.  If you omit this environment variable then Birdseye will try to use a timestamp for the run but this is not very reliable.


Setting environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This can be done in the terminal using the `export` command.

Alternatively in the entry point of your Python code (the main file you run), you can also set the environment variables at this time using:

    import os

    os.environ['BIRDSEYE_ENABLED'] = 'False' or 'True'
    os.environ['BIRDSEYE_DB'] = '/User/matt/junk/bird_database.sqlite'
    os.environ['BIRDSEYE_JOB'] = 'Name of my calculation job'

Make sure this happens in the first file you run otherwise you may get very strange behaviour.


To point to a Postgres database instead, put in the database URL in the `BIRDSEYE_DB` variable.


Developers
----------

See the developer documentation in the Birdseye repo for setting up your local machine - https://birdseye.readthedocs.io/en/latest/contributing.html


Packaging - we are deploying this fork using the wheel file.  To create the package:

1.  Bump up the `__version__` in the **setup.policy** file

2.  Run setuptools from the command line project folder 

        python setup.py bdist_wheel

3.  Deploy the Wheel file from the **dist** folder using

        pip install [package_name_and_version].whl
