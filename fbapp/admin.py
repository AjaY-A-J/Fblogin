# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import log,detail,sign
from django.contrib import admin

# Register your models here.
admin.site.register(log)

admin.site.register(detail)

admin.site.register(sign)