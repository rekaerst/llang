#!/usr/bin/python3
import re
import subprocess
import unittest
import llang
from tests.common import *

excepted = ['let', 'stdout', '"enter your name:"', ';', 'let',
            'age', ':', 'int', 'stdin', ';', 'if', '(', 'less',
            'age', '18', ')', '(', 'let', 'stdout',
            '"You are not allowed to view this content. Please go."', ')']


class TestCommandLine(unittest.TestCase):
    def test_no_input_file(self):
        message("running llang.main([])")
        self.assertEqual(llang.main([]), 1, "no input file: llang should return 1")

    def test_no_input_file_diagnosis(self):
        message("running ./llang.py")
        process_stdout = subprocess.run(['./llang.py'], stdout=subprocess.PIPE).stdout.decode("utf-8")
        self.assertEqual(sub_ansi_escape(process_stdout), "llang: fatal error: no input file\n")


if __name__ == "__main__":
    unittest.main()
