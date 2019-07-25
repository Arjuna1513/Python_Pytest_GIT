import unittest
from session_scope_driiver.tests_pytest import SampleTests
from session_scope_driiver.tests_pytest1 import SampleTests1

cl1 = unittest.TestLoader().loadTestsFromTestCase(SampleTests)
cl2 = unittest.TestLoader().loadTestsFromTestCase(SampleTests1)

sanity_suite = unittest.TestSuite([cl1, cl2])
unittest.TextTestRunner().run(sanity_suite)
