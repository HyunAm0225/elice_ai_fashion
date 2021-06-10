import json
from .models import Product, LikeProduct
from .serializers import ProductSerializer, LikeSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from django_filters import rest_framework as filters
from django.http import HttpResponse, JsonResponse
from .pagination import CustomResultsSetPagination


class ProductView(generics.ListAPIView):
    """
    url주소에서 category와 page_size를 받아 상품을 출력해주는 api
    :param url: 불러올 url
    :return:
    """
    model = Product
    queryset = Product.objects.get_queryset().order_by('?')
    serializer_class = ProductSerializer
    permission_classes = [
        AllowAny
    ]
    pagination_class = CustomResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('category',)


class RecommendView(generics.ListAPIView):
    '''
    상품의 feature와 color을 받아 그와 맞는 상품을 출력해주는 api
    body : list안에 상품마다 feature,color를 딕셔너리 형태로 보내줌
    ex)
        [
            {
                "shorts" : "pink",
                "long sleeve outwear" : "yellow"
            },
            {
                "long sleeve dress" : "yellow"
            }
        ]
    return : feature,color값에 대한 Product 정보
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        AllowAny
    ]
    pagination_class = CustomResultsSetPagination

    def post(self, request):
        recommend_list = []
        request = (json.loads(request.body))
        print(request)
        for style in request:
            for category, color in style.items():
                print(category, color)
                recommend_product = Product.objects.filter(category=category, color=color)
                print(list(recommend_product.values()))
                recommend_list.append(list(recommend_product.values()))

        return JsonResponse({'recommend_list': recommend_list})


class LikeProductView(generics.ListAPIView):
    '''
    - post 요청시
    상품의 좋아요 상태를 추가,삭제하는 api
    body : 좋아요 할 post_id ()
    ex)
        "post_id" : 5352
    return : message

    -get 요청시
    jwt 토큰에 있는 유저정보 값으로 likeproduct 출력 api
    return : likeproduct list 출력
    '''
    model = LikeProduct
    serializer_class = LikeSerializer
    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request, format=None):
        if not LikeProduct.objects.filter(product_id=request.data['product_id'], user_id=request.user.pk).exists():
            LikeProduct.objects.create(
                user_id=request.user,
                product_id=Product.objects.get(id=request.data['product_id']),
                is_like=True
            ).save
            return HttpResponse({'message': 'CREATE_LIKE_PRODUCT'}, status=200)

        delete_product = LikeProduct.objects.get(product_id=request.data['product_id'], user_id=request.user.pk)
        delete_product.delete()
        return HttpResponse({'message': 'DELETE_LIKE_PRODUCT'}, status=200)

    def get(self, request, format=None):
        queryset = LikeProduct.objects.filter(user_id=request.user.pk)
        serializer = LikeSerializer(queryset, many=True)
        return Response(serializer.data)
