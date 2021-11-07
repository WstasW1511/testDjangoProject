from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet



from outlet.models import ProductModel
from outlet.serializers import ProductListSerializer


class ProductViewSet(ListModelMixin,
                    CreateModelMixin,
                    GenericViewSet):
    queryset = ProductModel.objects.all()
    # serializer_class = OutletListSerializer

    def get_serializer_class(self):
        serializer_class = ProductListSerializer
        # if self.action == 'create':
        #     serializer_class = OutletCreateSerializer
        if self.action == 'list':
            serializer_class = ProductListSerializer
        # elif self.action == 'update':
        #     serializer_class = PostUpdateSerializer
        return serializer_class


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        serializer_data = ProductListSerializer(instance).data
        return Response(data=serializer_data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
