from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404
class IsExpert(BasePermission):
    message = "You must be an Expert for any process"

    def has_object_permission(self, request, view, obj):
        print(type(request.auth.key))
        print((request.auth.key))
        return request.user.is_expert


class IsCustomer(BasePermission):
    message = "You must be a Customer for any process"

    def has_object_permission(self, request, view, obj):
        return request.user.is_regular