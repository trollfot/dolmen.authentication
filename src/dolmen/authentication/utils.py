# -*- coding: utf-8 -*-

from zope.security.management import queryInteraction
from dolmen.authentication import IPrincipal


def query_active_principal():
    interaction = queryInteraction()
    if interaction is not None and interaction.participations:
        principal = interaction.participations[0].principal
        if IPrincipal.providedBy(principal):
            return principal
    return None
