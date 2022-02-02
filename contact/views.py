from contact.models import Contact
from contact.serializers import ContactSerializer
from rest_framework import routers, serializers, viewsets, permissions


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ['post']
    permission_classes = [permissions.AllowAny]
