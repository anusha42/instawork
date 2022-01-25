from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from addMember.models import Users as UsersModel
# from .forms import UserForm


class ListView(View):
    template_name = 'listMembers.html'

    def get(self, request):
        user_list = []
        #form_user = UserForm()
        users = UsersModel.objects.all()[:50]

        for user in users:
            if (user.role == 1):
                roleName = '(Admin)'
            else:
                roleName = ''
                
            user_list.append({'firstName': user.firstName, 'lastName': user.lastName, 'phone': user.phone, 
            	'email': user.email, 'role': roleName})

        

        return render(request, self.template_name, {
            'title': 'Team Members:',
            'user_list': user_list,
            'num_members': len(user_list)
        })

    # def post(self, request):
    #     form_user = UserForm(request.POST)
    #     if form_user.is_valid():
    #         form_user.save()
    #         return HttpResponseRedirect('/addUser/')
