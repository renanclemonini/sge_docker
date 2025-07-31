from rest_framework.permissions import BasePermission


class StrictDjangoModelPermissions(BasePermission):
    """
    Bloqueia requisições se o usuário não tiver permissão explícita no modelo,
    inclusive o GET (requere 'view_modelname').
    """
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False

        queryset = getattr(view, 'queryset', None)
        if queryset is None:
            return False

        model_cls = queryset.model
        required_perms = [perm % {
            'app_label': model_cls._meta.app_label,
            'model_name': model_cls._meta.model_name
        } for perm in self.perms_map.get(request.method, [])]

        return user.has_perms(required_perms)
