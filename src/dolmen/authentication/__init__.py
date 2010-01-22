from zope.i18nmessageid import MessageFactory
MF = MessageFactory('dolmen.authentication')

from dolmen.authentication.interfaces import (
    IPrincipalFolder, IPrincipal, IGroup,
    IAccountStatus, IPasswordChecker, IPasswordProtected)
from dolmen.authentication.events import (
    IUserLoggedInEvent, IUserLoggedOutEvent, UserLoginEvent, UserLogoutEvent)
