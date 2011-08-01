# -*- coding: utf-8 -*-

import zope.schema
import zope.security.interfaces
from cromlech.container.interfaces import IContainer
from cromlech.container.constraints import contains
from dolmen.authentication import MF as _
from zope.interface import (
    Invalid, Interface, Attribute, moduleProvides, invariant)


class IPrincipalFolder(IContainer):
    contains('.IPrincipal')


class IPrincipal(zope.security.interfaces.IGroupAwarePrincipal):
    """Principals are easily identifiable entities that interact
    with the content. Commonly, a principal is a user or a group.
    """
    id = zope.schema.ASCIILine(
        title=_(u'Unique principal identifier.'),
        required=True,
        )

    title = zope.schema.TextLine(
        title=_(u'Principal name'),
        description=_(u'Descriptive name of the principal.'),
        required=True,
        )


class IGroup(zope.security.interfaces.IGroup, IPrincipal):
    """A group of principals.
    """


class IAccount(Interface):
    """An interface managing a simple account status.
    """
    status = Attribute("Status of the account.")

    def activate():
        """Activate the account.
        """

    def deactivate():
        """Deactivate user.
        """

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


class IPasswordProtected(Interface):
    """This interface defines items protected by a password.
    """
    password = Attribute("A password.")


class IChangePassword(IPasswordProtected):
    """This interface defines a convenient way to change a password,
    including a double check.
    """
    password = zope.schema.Password(
        title=_(u"Password"),
        description=_(u"Type a password."),
        required=True)

    verify_password = zope.schema.Password(
        title=_(u"Password checking"),
        description=_(u"Retype the password."),
        required=True)

    password.order = 25
    verify_password.order = 26

    @invariant
    def check_pass(data):
        if data.password != data.verify_password:
            raise Invalid(_(u"Mismatching passwords."))


class IAuthenticationInterfaces(Interface):
    """This interface describes and exposes the meaningful interfaces
    of the authentication module.
    """
    IPrincipalFolder = Attribute(
        "A container specialized in storing principal representations.")

    IPrincipal = Attribute(
        "A principal representation, directly inheriting from "
        "zope.security IPrincipal, but redefining several fields "
        "for a user-friendly form display.")

    IGroup = Attribute(
        "A logical grouping of principals. This component is an "
        "IPrincipal itself.")

    IAccount = Attribute(
        "Abstraction component allowing to check the status of a principal.")

    IPasswordChecker = Attribute(
        "Abstraction component in charge of resolving a principal's "
        "credentials.")

    IChangePassword = Attribute(
        "Convenient schema to provide a 'double check' password change.")

    IPasswordProtected = Attribute(
        "This interface defines any component protected by a password")


moduleProvides(IAuthenticationInterfaces)
__all__ = list(IAuthenticationInterfaces)
