# !/usr/bin/python
__author__ = 'Mayank'

# Assignment 6
# Run : py.test TestMyCustomDict
from assignment4 import MyCustomDict, MyDictError
import os
import pytest
import shutil


class TestMyCustomDict(object):
    existing_file = 'conf_file.template'
    existing_file_template = 'config_file.template'
    new_file = 'config_file_new.txt'
    bad_path = '/some/invalid/path/file.txt'

    def setup(self):
        shutil.copy(TestMyCustomDict.existing_file_template, TestMyCustomDict.existing_file)

    def cleanup(self):
        os.remove(TestMyCustomDict.new_file)

    def test_obj(self):
        c = MyCustomDict(TestMyCustomDict.existing_file)
        assert isinstance(c, MyCustomDict)
        assert isinstance(c, dict)

    def test_existing_filename(self):
        c = MyCustomDict(TestMyCustomDict.existing_file)
        assert c._filename == TestMyCustomDict.existing_file

    def test_new_filename(self):
        assert not os.path.isfile(TestMyCustomDict.new_file)
        c = MyCustomDict(TestMyCustomDict.new_file)
        assert c._filename == TestMyCustomDict.new_file
        assert os.path.isfile(TestMyCustomDict.new_file)

    def test_bad_file_path(self):
        with pytest.raises(IOError):
            MyCustomDict(TestMyCustomDict.bad_path)

    def test_read_dict(self):
        cc = MyCustomDict(TestMyCustomDict.existing_file)
        assert cc['a'] == '5'
        assert cc['b'] == '10'
        assert cc['c'] == 'this=that'

        with pytest.raises(MyDictError):
            print cc['x']

    def test_write_dict(self):
        c = MyCustomDict(TestMyCustomDict.existing_file)
        c['z'] = 'hello'
        c2 = MyCustomDict(TestMyCustomDict.existing_file)
        assert c2['z']
