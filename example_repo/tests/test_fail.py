# https://github.com/malini/500lines/tree/master/ci/tests
import unittest

class TestFail(unittest.TestCase):

    def test_fail(self):
        self.fail('destined for greatness')
