from rest_framework.response import Response
from rest_framework.views import APIView

from api.networkModels import PromptModel
from api.tasks import learnFromCategory


class LearnView(APIView):
    def get(self, request, *args, **kwargs):
        learnFromCategory.delay()
        return Response()


class PredictView(APIView):
    def get(self, request, *args, **kwargs):
        response = PromptModel()
        return Response({"prediction": response.predictModel("", request.query_params['keywords'])})
