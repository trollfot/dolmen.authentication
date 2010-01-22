# -*- coding: utf-8 -*-

import zope.schema
import zope.security.interfaces
from zope.interface import Interface, Attribute
from dolmen.authentication import MF as _


class IPrincipalFolder(Interface):
    contains('.IPrincipal')
    
    def getUser(id):
        """Returns an IPrincipal with the given id.
        """


class IPrincipal(zope.security.interfaces.IGroupAwarePrincipal):
    """Principals are easily identifiable entities that interact
    with the content. Commonly, a principal is a user or a group.
    """
    id = schema.ASCIILine(
        title = _(u'Login'),
        required = True
        )

    title = schema.TextLine(
        title = _(u'Full name'),
        description = _(u'Enter your full name.'),
        required = True,
        )


class IGroup(IPrincipal):
    """Groups are principals that are a grouping of other principals.
    Groups can be parts of groups, for a logical nesting.
    """


class IAccountStatus(Interface):
    """An interface managing a simple account status.
    """
    status = Attribute("Status of the account.")
    
    def check():
        """Returns a boolean. True allows the normal user login.
        False will disable the account and act like a failed login.
        """


class IPasswordChecker(Interface):
    """This interface defines items that can challenge a
    given value against a stored password value.
    """
    def checkPassword(password):
        """Challenges the input password with the stored one.
        Returns True if the passwords match, False otherwise.
        """