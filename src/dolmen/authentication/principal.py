# -*- coding: utf-8 -*-

import grokcore.component as grok
from dolmen.authentication import IPrincipal
from zope.publisher.interfaces import IRequest
from zope.security.interfaces import IGroupClosureAwarePrincipal
from zope.pluggableauth.interfaces import (
    IPrincipalInfo, IAuthenticatedPrincipalFactory, IFoundPrincipalFactory)


class PrincipalInfo(grok.Adapter):
    grok.context(IPrincipal)
    grok.implements(IPrincipalInfo)
    
    def __init__(self, context):
        self.id = context.id
        self.title = context.title
        self.description = context.description
        self.credentialsPlugin = None
        self.authenticatorPlugin = None


class AuthenticatedPrincipalFactory(grok.MultiAdapter):
    grok.adapts(IPrincipal, IRequest)
    grok.provides(IAuthenticatedPrincipalFactory)

    
class FoundPrincipalFactory(grok.MultiAdapter):
    grok.adapts(IPrincipal, IRequest)
    grok.provides(IFoundPrincipalFactory)
