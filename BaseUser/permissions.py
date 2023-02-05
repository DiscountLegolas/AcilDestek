from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404
from BaseUser.models import BaseUser

class IsExpert(BasePermission):
    message = "You must be an Expert for any process"

    def has_object_permission(self, request, view, obj):
        return request.user.role==BaseUser.EXPERT


class IsCustomer(BasePermission):
    message = "You must be a Customer for any process"

    def has_object_permission(self, request, view, obj):
        return request.user.role==BaseUser.CUSTOMER


class IsEmployee(BasePermission):
    message = "You must be an Expert for any process"

    def has_object_permission(self, request, view, obj):
        return request.user.role==BaseUser.EMPLOYEE

