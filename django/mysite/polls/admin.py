from django.contrib import admin
from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Series, Card


class SeriesAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            url(r'^(?P<pk>\d+)/export/$', self.admin_site.admin_view(self.passcode_export), name='export'),
        ]
        return my_urls + urls

    def passcode_export(self, request, pk):
        return HttpResponse('OK')


admin.site.register(Series, SeriesAdmin)
admin.site.register(Card)
