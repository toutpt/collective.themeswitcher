from zope import component
from zope.globalrequest import getRequest


def getDefaultSkin(self):
    """this is a monkey patch to let the CMF skin switchable"""
    if hasattr(self, "REQUEST"):
        request = self.REQUEST
    else:
        request = getRequest()

    switcher = component.getMultiAdapter((self, request),
                                         name=u"themeswitcher")
    return switcher.getDefaultSkin(self._old_getDefaultSkin)
