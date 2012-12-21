# -*- coding: utf-8 -*-
import io
import os
from os.path import dirname, join, isdir
import shutil
from StringIO import StringIO
import sys

import pytest

from clay import Clay
from clay.helpers import make_dirs, create_file


HTTP_OK = 200
HTTP_NOT_FOUND = 404
TESTS = dirname(__file__)
SOURCE_DIR = join(TESTS, 'source')
BUILD_DIR = join(TESTS, 'build')


@pytest.fixture(scope="module")
def c():
    return Clay(TESTS)


@pytest.fixture(scope="module")
def t(c):
    return c.get_test_client()


def get_source_path(path):
    return join(SOURCE_DIR, path)


def get_build_path(path):
    return join(BUILD_DIR, path)


def read_content(path, encoding='utf8'):
    with io.open(path, 'r', encoding=encoding) as f:
        return f.read().encode(encoding)


def remove_file(path):
    try:
        os.remove(path)
    except OSError:
        pass


def remove_dir(path):
    try:
        shutil.rmtree(path)
    except OSError:
        pass


def execute_and_read_stdout(f):
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    f()
    sys.stdout = old_stdout
    mystdout.seek(0)
    return mystdout.read()

