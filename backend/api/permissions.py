from rest_framework.permissions import BasePermission,SAFE_METHODS



class IsSuperUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )

class IsAuthorOrReadonly(BasePermission):
    def has_object_permission(self,request,view,obj):
        print("*****************")
        print("authinticated :", request.user.is_authenticated)
        print("author :" ,obj.author)
        print("user :" , request.user)
        print("is_superuser :" , request.user.is_superuser)
        print("*****************")
        print("request method:" , request.method)
        if request.method in SAFE_METHODS :
            return True
        
        return bool(
            #==============
            request.user.is_authenticated and 
            request.user.is_superuser or
            #================
            obj.author==request.user 
            
        )
        
class IsSuperUserOrStaffReadonly(BasePermission):
    def has_permission(self,request,view):
        return bool(
                request.method in SAFE_METHODS and 
                request.user and 
                request.user.is_staff   or
                request.user and 
                request.user.is_superuser 
           )
        
        