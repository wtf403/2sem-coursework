from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from comment.serializers import CommentSerializer, CommentListSerializer
from comment.models import Comment
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import NotFound

class IsSelf(BasePermission):

    def has_object_permission(self, request, view, obj):
        try: 
            user_email = request.user.email
            return user_email == str(obj.user)
        except:
            raise NotFound('Пользователь не авторизован')
           

class CommentViewSet(ModelViewSet):
    permission_classes = [IsSelf]
   
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer

    action_serializers = {
        'list': CommentListSerializer,
        'create': CommentSerializer,
        'update': CommentSerializer,
    }
        
    def get_serializer_class(self):

        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(CommentViewSet, self).get_serializer_class()
