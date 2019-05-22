from django.db import models


class TourType(models.Model):
    HEADLINER = 'Headliner'
    DIRECT_SUPPORT = 'Direct Support'
    OPENER = 'Opener'
    TOUR_TYPES = [
        (HEADLINER, 'Headliner'),
        (DIRECT_SUPPORT, 'Direct Support'),
        (OPENER, 'Opener')
    ]
