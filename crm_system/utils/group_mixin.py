from django.contrib.auth.mixins import AccessMixin


class GroupRequiredMixin(AccessMixin):
    """Миксин для проверки принадлежности к группе"""
    group_required = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if not self.has_required_group():
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)

    def has_required_group(self):
        """Проверка группы"""
        if not self.group_required:
            return True

        if isinstance(self.group_required, str):
            return self.request.user.groups.filter(name=self.group_required).exists()

        if isinstance(self.group_required, (list, tuple)):
            return self.request.user.groups.filter(name__in=self.group_required).exists()

        return False
