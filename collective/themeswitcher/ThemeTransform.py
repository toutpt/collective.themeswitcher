from zope import component
from plone.app.theming.utils import findContext


def getSettings(self):
    """Return a setting object. the setting to support cache must have a
    persistent __registry__ attributes, this is where plone.app.theming
    store it's cache"""
    context = findContext(self.request)
    switcher = component.getMultiAdapter((context, self.request),
                                         name=u"themeswitcher")

    return switcher.getSettings(self._old_getSettings)
