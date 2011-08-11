#!/bin/bash
virtualenv --no-site-packages ve && \
source ve/bin/activate && \
nosetests --with-doctest --with-coverage --cover-package=smpp --with-xunit && \
coverage xml smpp/* && \
pep8 --repeat --exclude '0*.py' smpp > pep8.txt
deactivate
