from django.views.generic import TemplateView

from zinnia.views.archives import EntryIndex


class WidthEntryIndex(EntryIndex):
    template_name = 'zinnia/width_entry_list.html'


class AboutView(TemplateView):
    template_name = 'zinnia/about.html'


class ContactView(TemplateView):
    template_name = 'zinnia/contact.html'
