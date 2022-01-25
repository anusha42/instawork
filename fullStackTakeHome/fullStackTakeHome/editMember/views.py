from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import View
from addMember.models import Users as UsersModel
from .models import EditUsers as EditUsersModel
from .forms import EditUserForm
from addMember.forms import UserForm

def editMemberEntry(request, pk): 
        instance = get_object_or_404(UsersModel, email = pk)
        print(instance.firstName)
        if request.method == 'POST': 
            print("ITS A POST")
            form = EditUserForm(request.POST, instance = instance)
            if form.is_valid():
                form.save()
        elif request.method == 'GET':
            print("in editMemberEntry - GET")
            t = UsersModel.objects.get(email='a@s.com')
            form = EditUserForm(request.GET, instance = instance)
            t.firstName = request.GET.get('firstName')
            print(t.firstName)
            t.save()
        else:
            print('not a post')
            print(request.method)
            form = EditUserForm(request.POST, instance = instance)

class EditView(View):

    template_name = 'editMember.html'

    def get(self, request):
        user_list = []
        form_user = EditUserForm()
        users = UsersModel.objects.all()[:50]

        for user in users:
            user_list.append(user.email)


        # #THIS ACTUALLY UPDATES THE DATABASE
        # t = TemperatureData.objects.get(id=1)
        # t = 
        # t.save() # this will update only


        #ATTEMPTING TO AUTOFILL ENTRY
        print('HERE!!!')
        #print(request)
        #editMemberEntry(request, 'a@s.com')

        return render(request, self.template_name, {
            'title': 'Edit Team Member',
            'user_list': user_list,
            'form_user': form_user
        })

    def post(self, request):
        print("IN A POST")
        form_user = UserForm(request.POST)
        if form_user.is_valid():
            
            return HttpResponseRedirect('/home/')
        else:
            print('not valid')
            t = UsersModel.objects.get(email='a@s.com')
            
            t.firstName = request.POST.get('firstName')
            t.lastName = request.POST.get('lastName')
            t.phone = request.POST.get('phone')
            t.role = request.POST.get('role')

            t.save()
            return HttpResponseRedirect('/home/')

    