from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict

class DrfPaginate(PageNumberPagination):
    # 用来控制每页显示多少条数据（全局参数名为PAGE_SIZE）；
    page_size = 10
    # 用来提供直接访问某页的数据；
    page_query_param = 'page'
    # 控制page_size_query_param参数能调整的最大条数
    max_page_size = 20
    # 临时调整当前显示多少条数据
    page_size_query_param = 'size'

    def get_next_link(self):
      if not self.page.has_next():
          return None
      page_number = self.page.next_page_number()
      return page_number

    def get_previous_link(self):
        if not self.page.has_previous():
            return None
        page_number = self.page.previous_page_number()
        return page_number


    def get_paginated_response(self, data):
      print('data: ', self)
      return OrderedDict([
          ('count', self.page.paginator.count),
          ('next', self.get_next_link()),
          ('previous', self.get_previous_link()),
          ('content', data)
      ])