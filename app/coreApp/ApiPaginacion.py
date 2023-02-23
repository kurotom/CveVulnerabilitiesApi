from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PaginacionAPI(PageNumberPagination):
    page_size = 20

    def get_paginated_response(self, data):
        return {
            'next': self.get_next_link(),
            'prev': self.get_previous_link(),
            'current': f'{self.page.number} - {self.page.paginator.num_pages}',
            'results': data
        }
