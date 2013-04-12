import unittest2 as unittest
from collective.themeswitcher.tests import base


class TestSetup(base.IntegrationTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def test_registry(self):
        registry = self.portal.portal_registry
        keys = ('theme.mobile', 'switcher', 'rules', 'absolutePrefix',
                'currentTheme', 'doctype', 'enabled', 'readNetwork',
                'parameterExpressions', 'hostnameBlacklist')
        prefix = 'collective.themeswitcher'
        marker = object()
        for key in keys:
            rkey = '.'.join((prefix, key))
            value = registry.get(rkey, marker)
            self.assertNotEqual(value, marker)

    def test_monkeypatch(self):
        self.assertEqual(self.portal.portal_skins.getDefaultSkin.__module__,
                         'collective.themeswitcher.SkinsTool')
        from plone.app.theming.transform import ThemeTransform
        self.assertEqual(ThemeTransform.getSettings.__module__,
                         'collective.themeswitcher.ThemeTransform')

    def test_upgrades(self):
        profile = 'collective.themeswitcher:default'
        setup = self.portal.portal_setup
        upgrades = setup.listUpgrades(profile, show_old=True)
        self.assertTrue(len(upgrades) > 0)
        for upgrade in upgrades:
            upgrade['step'].doStep(setup)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
