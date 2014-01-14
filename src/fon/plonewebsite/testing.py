from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class FonplonewebsiteLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import fon.plonewebsite
        xmlconfig.file(
            'configure.zcml',
            fon.plonewebsite,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'fon.plonewebsite:default')

FON_PLONEWEBSITE_FIXTURE = FonplonewebsiteLayer()
FON_PLONEWEBSITE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(FON_PLONEWEBSITE_FIXTURE,),
    name="FonplonewebsiteLayer:Integration"
)
FON_PLONEWEBSITE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FON_PLONEWEBSITE_FIXTURE, z2.ZSERVER_FIXTURE),
    name="FonplonewebsiteLayer:Functional"
)
