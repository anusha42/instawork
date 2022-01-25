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


class EditView(View):

    template_name = 'editMember.html'

    def get(self, request, email):
        print(email)
        inputUser = UsersModel.objects.get(email=email)

        user_data = {
            'firstName': inputUser.firstName,
            'lastName':  inputUser.lastName,
            'email':  email,
            'phone':  inputUser.phone,
            'role': inputUser.role
        }

        user_list = []
        form_user = EditUserForm(initial = user_data)
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

    def post(self, request, email):
        print("IN A POST")
        form_user = UserForm(request.POST)
        if form_user.is_valid():
            return HttpResponseRedirect('/home/')

        elif request.POST.get('delete'):
            UsersModel.objects.filter(email=email).delete()
            return HttpResponseRedirect('/home/')
            print('DELEting')
        elif request.POST.get('edit'):
            print('IN EDIT')
            t = UsersModel.objects.get(email=request.POST.get('email'))

            t.firstName = request.POST.get('firstName')
            t.lastName = request.POST.get('lastName')
            t.phone = request.POST.get('phone')
            t.role = request.POST.get('role')

            t.save()
            return HttpResponseRedirect('/home/')
        else:
            print('extra case')
            return HttpResponseRedirect('/editUser/')

    