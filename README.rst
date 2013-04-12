Introduction
============

This addon provide a browser view @@themeswitcher which apply on the root
and let you override the theme which is used on all theme technologies of Plone.

This addon is intended for integrators.

How to use
==========

TODO;

Plone Theming stack
===================

portal_skins
------------

From CMF this is the most old piece. 

This one is monkeypatched.

browser_layer
-------------

from Zope3, this is the modern way to create and override views and so
"viewpagetemplatefile".

This one is already set by plone.theme on the portal_skins.

diazo
-----

The last technology it happens after the rendering of the page to make xslt
transform on the Plone rendered page.

This one is monkeypatched.

How to install
==============

This addon can be installed has any other addons. please follow official
documentation_

Credits
=======

Companies
---------

* `Planet Makina Corpus <http://www.makina-corpus.org>`_
* `Contact Makina Corpus <mailto:python@makina-corpus.org>`_

People
------

- JeanMichel FRANCOIS aka toutpt <toutpt@gmail.com>

.. _documentation: http://plone.org/documentation/kb/installing-add-ons-quick-how-to
