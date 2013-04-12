import transaction
import unittest2 as unittest
from collective.themeswitcher import testing
from collective.themeswitcher.tests.fake import FakeContext, Request


class UnitTestCase(unittest.TestCase):

    def setUp(self):
        self.portal = FakeContext()
        self.request = Request()

        def _old_settings():
            return 'old settings'
        self._old_settings = _old_settings

        def _old_getDefaultSkin():
            return 'old default skin'
        self._old_getDefaultSkin = _old_getDefaultSkin


class IntegrationTestCase(unittest.TestCase):

    layer = testing.INTEGRATION

    def setUp(self):
        super(IntegrationTestCase, self).setUp()
        self.portal = self.layer['portal']
        self.request = self.layer['request']

        def _old_settings():
            return 'old settings'
        self._old_settings = _old_settings

        def _old_getDefaultSkin():
            return 'old default skin'
        self._old_getDefaultSkin = _old_getDefaultSkin


class FunctionalTestCase(IntegrationTestCase):

    layer = testing.FUNCTIONAL

    def setUp(self):
        #we must commit the transaction
        transaction.commit()
