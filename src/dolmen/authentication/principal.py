# -*- coding: utf-8 -*-

import grokcore.component as grok
from dolmen.authentication import IPrincipal
from zope.app.authentication.interfaces import IPrincipalInfo


class PrincipalInfo(grok.Adapter):
    grok.context(IPrincipal)
    grok.implements(IPrincipalInfo)
    
    def __init__(self, context):
        self.id = context.id
        self.title = context.title
        self.description = context.description
        self.credentialsPlugin = None
        self.authenticatorPlugin = None
 
