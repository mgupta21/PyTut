#!/usr/bin/python
__author__ = 'Mayank'

# Needs pytest installed in system
# sudo pip install pytest

import myprogram
import pytest
import shutil
import os


class Test_Myprogram(object):
    num_file_template = 'test_nums.template'
    num_file_tester = 'temp.txt'

    def setup(self):
        shutil.copy(Test_Myprogram.num_file_template, Test_Myprogram.num_file_tester)

    def cleanup(self):
        os.remove(Test_Myprogram.num_file_tester)

    def test_double_file_vals(self):
        myprogram.double_file_vals(Test_Myprogram.num_file_tester)
        old_vals = [int(line) for line in open(Test_Myprogram.num_file_template)]
        new_vals = [int(line) for line in open(Test_Myprogram.num_file_tester)]
        for old_val, new_val in zip(old_vals, new_vals):
            assert int(new_val) == int(old_val) * 2

    def test_doubleit(self):
        assert myprogram.doubleit(10) == 20

    def test_doubleit_type(self):
        with pytest.raises(TypeError):
            myprogram.doubleit('hi')
