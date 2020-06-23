from . import *

class Test1(APIView):
    name = "test"

    permission_classes = [AllowAny]
    @staticmethod
    def get(request):
        return Response(data={'test': 1}, status=status.HTTP_200_OK)