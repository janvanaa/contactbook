from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Person, Company
from .forms import PersonForm, CompanyForm

class HomeView(generic.TemplateView):
    template_name = 'home.html'


# Person views
class ContactPersonListView(generic.ListView):
    model = Person
    
    def get_queryset(self):
        return super(ContactPersonListView, self).get_queryset()
    
class ContactPersonDetailView(generic.DetailView):
    model = Person
    template_name = 'contacts/person.html'
    
class ContactPersonCreateView(generic.CreateView):
    model = Person
    template_name = 'contacts/person_create.html'
    form_class = PersonForm
    
    def get_success_url(self):
        return reverse('person-list')
 
    def get_context_data(self, **kwargs):
        context = super(ContactPersonCreateView, self).get_context_data(**kwargs)
        context['target'] = reverse('person-new')
        return context
    
class ContactPersonUpdateView(generic.UpdateView):
    model = Person
    template_name = 'contacts/person_create.html'
    form_class = PersonForm
    
    def get_success_url(self):
        return reverse('person-list')
    
    def get_context_data(self, **kwargs):
        context = super(ContactPersonUpdateView, self).get_context_data(**kwargs)
        context['target'] = reverse('person-edit', kwargs={'pk': self.get_object().id})
        return context
    

class ContactPersonDeleteView(generic.DeleteView):
    model = Person
    template_name = 'contacts/confirm_delete.html'
    
    def get_success_url(self):
        return reverse('person-list')

#Company views
class ContactCompanyListView(generic.ListView):
    model = Company
    
    def get_queryset(self):
        return super(ContactCompanyListView, self).get_queryset()
    
class ContactCompanyDetailView(generic.DetailView):
    model = Company
    template_name = 'contacts/company.html'

class ContactCompanyCreateView(generic.CreateView):
    model = Company
    template_name = 'contacts/company_create.html'
    form_class = CompanyForm
    
    def get_success_url(self):
        return reverse('company-list')
 
    def get_context_data(self, **kwargs):
        context = super(ContactCompanyCreateView, self).get_context_data(**kwargs)
        context['target'] = reverse('company-new')
        return context
    
class ContactCompanyUpdateView(generic.UpdateView):
    model = Company
    template_name = 'contacts/company_create.html'
    form_class = CompanyForm
    
    def get_success_url(self):
        return reverse('company-list')
    
    def get_context_data(self, **kwargs):
        context = super(ContactCompanyUpdateView, self).get_context_data(**kwargs)
        context['target'] = reverse('company-edit', kwargs={'pk': self.get_object().id})
        return context
    
class ContactCompanyDeleteView(generic.DeleteView):
    model = Company
    template_name = 'contacts/company-delete'
    
    def get_success_url(self):
        return reverse('company-list')
    
    def get_context_data(self, **kwargs):
        context = super(ContactDeleteView, self).get_context_data(**kwargs)
        context['target'] =  'company-delete'
        return context

