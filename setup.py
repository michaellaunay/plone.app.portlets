from setuptools import find_packages
from setuptools import setup


version = "5.0.0a6.dev0"

setup(
    name="plone.app.portlets",
    version=version,
    description="Plone integration for the basic plone.portlets package",
    long_description=open("README.rst").read() + "\n" + open("CHANGES.rst").read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: Core",
        "Framework :: Zope :: 5",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="portlets viewlets plone",
    author="Plone Foundation",
    author_email="plone-developers@lists.sourceforge.net",
    url="https://pypi.org/project/plone.app.portlets",
    license="GPL version 2",
    packages=find_packages(),
    namespace_packages=["plone", "plone.app"],
    include_package_data=True,
    zip_safe=False,
    extras_require=dict(
        test=[
            "plone.app.testing",
        ],
    ),
    install_requires=[
        "setuptools",
        "five.customerize",
        "plone.autoform",
        "plone.i18n",
        "plone.memoize",
        "plone.portlets>=1.1",
        "plone.app.i18n",
        "plone.app.vocabularies >= 2.1.15.dev0",
        "plone.app.z3cform",
        "transaction",
        "zope.annotation",
        "zope.browser",
        "zope.component",
        "zope.configuration",
        "zope.container",
        "zope.contentprovider",
        "zope.event",
        "zope.i18nmessageid",
        "zope.interface",
        "zope.lifecycleevent",
        "zope.publisher",
        "zope.schema",
        "zope.site",
        "zope.traversing",
        "Products.CMFCore",
        "Products.CMFDynamicViewFTI",
        "Products.GenericSetup >= 2.0.dev0",
        "Products.PluggableAuthService",
        "ZODB",
        "Acquisition",
        "DateTime",
        "Zope >= 5",
        "feedparser",
    ],
)
