import django_filters
from employees.models import Employee


class EmployeeFilter(django_filters.FilterSet):
    department = django_filters.CharFilter(field_name='department', lookup_expr='iexact')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    # id = django_filters.RangeFilter(field_name='id')
    id_min = django_filters.CharFilter(method='filter_by_id_range', label='From EMP ID')
    id_max = django_filters.CharFilter(method='filter_by_id_range', label='To EMP ID')

    class Meta:
        model = Employee
        fields = ['department', 'name', 'id_min', 'id_max']

    def filter_by_id_range(self, queryset, name, value):
        if name == 'id_min':
            return queryset.filter(employee_id__gte=value)
        elif name == 'id_max':
            return queryset.filter(employee_id__lte=value)
        return queryset