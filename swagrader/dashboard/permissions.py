from rest_framework.permissions import BasePermission
from .models import Course

class IsGlobalInstructor(BasePermission):
    """
    Permission to allow only instructor to have the view permissions (Course)
    """
    def has_permission(self, request, view):
        return request.user.global_instructor_privilege

class IsGlobalTA(BasePermission):
    """
    Permission to allow only TA to have the obj permissions (Course)
    """
    def has_permission(self, request, view):
        return request.user.global_ta_privilege

class IsInstructor(BasePermission):
    """
    Permission to allow only instructor to have the obj permissions (Course)
    """
    def has_object_permission(self, request, view, obj):
        print(obj, " is the obj")
        return request.user in obj.instructors.all()
    
    def has_permission(self, request, view):
        # print(request.META, " meta for the req")
        course_uid = view.kwargs.get('course_uid', None)
        if course_uid:
            course = Course.objects.filter(course_id=course_uid)
            if len(course):
                course = course.first()
                return request.user in course.instructors.all()

        else:
            return False
        