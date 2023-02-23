from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView

from django.http import JsonResponse

from coreApp.ApiPaginacion import PaginacionAPI

from datetime import datetime
import re

from .serializers import CveSerializer
from .models import CveModel


from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


testDateEnd = datetime.now()
testDateStart = datetime.fromtimestamp(testDateEnd.timestamp() - 31536000)


class ApiGetByNameView(generics.ListAPIView):
    """
    Queries by vendor, product_id and returns cve found.
    """
    pagination_class = PaginacionAPI
    serializer_class = CveSerializer

    test_param = openapi.Parameter('q', openapi.IN_QUERY, description="vendor_product_version", default="microsoft_windows_10_1607",type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[test_param], pagination_class=None, operation_description="GET /search?=vendor_product_version")
    def get(self, request, format="json"):
        try:
            stringQuery = request.GET['q'].replace("_", " ")

            if stringQuery != "":
                query = CveModel.objects.filter(description__icontains=stringQuery).order_by("-id")
                serializer = self.serializer_class(query, many=True)

                page = self.paginate_queryset(serializer.data)
                return JsonResponse(self.get_paginated_response(page), safe=False)

            else:
                return Response({"error": "Query is empty."}, status=400)

        except Exception as e:
            print(e.with_traceback)
            return Response({"error": "You need made a query: '?q=queryString'"}, status=400)



# class SearchCveIdApiView(generics.ListAPIView):
class SearchCveIdApiView(APIView):
    """
    Search by CVEID,\n?q=PARAMETER
    """
    pagination_class = None
    serializer_class = CveSerializer

    test_param = openapi.Parameter('id', openapi.IN_QUERY, description="CVE-YYYY-[XXXX|XXXXX|XXXXXXX]", default="CVE-2023-24580",type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[test_param])
    def get(self, request, format="json"):
        try:
            cveid = request.GET["id"]
            regex = re.search('(^cve-\d{4}-(\d{4}$|\d{5}$|\d{7}$))', cveid, flags=re.IGNORECASE)
            if regex != None:
                query = CveModel.objects.filter(name__icontains=regex.group(0).upper()).order_by('-id').values()
                serializer = CveSerializer(query, many=True)
                return JsonResponse(serializer.data, safe=False, status=200)
            else:
                return Response({"error": "Enter CVE ID with correct format."}, status=400)
        except Exception as e:
            return Response({"error": "No 'id' query was made."}, status=400)


class ByDateCvesView(generics.ListAPIView):
    """
    Get CVEs by date:\n/date?start=YYYY-MM-DD[&end=YYYY-MM-DD]
    """
    pagination_class = PaginacionAPI
    serializer_class = CveSerializer

    paramStart = openapi.Parameter('start', openapi.IN_QUERY, description="YYYY-MM-DD", default=f'{testDateStart.date()}' ,type=openapi.TYPE_STRING)
    paramEnd = openapi.Parameter('end', openapi.IN_QUERY, description="YYYY-MM-DD", default=f'{testDateEnd.date()}' ,type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[paramStart, paramEnd])
    def get(self, request, format="json"):
        try:
            start = request.GET['start']
            end = None
            endDate = None

            startDate = datetime.fromisoformat(start)
            try:
                end = request.GET['end']
                endDate = datetime.fromisoformat(end)
            except:
                pass

            if endDate != None:
                if startDate.timestamp() <= endDate.timestamp():

                    query = CveModel.objects.all()

                    startQuery = query.filter(name__icontains=f'cve-{startDate.year}').values()
                    endQuery = query.filter(name__icontains=f'CVE-{endDate.year}').values()

                    serializerStart = self.serializer_class(startQuery, many=True)
                    serializerEnd = self.serializer_class(endQuery, many=True)

                    datos = {}
                    datos['data'] = serializerStart.data + serializerEnd.data

                    page = self.paginate_queryset(datos['data'])

                    return JsonResponse(self.get_paginated_response(page), safe=False, status=200)
                else:
                    return Response({"error": "Date 'start' parameter must be less than or equal to 'end' parameter."}, status=400)
            else:
                query = CveModel.objects.filter(name__icontains=f'cve-{startDate.year}').values()
                serializer = CveSerializer(query, many=True)
                return JsonResponse(serializer.data, safe=False, status=200)

        except Exception as e:
            # raise Exception(f"Error format: from: {request.META['REMOTE_ADDR']}, query: {request.META['QUERY_STRING']}")
            return Response({"error": "Parameter format error:'start=YYYY-MM-DD', 'end=YYYY-MM-DD'."}, status=400)













#
