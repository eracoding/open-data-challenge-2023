from rest_framework.response import Response
from rest_framework.views import APIView

from api.tasks import learnFromCategory


class LearnView(APIView):
    def get(self):
        learnFromCategory.delay()
        return Response()
