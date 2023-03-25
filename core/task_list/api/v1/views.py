from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import taskSerializer
from ...models import Task
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .paginations import StandardResultsSetPagination

class TaskModelViewSet(viewsets.ModelViewSet):
    '''writing a view class for list and deatails of tasks togeather'''
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    serializer_class = taskSerializer
    queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['title', 'user','complete']
    search_fields = ['title']
    ordering_fields = ['created_date']
    pagination_class = StandardResultsSetPagination