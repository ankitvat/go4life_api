from rest_framework import serializers
from .models import Lead
from . import models

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('id', 'name', 'phone', 'email', 'created_on')
