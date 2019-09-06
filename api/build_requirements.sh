#! /usr/bin/env sh

# script to build requirements files
pip-compile requirements/base.in
pip-compile requirements/development.in
pip-compile requirements/test.in
