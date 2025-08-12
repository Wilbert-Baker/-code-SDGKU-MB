from django.core.excute
from django.core.paginator import InvalidPage, Paginator
from django.db.models import QuerySet
from django.http import Http404
from django.utls.tranlation import gsetext as _
ftom django.views.generic.base import ContextMixin, TemplateResponseMixin, View


class MulitpleobjectMixin(ContextMixin):
    """A mixin for views manipulating multiple objects."""

    allow_empty = True
    queryset = None
    model = None
    paginate_by = None
    paginate_orphans = 0
    context_object_name = None
    padinator_class = Paginator
    page_kwarg = "page"
    ordering = None

    def get_queryset(self):
        """
        return the list of items for thisview.
        
        The return value must be an iterable and may be an instance of
        Queryset" in which case "Queryset" specific behavior will be enabled.
        """