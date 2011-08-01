# -*- coding: utf-8 -*-

from zope.component.interfaces import IObjectEvent, ObjectEvent
from zope.interface import implements, Interface, Attribute, moduleProvides


class IUserEvent(IObjectEvent):
    """A user-centric event.
    """


class IUserLoggedInEvent(IUserEvent):
    """An event trigged when a user logs in.
    """


class IUserLoggedOutEvent(IUserEvent):
    """An event trigged when a user logs out.
    """


class UserLoginEvent(IUserEvent):
    """A basic implementation of an IUserLoggedInEvent.
    """
    implements(IUserLoggedInEvent)


class UserLogoutEvent(IUserEvent):
    """A basic implementation of an IUserLoggedOutEvent.
    """
    implements(IUserLoggedOutEvent)


class IAuthenticationEvents(Interface):
    """This interface describes and exposes the meaningful events
    descriptions and components of the authentication module.
    """
    IUserEvent = Attribute(
        "IObjectEvent extending event.")

    IUserLoggedInEvent = Attribute(
        "IUserEvent extending event: a user has logged in.")

    UserLoginEvent = Attribute(
        "An IUserLoggedInEvent implementation.")

    IUserLoggedOutEvent = Attribute(
        "IUserEvent extending event: a user has logged out.")

    UserLogoutEvent = Attribute(
        "An IUserLoggedOutEvent implementation.")


moduleProvides(IAuthenticationEvents)
__all__ = list(IAuthenticationEvents)
