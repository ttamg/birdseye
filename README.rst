Quantco birdseye
================

This is a fork of the original **Birdseye** package and adjusted for Quantco calculation mapping purposes.

For the original package see https://github.com/alexmojaki/birdseye

For the original documentation see https://birdseye.readthedocs.io/en/latest/


Modifications
-------------

We have made the following adjustments in this fork vs the original package.

Functionality
~~~~~~~~~~~~~

*  More explicit use of environment variables to log the runs and push the tracking to the same common birdseye database.

*  Added the concept of a **Job** which is set as an environment variable to link together the different function calls for one calculation or sample policy.  If not filled in it uses a broad timestamp as the job.  

Env variables
~~~~~~~~~~~~~

#. Made it an explicit requirement to set the `BIRDSEYE_DB` environment variable rather than defaulting to creating in user home directory.  This just avoids confusion and ensures we have a sensible explicit setup.

#. Added a `JOB_NAME` environment variable that can be set before running the job.  This will then set the Job to be the Job object with this name in the database.  This is useful as we can then have a job to watch one calculation run job end to end.

Database
~~~~~~~~

#. Added a `Job` table to the tracking database to enable us to bundle together calculations into one **job**.  When running a profile, it will link all the individual calls to this **job** record.  It will create this job record if it does not already exist.
   

Using in practice
-----------------

*  Explicitly use the `BIRDSEYE_DB` environment variable to direct tracking traffic to the right database.  If this is not done then anyone running it will send the tracking to a new database that is created in their personal home folder.


