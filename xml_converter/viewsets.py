from django.http import JsonResponse
from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from xml_converter.forms import XMLFileForm
from xml_converter.serializers import XMLFileSerializer
from xml_converter.xml_parser import parse_xml_fromstring, parse_xml_to_dict

from xml.etree.ElementTree import ParseError


def convert_xml(file_data):
    tree_data = parse_xml_fromstring(xml_fromstring=file_data)
    return parse_xml_to_dict(el=tree_data)


def upload_page(request):
    if request.method == 'POST':
        form = XMLFileForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES.get('file')
            file_content = file.open().read().decode('utf-8')

            try:
                result = convert_xml(file_data=file_content)
            except ParseError:
                return render(request, 'invalid_file_page.html', status=status.HTTP_400_BAD_REQUEST)

            return JsonResponse(result)

        return render(request, 'invalid_file_page.html', status=status.HTTP_400_BAD_REQUEST)

    return render(request, 'upload_page.html')


class ConverterViewSet(ViewSet):
    parser_classes = [MultiPartParser]

    @action(methods=['POST'], detail=False, url_path='convert')
    def convert(self, request, **kwargs):
        serializer = XMLFileSerializer(data=request.data)

        file_content = ''
        if serializer.is_valid(raise_exception=True):
            file = self.request.data.get('file')
            file_content = file.open().read().decode('utf-8')

        try:
            result = convert_xml(file_data=file_content)
        except ParseError:
            return Response(dict(error='Invalid XML file format.'), status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_200_OK)
