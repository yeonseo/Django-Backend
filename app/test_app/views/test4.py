from . import *

class Test4(APIView):
    name = "test4"

    permission_classes = [AllowAny]
    @staticmethod
    def get(request):
        return Response(data={'test': 4}, status=status.HTTP_204_NO_CONTENT)