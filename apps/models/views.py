from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render
from apps.utils.views import GenericCreate, GenericUpdate, GenericDelete
from . import forms, models
from django.urls import reverse_lazy

# Model related views

modelform_generic_template = 'pages/modelform.html'

#
#  City
#


class CityCreate(GenericCreate):
  """Generic view to create City objects."""

  model            = models.City
  form_class       = forms.CityForm
  form__html_class = 'city'
  template_name    = modelform_generic_template
  title            = _('Añade una ciudad')
  success_url      = reverse_lazy('front')

  """ Pass context data to generic view """

  def get_context_data(self, **kwargs):
    context = super(CityCreate, self).get_context_data(**kwargs)
    context['form__html_class'] = self.form__html_class
    return context


class CityEdit(GenericUpdate):
  """Generic view to edit City objects."""

  model            = models.City
  form_class       = forms.CityForm
  form__html_class = 'city'
  template_name    = modelform_generic_template
  title            = _('Edita la información de ')
  success_url      = reverse_lazy('front')

  def get_context_data(self, **kwargs):
    """ Pass context data to generic view """
    context = super(CityEdit, self).get_context_data(**kwargs)
    id = self.kwargs['pk']
    city = get_object_or_404(models.City, pk=pk)
    context['title'] = self.title + (' ') + receiver.name
    context['form__html_class'] = self.form__html_class
    return context


class CityDelete(GenericDelete):
  """Generic view to delete City objects."""

  model            = models.City
  form_class       = forms.CityForm
  form__html_class = 'city'
  template_name    = modelform_generic_template
  title            = _('Borra la ciudad ')
  success_url      = reverse_lazy('front')

  def get_context_data(self, **kwargs):
    """ Pass context data to generic view """
    context = super(CityEdit, self).get_context_data(**kwargs)
    id = self.kwargs['pk']
    city = get_object_or_404(models.City, pk=pk)
    context['title'] = self.title + (' ') + receiver.name
    return context


#
#  Initiative
#

class InitiativeCreate(GenericCreate):
  """Generic view to create Initiative objects."""

  model            = models.Initiative
  form_class       = forms.InitiativeForm
  form__html_class = 'initiative'
  template_name    = modelform_generic_template
  title            = _('Sube tu iniciativa')
  success_url      = reverse_lazy('front')
  dependencies     = ['leaflet']

  def get_context_data(self, **kwargs):
    """Pass context data to generic view."""
    context = super(InitiativeCreate, self).get_context_data(**kwargs)
    context['form__html_class'] = self.form__html_class
    return context

  def get_initial(self):
    super(InitiativeCreate, self).get_initial()
    user = self.request.user
    return {
        "user"     : user
    }

class InitiativeEdit(GenericUpdate):
  """Generic view to edit Initiative objects."""
  model            = models.Initiative
  form_class       = forms.InitiativeForm
  form__html_class = 'initiative'
  template_name    = modelform_generic_template
  title            = _('Edita la información de la iniciativa ')
  success_url      = reverse_lazy('front')
  dependencies     = ['leaflet']

  def get_context_data(self, **kwargs):
    """Pass context data to generic view."""
    context                     = super(InitiativeEdit, self).get_context_data(**kwargs)
    slug                        = self.kwargs['slug']
    initiative                  = get_object_or_404(models.Initiative, slug=slug)
    context['title']            = self.title + (' ') + initiative.name
    context['form__html_class'] = self.form__html_class
    return context

class InitiativeDelete(GenericDelete):
  """Generic view to delete Initiative objects."""
  model            = models.Initiative
  form_class       = forms.InitiativeForm
  form__html_class = 'initiative'
  template_name    = modelform_generic_template
  title            = _('Borra la iniciativa ')
  success_url      = reverse_lazy('front')

  def get_context_data(self, **kwargs):
    """Pass context data to generic view."""
    context          = super(InitiativeDelete, self).get_context_data(**kwargs)
    slug             = self.kwargs['slug']
    initiative       = get_object_or_404(models.Initiative, slug=slug)
    context['title'] = self.title + (' ') + initiative.name
    return context


#
#  Event
#

class EventCreate(GenericCreate):
  """Generic view to create Event objects."""

  model            = models.Event
  form_class       = forms.EventForm
  form__html_class = 'event'
  template_name    = modelform_generic_template
  title            = _('Crea un evento ')
  success_url      = reverse_lazy('front')

  def get_context_data(self, **kwargs):
    """Pass context data to generic view."""
    context                     = super(EventCreate, self).get_context_data(**kwargs)
    context['form__html_class'] = self.form__html_class
    return context

class EventEdit(GenericUpdate):
  """Generic view to edit Event objects."""
  model = models.Event
  form_class = forms.EventForm
  template_name = modelform_generic_template
  title = _('Edita la información del evento ')
  success_url = reverse_lazy('front')

  def get_context_data(self, **kwargs):
    """Pass context data to generic view."""
    context                     = super(EventEdit, self).get_context_data(**kwargs)
    slug                        = self.kwargs['slug']
    event                       = get_object_or_404(models.City, slug=slug)
    context['title']            = self.title + (' ') + event.name
    context['form__html_class'] = self.form__html_class
    return context

class EventDelete(GenericDelete):
  """Generic view to delete Event objects."""

  model            = models.Event
  title            = _('Borra el evento ')
  form__html_class = 'event'
  success_url      = reverse_lazy('front')
  template_name    = modelform_generic_template

  def get_context_data(self, **kwargs):
    """Pass context data to generic view."""
    context          = super(EventDelete, self).get_context_data(**kwargs)
    slug             = self.kwargs['slug']
    event            = get_object_or_404(models.Event, slug=slug)
    context['title'] = self.title + (' ') + event.name
    return context
