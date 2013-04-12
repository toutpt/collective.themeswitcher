Introduction
============

This addon provide a browser view @@themeswitcher which apply on the root
and let you override the theme which is used on all theme technologies of Plone.

This addon is intended for integrators.

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


Switcher
========

This addon has been designed to easily support new switcher. At the moment
the only switcher that is implemented is the "mobile switcher"
based on user agent from http://detectmobilebrowsers.com/ (python version).

Some ideas on switcher that could be easily done:

* switch on domain
* switch on protocol (http / https)
* switch on role
* switch on path
* switch on device (mobile, tablet, desktop)
* switch on a cookie value

How to use
==========

You just have to configure in portal_registry which switcher you want to use
and configure it.

To use a specific diazo theme you have to copy it's settings to switcher
registry.

For example let say you want to use plonetheme.mobile only for a mobile
you have to add a registry.xml with::


  <record name="collective.themeswitcher.theme.mobile">
    <field type="plone.registry.field.ASCIILine">
        <title>Mobile theme</title>
    </field>
    <value>plonetheme.mobile</value>
  </record>
  <record name="collective.themeswitcher.switcher">
    <field type="plone.registry.field.TextLine">
        <title>Theme switcher</title>
        <description>The named switcher that will be used</description>
    </field>
    <value>themeswitcher_mobile</value>
  </record>
  <record name="switcher.absolutePrefix" interface="plone.app.theming.interfaces.IThemeSettings" field="absolutePrefix">
    <field type="plone.registry.field.TextLine">
      <description>convert_relative_url</description>
      <required>False</required>
      <title>absolute_url_prefix</title>
    </field>
    <value>/++theme++plonetheme.mobile</value>
  </record>
  <record name="switcher.currentTheme" interface="plone.app.theming.interfaces.IThemeSettings" field="currentTheme">
    <field type="plone.registry.field.TextLine">
      <description>current_theme_description</description>
      <title>current_theme</title>
    </field>
    <value>plonetheme.mobile</value>
  </record>
  <record name="switcher.doctype" interface="plone.app.theming.interfaces.IThemeSettings" field="doctype">
    <field type="plone.registry.field.ASCIILine">
      <default></default>
      <description>doctype_description</description>
      <required>False</required>
      <title>doctype</title>
    </field>
    <value>&lt;!DOCTYPE html&gt;</value>
  </record>
  <record name="switcher.enabled" interface="plone.app.theming.interfaces.IThemeSettings" field="enabled">
    <field type="plone.registry.field.Bool">
      <default>False</default>
      <description>enable_theme_globally</description>
      <title>enabled</title>
    </field>
    <value>True</value>
  </record>
  <record name="switcher.hostnameBlacklist" interface="plone.app.theming.interfaces.IThemeSettings" field="hostnameBlacklist">
    <field type="plone.registry.field.List">
      <default>
        <element>127.0.0.1</element>
      </default>
      <description>hostname_blacklist_description</description>
      <required>False</required>
      <title>hostname_blacklist</title>
      <value_type type="plone.registry.field.TextLine"/>
    </field>
    <value>
      <element>127.0.0.1</element>
    </value>
  </record>
  <record name="switcher.parameterExpressions" interface="plone.app.theming.interfaces.IThemeSettings" field="parameterExpressions">
    <field type="plone.registry.field.Dict">
      <default/>
      <description>parameter_expressions_description</description>
      <key_type type="plone.registry.field.ASCIILine"/>
      <required>False</required>
      <title>parameter_expressions</title>
      <value_type type="plone.registry.field.ASCIILine"/>
    </field>
    <value>
      <element key="ajax_load">python: request.form.get('ajax_load')</element>
    </value>
  </record>
  <record name="switcher.readNetwork" interface="plone.app.theming.interfaces.IThemeSettings" field="readNetwork">
    <field type="plone.registry.field.Bool">
      <default>False</default>
      <description>network_urls_allowed</description>
      <title>readNetwork</title>
    </field>
    <value>False</value>
  </record>
  <record name="switcher.rules" interface="plone.app.theming.interfaces.IThemeSettings" field="rules">
    <field type="plone.registry.field.TextLine">
      <description>rules_file_path</description>
      <required>False</required>
      <title>rules_file</title>
    </field>
    <value>/++theme++plonetheme.mobile/rules.xml</value>
  </record>


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
