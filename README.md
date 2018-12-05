# travis-test

This is an example project demonstrating the use of Travis CI. This project was
developed for ECEN 5033 DevOps in the Cloud at CU Boulder.

This project implements a decimal to arbitrary base converter website. The Travis CI
portion of the project automatically builds, tests and deploys the website
to an AWS Elastic Beanstalk instance.

The template used for the base of the website is called 'Ava' and can be found
at https://onepagelove.com/ava. The template is released under GPLv3. This
template was modified to include forms for base conversion calculations.

The .travs.yml file instructs Travis CI on how to build and release the
website to AWS.
