from ZPublisher.tests.testPublish import Request as BaseRequest


class FakeAcquisition(object):
    def __init__(self):
        self.aq_explicit = None


class FakeContext(object):

    def __init__(self):
        self.id = "myid"
        self.title = "a title"
        self.description = "a description"
        self.creators = ["myself"]
        self.date = "a date"
        self.aq_inner = FakeAcquisition()
        self.aq_inner.aq_explicit = self
        self._modified = "a modification date"
        self.remoteUrl = ''  # fake Link
        self.portal_type = 'Document'
        self.text = "Text"

    def getId(self):
        return self.id

    def Title(self):
        return self.title

    def Creators(self):
        return self.creators

    def Creator(self):
        return self.creators[0]

    def Description(self):
        return self.description

    def Date(self):
        return self.date

    def modified(self):
        return self._modified

    def getPhysicalPath(self):
        return ('/', 'a', 'not', 'existing', 'path')

    def absolute_url(self):
        return "http://nohost.com/" + self.id


def setHeader(header, value):
    pass


class Request(BaseRequest):
    """Request with set item support"""

    def __init__(self):
        BaseRequest.__init__(self)
        self.content = {}
        setattr(self.response, 'setHeader', setHeader)  # patch for tests

    def __setitem__(self, name, value):
        self.content[name] = value

    def get(self, a, b=''):
        return self.content.get(a, b)

marker = object()


class FakeRegistry(object):
    def __init__(self):
        self.registry = {}

    def get(self, key, default=marker):
        if default != marker:
            return self.registry.get(key, default)
        return self.registry[key]


class FakeSwitcher(object):
    def __init__(self):
        self.useOld = False

    def getDefaultSkin(self, old):
        if self.useOld:
            return old()
        return 'defaultskin'

    def getSettings(self, old):
        if self.useOld:
            return old()
        return 'settings'


class FakePortalSkins(object):
    def __init__(self):
        self.selections = []

    def getSkinSelections(self):
        return self.selections
