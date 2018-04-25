from django.contrib import admin
from .models import HistoryNote
from django.db.models import Q


class InputFilter(admin.SimpleListFilter):
    template = 'admin/input_filter.html'
    # related_filter_parameter = 'NameInSourcesFilter__TitlesFilter'

    def lookups(self, request, model_admin):
        # Dummy, required to show the filter.
        list_of_people = []
        queryset = HistoryNote.objects.order_by('id')
        if self.related_filter_parameter in request.GET:
            queryset = queryset.filter(id=request.GET[self.related_filter_parameter])
        for person in queryset:
            list_of_people.append(
                (str(person.id))
            )
        return sorted(list_of_people, key=lambda tp: tp[1])

    def choices(self, changelist):
        # Grab only the "all" option.
        all_choice = next(super().choices(changelist))
        all_choice['query_parts'] = (
            (k, v)
            for k, v in changelist.get_filters_params().items()
            if k != self.parameter_name
        )
        yield all_choice


# class NameInSourcesFilter(InputFilter):
#     parameter_name = 'name_in_sources'
#     title = ('name_in_sources')
#
#     def queryset(self, request, queryset):
#         name_in_sources = self.value()
#         if name_in_sources is None:
#             return
#         any_name = Q()
#         for bit in name_in_sources.split():
#             any_name &= (
#                 Q(name_in_sources__icontains=bit) |
#                 Q(name_in_sources__icontains=bit)
#             )
#         return queryset.filter(any_name)
#
#
# class TitlesFilter(InputFilter):
#     parameter_name = 'titles'
#     title = ('titles')
#
#     def queryset(self, request, queryset):
#         titles = self.value()
#         if titles is None:
#             return
#         any_name = Q()
#         for bit in titles.split():
#             any_name &= (
#                 Q(titles__icontains=bit) |
#                 Q(titles__icontains=bit)
#             )
#         return queryset.filter(any_name)


class HistoryNoteAdmin(admin.ModelAdmin):
    search_fields = ('name_in_sources', 'article_name', 'author_before', 'life_dates')
    # list_filter = (NameInSourcesFilter, TitlesFilter,)


admin.site.register(HistoryNote, HistoryNoteAdmin)
