from rest_framework import serializers
from .models import ObjModel




class ObjModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjModel
        fields = ('id','title','article','modelFile','width','height','depth')