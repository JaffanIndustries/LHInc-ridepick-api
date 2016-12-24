import externals
from rest_framework.decorators import api_view
from rest_framework.response import Response
from serializers import estimateSerializer

# Create your views here.
@api_view(['GET'])
def get_estimates(request):
    start_latitude=37.770,
    start_longitude=-122.411,
    end_latitude=37.791,
    end_longitude=-122.405,
    seat_count=2
    estimates = externals.get_all_estimates(start_lat=start_latitude,
                                            start_lon=start_longitude,
                                            end_lat=end_latitude,
                                            end_lon=end_longitude,
                                            seat=seat_count)
    serializer = estimateSerializer(estimates, many=True)
    return Response(serializer.data)