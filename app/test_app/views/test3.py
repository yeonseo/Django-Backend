from . import *

class Test3(APIView):
    name = "test3"

    permission_classes = [AllowAny]
    @staticmethod
    def get(request):
        return Response(data={'test': 3}, status=status.HTTP_200_OK)