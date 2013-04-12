from plone.app.testing import *
import collective.themeswitcher


FIXTURE = PloneWithPackageLayer(
    zcml_filename="configure.zcml",
    zcml_package=collective.themeswitcher,
    additional_z2_products=[],
    gs_profile_id='collective.themeswitcher:default',
    name="collective.themeswitcher:FIXTURE"
)

INTEGRATION = IntegrationTesting(
    bases=(FIXTURE,), name="collective.themeswitcher:Integration"
)

FUNCTIONAL = FunctionalTesting(
    bases=(FIXTURE,), name="collective.themeswitcher:Functional"
)
