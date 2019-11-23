"""
URL mapping for the all local apps.
"""


from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Default redirect to postcodes_app
    path('', include('postcodes_app.urls')),
]
