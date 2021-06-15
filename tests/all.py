import unittest
from tests.test_charger import TestCharger
from tests.test_dcm import TestDCM
from tests.test_scpi import TestSCPI
from tests.test_com import TestCOM

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestDCM('test mock DCM')) # add DCM test cases
    suite.addTest(TestCharger('test charger handler')) # add charger test cases
    suite.addTest(TestSCPI('test SCPI handler')) # add SCPI test cases
    suite.addTest(TestCOM('test COM handler')) # add COM test cases
    return suite

if __name__=="__main__":
    runner = unittest.TestRunner() # create suite
    runner.run(suite()) # run suite