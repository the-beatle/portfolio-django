from contact.models import Contact
from contact.serializers import ContactSerializer
from rest_framework import routers, serializers, viewsets


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer