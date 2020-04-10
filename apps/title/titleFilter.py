from django_filters import rest_framework as filters

from .models import Title


class TitleFilter(filters.FilterSet):
    """商品的过滤类"""
    # 区间查询,指定区间的最大最小值
    # min_price = filters.NumberFilter(field_name="shop_price", lookup_expr=‘gte‘)
    # max_price = filters.NumberFilter(field_name="shop_price", lookup_expr=‘lte‘)
    # 模糊查询,这里带i是忽略大小写
    # is_delete = filters.BooleanFilter(
    # field_name="is_delete", lookup_expr="exact")
    title_name = filters.CharFilter(
        field_name="title_name", lookup_expr="icontains")

    class Meta:
        model = Title
        fields = ['title_name']
