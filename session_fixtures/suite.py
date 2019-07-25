import unittest
from session_fixtures.unit_test1 import Class_1
from session_fixtures.unit_test2 import Class_2

cl1 = unittest.TestLoader().loadTestsFromTestCase(Class_1)
cl2 = unittest.TestLoader().loadTestsFromTestCase(Class_2)

sanity_suite = unittest.TestSuite([cl1, cl2])
unittest.TextTestRunner().run(sanity_suite)
