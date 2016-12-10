"""hacksociety URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from gov_api.models import Entry
from rest_framework import routers, serializers, viewsets
from rest_framework.serializers import ModelSerializer
from rest_framework_bulk.routes import BulkRouter
from rest_framework_bulk.generics import BulkModelViewSet
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)


class BulkEntrySerializer(BulkSerializerMixin, ModelSerializer):
    class Meta(object):
        model = Entry
        # only necessary in DRF3
        list_serializer_class = BulkListSerializer
        fields = ('id',)


class BulkEntryView(ListBulkCreateUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = BulkEntrySerializer


# Serializers define the API representation.
class EntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entry
        # fields = ('cod_unic_candidat', 'sex', 'medie')
        fields = '__all__'


# ViewSets define the view behavior.
class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryBulkViewSet(BulkModelViewSet):
    model = Entry
    queryset = Entry.objects.all()
    serializer_class = BulkEntrySerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'entries', EntryViewSet)

router_bulk = BulkRouter()
router_bulk.register(r'entries_bulk', EntryBulkViewSet, base_name='bulk')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^', include(router.urls)),
    url(r'^', include(router_bulk.urls))
]
