from .serializers import InputSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def calc_npv(k, year, start_year=2020):
    '''Расчет NPV на каждый год'''
    n = year - start_year
    income = [1000, 1000, 500, 500, 1000, 1000,
              1000, 1000, 1000, 1000, 1000, 1000, 1000,
              1000, 1000, 1000, 1000, 1000, 1000, 1000,
              1000, 1000, 1000, 1000, 1000, 1000, 1000,
              1000, 1000, 1000, 1000]

    if n == 0:
        return round((income[n]/(1+k)**(n+1)), 2)
    return round((income[n]/(1+k)**(n+1) + calc_npv(k, year-1)), 2)


@api_view(['POST'])
def index(request):
    if request.method == 'POST':
        serializer = InputSerializer(data=request.data)

        if serializer.is_valid():
            year = serializer.validated_data['year']
            coeff = serializer.validated_data['coeff']
            result = calc_npv(coeff, year)
            response = {'result': result}
            return Response(response, status=status.HTTP_200_OK)
