from fon.plonewebsite.testing import FON_PLONEWEBSITE_FUNCTIONAL_TESTING
from plone.testing import layered
import robotsuite
import unittest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(robotsuite.RobotTestSuite("robot_test.robot"),
                layer=FON_PLONEWEBSITE_FUNCTIONAL_TESTING)
    ])
    return suite
