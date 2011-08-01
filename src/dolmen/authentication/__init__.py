# -*- coding: utf-8 -*-

from zope.i18nmessageid import MessageFactory
MF = MessageFactory('dolmen.authentication')

from dolmen.authentication.interfaces import *
from dolmen.authentication.interfaces import IAuthenticationInterfaces

from dolmen.authentication.events import *
from dolmen.authentication.events import IAuthenticationEvents


class IAuthenticationAPI(IAuthenticationInterfaces, IAuthenticationEvents):
    """The dolmen authentication public components.
    """


from zope.interface import moduleProvides

moduleProvides(IAuthenticationAPI)
__all__ = list(IAuthenticationAPI)
