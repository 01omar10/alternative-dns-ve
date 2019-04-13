# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField

class Member(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    last_location = models.PointField(null=True, blank=True)
    last_ip = models.GenericIPAddressField(null=True, blank=True)
    resolver_cache = JSONField(null=True, blank=True)
