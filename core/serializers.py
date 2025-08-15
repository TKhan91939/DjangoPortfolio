from rest_framework import serializers
from .models import Developer, Project

class DeveloperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Developer
        fields = ["first_name", "last_name", "img"]


class ProjectSerializer(serializers.ModelSerializer):
    developers = DeveloperSerializer(many=True, read_only=True, source="dev")

    class Meta:
        model = Project
        fields = ["name", "img", "description", "link", "gist", "developers"]