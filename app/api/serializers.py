from rest_framework import serializers
from .models import CveModel


class CveSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    status = serializers.CharField()
    description = serializers.CharField()
    references = serializers.CharField()
    phase = serializers.CharField()
    votes = serializers.CharField()
    comments = serializers.CharField()

    class Meta:
        model = CveModel
        fields = [
            'name',
            'status',
            'description',
            'references',
            'phase',
            'votes',
            'comments'
        ]
