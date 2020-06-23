from . import *

class Test2(APIView):
    name = "test2"

    permission_classes = [AllowAny]
    @staticmethod
    def get(request):
        return Response(data={'test': 2}, status=status.HTTP_204_NO_CONTENT)