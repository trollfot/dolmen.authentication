# -*- coding: utf-8 -*-

import grokcore.component as grok
from zope.location.interfaces import ILocation
from dolmen.authentication import IPrincipal
from zope.pluggableauth.interfaces import IPrincipalInfo


class PrincipalInfo(grok.Adapter):
    grok.context(IPrincipal)
    grok.implements(ILocation)
    grok.provides(IPrincipalInfo)
    
    def __init__(self, context):
        self.id = context.id
        self.title = context.title
        self.description = context.description
        self.credentialsPlugin = None
        self.authenticatorPlugin = None
        self.__name__ = context.__name__
        self.__parent__ = context.__parent__
