
class SearchMixin:
    search_field = None
    search_form_class = None

    def get_query_set(self):
        queryset = super().get_queryset()
        form = self.search_form_class(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data.get(self.search_field)
            if query:
                return queryset.filter()