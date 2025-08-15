from django.shortcuts import render
from rest_framework.views import APIView
from .models import Project
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .serializers import ProjectSerializer


class ProjectTemplateView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "projects_list.html"


    def get(self, request):
        projects_qs = Project.objects.prefetch_related("dev").all()
        data = ProjectSerializer(projects_qs, many=True, context={"request": request}).data  # 👈 add context
        return Response({"projects": data})
    




