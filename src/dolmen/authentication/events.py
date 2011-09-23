# -*- coding: utf-8 -*-

from zope.component.interfaces import IObjectEvent, ObjectEvent
from zope.interface import implements, Interface, Attribute, moduleProvides


class IUserEvent(IObjectEvent):
    """A user-centric event.
    """


class IUserRegisteredEvent(IUserEvent):
    """A user successfully completed the registration process.
    """


class IUserJoinedGroupEvent(IUserEvent):
    """A user joined a new group
    """
    group = Attribute('group joined by user')


class IUserLeftGroupEvent(IUserEvent):
    """A user left a group
    """
    group = Attribute('group left by user')


class IUserLoggedInEvent(IUserEvent):
    """An event trigged when a user logs in.
    """


class IUserLoggedOutEvent(IUserEvent):
    """An event trigged when a user logs out.
    """


class UserRegisteredEvent(ObjectEvent):
    """A basic implementation of an IUserRegisteredEvent.
    """
    implements(IUserRegisteredEvent)


class UserJoinedGroupEvent(ObjectEvent):
    """A basic implementation of an IUserJoinedGroupEvent.
    """
    implements(IUserJoinedGroupEvent)

    def __init__(self, user, group):
        super(UserJoinedGroupEvent, self).__init__(user)
        self.group = group


class UserLeftGroupEvent(ObjectEvent):
    """A basic implementation of an IUserLeftGroupEvent.
    """
    implements(IUserLeftGroupEvent)

    def __init__(self, user, group):
        super(UserLeftGroupEvent, self).__init__(user)
        self.group = group


class UserLoginEvent(ObjectEvent):
    """A basic implementation of an IUserLoggedInEvent.
    """
    implements(IUserLoggedInEvent)


class UserLogoutEvent(ObjectEvent):
    """A basic implementation of an IUserLoggedOutEvent.
    """
    implements(IUserLoggedOutEvent)


class IAuthenticationEvents(Interface):
    """This interface describes and exposes the meaningful events
    descriptions and components of the authentication module.
    """
    IUserEvent = Attribute(
        "IObjectEvent extending event.")

    IUserRegisteredEvent = Attribute(
        "IUserEvent extending event: a user registered successfully.")

    UserRegisteredEvent = Attribute(
        "An IUserRegisteredEvent implementation.")

    IUserJoinedGroupEvent = Attribute(IUserJoinedGroupEvent.__doc__)
    
    UserJoinedGroupEvent = Attribute(UserJoinedGroupEvent.__doc__)

    IUserLeftGroupEvent = Attribute(IUserLeftGroupEvent.__doc__)
    
    UserLeftGroupEvent = Attribute(UserLeftGroupEvent.__doc__)

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
