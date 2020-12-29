from django.shortcuts import render,redirect
from BAI_app_v2.forms import (ParticipantInfoForm,SignUpForm,SpeedForm,SafetynWellfareForm,
                                OthersForm,EconomyForm,Project_infoForm, Project_info_1Form, 
                                QualityForm,CategoryForm, PaymentDetailsForm, UserCategoryForm)
from BAI_app_v2.models import (UserCategory, Category, PaymentDetails, Quality, Project_info, 
                                Project_info_1, Economy, Others,SafetynWellfare, Speed)
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm

from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from .utils import account_activation_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
#from verify_email.email_handler import send_verification_email
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
UserModel = get_user_model()
# Create your views here.

def home(request):
    return render(request,'BAI_app_v2/index.html')

def adminBAI(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        adminUser = authenticate(request,username=username,password=password)

        if adminUser is not None:
            if adminUser.is_active and adminUser.is_superuser:
                login(request,adminUser)
                return render(request,'BAI_app_v2/admin_home.html',{'adminUser':adminUser})

            else:
                return HttpResponse("Not Authorised to access Admin page! OR Account not active!")

        else:
            messages.add_message(request, 40, 'Invalid Login credentials')
            return redirect('BAI_app_v2/admin_login.html')
    else:
        return render(request,'BAI_app_v2/admin_login.html')


@user_passes_test(lambda u: u.is_superuser)
def admin_home(request):
    return render(request,'BAI_app_v2/admin_home.html')

@user_passes_test(lambda u: u.is_superuser)
def add_jury(request):
    return render(request,'BAI_app_v2/add_jury.html')

@user_passes_test(lambda u: u.is_superuser)
def admin_verified(request):
    return render(request,'BAI_app_v2/admin_verified.html')

@user_passes_test(lambda u: u.is_superuser)
def admin_notverified(request):

    # if request.method == "POST":
    #     #Q = Category.objects.get(users_name=request.user.username)
    #     user = Category.objects.filter(users_name=request.user.username).filter(app_form_cat=request.POST['app_form_cat'])
    #     print(user)
    #     if request.POST.get('status'):
    #         user.status = request.POST.get('status')
    #         for objs in user:
    #             objs.save()
    #         return HttpResponse('Accepted/Rejected....Check Admin page!!!')
    #     else:
    #         return HttpResponse('chuklay ikde!!!')

    cat_id = {
        "Residential (bungalow, row houses, standalone buildings)":1,
        "Residential (housing complex)":2,
        "Residential ( affordable housing)":3,
        "Commercial (malls, office, institution, hotel, hospital, cinema)":4,
        "Industrial (any size, any type)":5,
        "Infrastructure (bridges, flyovers, ESR etc.)":6,
        "Well equipped, well mechanized site":7,
        "Government, Semi-Govt., Public Works":8,
        "Work upto Bare Shell (includes RCC, Masonry and Plaster works)":9
    }
    all_entries = list()
    #q1 = Category.objects.filter(users_name).filter(app_form_cat)
    q1 = Category.objects.values('users_name','app_form_cat','status')
    #print(q1)
    for itr in q1:
        count = 0
        user = itr['users_name']
        cat = itr['app_form_cat']
        stat = itr['status']

        test = [Project_info,Project_info_1,Quality,Economy,Speed,PaymentDetails,Others,SafetynWellfare]
        for i in test:
            q = i.objects.filter(users_name=user).filter(category_latest=cat)
            if len(q)>0:
                count = count+1

        if count==8:
            sub_entry = list()
            sub_entry.append(user)
            sub_entry.append(cat_id[cat])
            sub_entry.append(stat)
            all_entries.append(sub_entry)
    
    return render(request,'BAI_app_v2/admin_notverified.html',{'all_entries':all_entries})  

@user_passes_test(lambda u: u.is_superuser)
def AcceptForm(request,user,cat_id):
    cat = {
            1:"Residential (bungalow, row houses, standalone buildings)",
            2:"Residential (housing complex)",
            3:"Residential ( affordable housing)",
            4:"Commercial (malls, office, institution, hotel, hospital, cinema)",
            5:"Industrial (any size, any type)",
            6:"Infrastructure (bridges, flyovers, ESR etc.)",
            7:"Well equipped, well mechanized site",
            8:"Government, Semi-Govt., Public Works",
            9:"Work upto Bare Shell (includes RCC, Masonry and Plaster works)"
        }
    category = cat[cat_id]
    #q = Category.objects.filter(users_name=user).filter(app_form_cat=category)
    q1 = Category.objects.get(users_name=user,app_form_cat=category)
    q1.status = 1
    q1.save()
    return HttpResponse("Accepted successfully!!")


@user_passes_test(lambda u: u.is_superuser)
def RejectForm(request,user,cat_id):
    cat = {
            1:"Residential (bungalow, row houses, standalone buildings)",
            2:"Residential (housing complex)",
            3:"Residential ( affordable housing)",
            4:"Commercial (malls, office, institution, hotel, hospital, cinema)",
            5:"Industrial (any size, any type)",
            6:"Infrastructure (bridges, flyovers, ESR etc.)",
            7:"Well equipped, well mechanized site",
            8:"Government, Semi-Govt., Public Works",
            9:"Work upto Bare Shell (includes RCC, Masonry and Plaster works)"
        }
    category = cat[cat_id]
    #q = Category.objects.filter(users_name=user).filter(app_form_cat=category)
    q1 = Category.objects.get(users_name=user,app_form_cat=category)
    q1.status = 2
    q1.save()
    return HttpResponse("Rejected Form!!")


@user_passes_test(lambda u: u.is_superuser)
def view_jury(request):
    return render(request,'BAI_app_v2/view_jury.html')



@login_required
def participant_logout(request):
    logout(request)
    return render(request,'BAI_app_v2/login.html')


def signup(request):
    
    registered = False

    if request.method == 'POST':
        signup_form = SignUpForm(data=request.POST)
        participant_form = ParticipantInfoForm(data=request.POST)

        if signup_form.is_valid() and participant_form.is_valid():
            user = signup_form.save()
            user.set_password(user.password)
            user.save()

            profile = participant_form.save(commit=False)
            profile.user = user
            profile.save()

            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('BAI_app_v2/active_email.html',
                                       {
                                           'user': user,
                                           'domain': current_site.domain,
                                           'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                           'token': default_token_generator.make_token(user),
                                       }
                                       )
            email_subject = 'Builders Association of India Account Verification.'

            to_email = user.email
            email = EmailMessage(
                email_subject,
                message,
                to=[to_email]
            )
            email.send(fail_silently=True)

            registered = True
            UserCategory(users_name=user.username).save()

            #messages.add_message(request, 40, 'Signup Successful!\nHead on to Logging In to fill the Application Form')
            return render(request, 'BAI_app_v2/signup.html', {'registered': registered})
        
        else:
            error_string = ' '.join([' '.join(x for x in l) for l in list(signup_form.errors.values())])
            return render(request, 'BAI_app_v2/signup.html',
                          {'signup_form': signup_form,
                           'participant_form': participant_form,
                           'registered': registered,
                           'error': error_string})

    else:
        return render(request, 'BAI_app_v2/signup.html', {'registered': registered})



def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user123 = authenticate(request,username=username,password=password)

        if user123 is not None:
            if user123.is_active:
                login(request,user123)
                obj = UserCategory.objects.all().filter(users_name=username)
                if len(obj) == 0:
                    UserCategory(users_name=username).save()

                return render(request,'BAI_app_v2/user_landing.html',{'user123':user123})

            else:
                return HttpResponse("Account not Active!")

        else:
            messages.add_message(request, 40, 'Invalid Login credentials')
            return redirect('/BAI_app_v2/user_login/')
    else:
        return render(request,'BAI_app_v2/login.html',{})

@login_required(login_url='/BAI_app_v2/user_login/')
def user_landing(request):
    return render(request,'BAI_app_v2/user_landing.html')

@login_required(login_url='/BAI_app_v2/user_login/')
def user_profile(request):
    return render(request,'BAI_app_v2/user_profile.html')


@login_required(login_url='/BAI_app_v2/user_login/')
def form0(request):

    filled0 = False
    if request.method == 'POST':

        category_cat = CategoryForm(data=request.POST)
        if category_cat.is_valid():
            category_cat1 = category_cat.save()
            category_cat1.users_name = request.user.username
            category_cat1.filled0 = 'True'
            category_cat1.save()
            obj = UserCategory.objects.filter(users_name=request.user.username)
            obj.update(category_latest=category_cat1.app_form_cat)
            #obj[0]
            obj[0].save()
            filled0 = True
            return render(request,'BAI_app_v2/form1_1.html',{'category_cat':category_cat,'filled0':filled0})

        else:
            # print("Chuklay ikde!")
            # print(category_cat)
            # print(category_cat.errors)
            error_string0 = ' '.join([' '.join(x for x in l) for l in list(category_cat.errors.values())])
            return render(request, 'BAI_app_v2/form0.html',
                          {'category_cat': category_cat,
                           'error0': error_string0})

    else:
        category_cat = CategoryForm()
        return render(request,'BAI_app_v2/form0.html',{'category_cat':category_cat,'filled0':filled0})
        
    #messages.info(request, 'Category selected successfully!!')
    

@login_required(login_url='/BAI_app_v2/user_login/')
def form1_1(request):
    filled1_1 = False
    if request.method == 'POST':

        project_info_cat = Project_infoForm(request.POST,request.FILES)
        
        if project_info_cat.is_valid():
            obj = UserCategory.objects.filter(users_name=request.user.username)

            project_info_cat1 = project_info_cat.save(commit=False)   
  
            if 'site_map' in request.FILES:
                project_info_cat1.site_map = request.FILES['site_map']   

            project_info_cat1.users_name = request.user.username
            project_info_cat1.filled1_1 = 'True'
            project_info_cat1.category_latest = obj[0].category_latest
            project_info_cat1.save()

            filled1_1 = True
            return render(request,'BAI_app_v2/form1_2.html',{'project_info_cat':project_info_cat,'filled1_1':filled1_1})

        else:
            error_string1_1 = ' '.join([' '.join(x for x in l) for l in list(project_info_cat.errors.values())])
            return render(request, 'BAI_app_v2/form1_1.html',
                          {'project_info_cat': project_info_cat,
                           'error1_1': error_string1_1})

    else:
        project_info_cat = Project_infoForm()
        return render(request,'BAI_app_v2/form1_1.html',{'project_info_cat':project_info_cat,
                                                    'filled1_1':filled1_1})

@login_required(login_url='/BAI_app_v2/user_login/')
def form1_2(request):
    filled1_2 = False
    if request.method == 'POST':

        project_info_1_cat = Project_info_1Form(request.POST,request.FILES)
        if project_info_1_cat.is_valid():
            obj = UserCategory.objects.filter(users_name=request.user.username)
            project_info_1_cat1 = project_info_1_cat.save(commit=False)

            if 'req_docs' in request.FILES:
                project_info_1_cat1.req_docs = request.FILES['req_docs']
            if 'green_project_details' in request.FILES:
                project_info_1_cat1.green_project_details = request.FILES['green_project_details']

            project_info_1_cat1.users_name = request.user.username
            project_info_1_cat1.filled1_2 = 'True'
            project_info_1_cat1.category_latest = obj[0].category_latest
            project_info_1_cat1.save()

            filled1_2 = True
            return render(request,'BAI_app_v2/form1_3.html',{'project_info_1_cat':project_info_1_cat,'filled1_2':filled1_2})
        
        else:
            error_string1_2 = ' '.join([' '.join(x for x in l) for l in list(project_info_1_cat.errors.values())])
            return render(request, 'BAI_app_v2/form1_2.html',
                          {'project_info_1_cat': project_info_1_cat,
                           'error1_2': error_string1_2})
    
    else:
        project_info_1_cat = Project_info_1Form()
        return render(request,'BAI_app_v2/form1_2.html',{'project_info_1_cat':project_info_1_cat,
                                                    'filled1_2':filled1_2})


@login_required(login_url='/BAI_app_v2/user_login/')
def form1_3(request):
    filled1_3 = False
    if request.method == 'POST':

        quality_cat = QualityForm(request.POST,request.FILES)
        if quality_cat.is_valid():
            obj = UserCategory.objects.filter(users_name=request.user.username)
            quality_cat1 = quality_cat.save(commit=False)

            if 'meeting_instruction_book_minute' in request.FILES:
                quality_cat1.meeting_instruction_book_minute = request.FILES['meeting_instruction_book_minute']
            if 'sample_Checklist_followed' in request.FILES:
                quality_cat1.sample_Checklist_followed = request.FILES['sample_Checklist_followed']
            if 'sample_test_reports' in request.FILES:
                quality_cat1.sample_test_reports = request.FILES['sample_test_reports']

            quality_cat1.users_name = request.user.username
            quality_cat1.filled1_3 = 'True'
            quality_cat1.category_latest = obj[0].category_latest
            quality_cat1.save()

            filled1_3 = True
            return render(request,'BAI_app_v2/form1_4.html',{'quality_cat':quality_cat,'filled1_3':filled1_3})

        else:
            error_string1_3 = ' '.join([' '.join(x for x in l) for l in list(quality_cat.errors.values())])
            return render(request, 'BAI_app_v2/form1_3.html',
                          {'quality_cat': quality_cat,
                           'error1_3': error_string1_3})

    else:
        quality_cat = QualityForm()
        return render(request,'BAI_app_v2/form1_3.html',{'quality_cat':quality_cat,
                                                    'filled1_3':filled1_3})


@login_required(login_url='/BAI_app_v2/user_login/')
def form1_4(request):
    filled1_4 = False
    if request.method == 'POST':

        speed_cat = SpeedForm(data=request.POST)
        if speed_cat.is_valid():
            obj = UserCategory.objects.filter(users_name=request.user.username)
            speed_cat1 = speed_cat.save()

            speed_cat1.users_name = request.user.username
            speed_cat1.filled1_4 = 'True'
            speed_cat1.category_latest = obj[0].category_latest
            speed_cat1.save()

            filled1_4 = True
            return render(request,'BAI_app_v2/form2_1.html',{'speed_cat':speed_cat,'filled1_4':filled1_4})

        else:
            error_string1_4 = ' '.join([' '.join(x for x in l) for l in list(speed_cat.errors.values())])
            return render(request, 'BAI_app_v2/form1_4.html',
                          {'speed_cat': speed_cat,
                           'error1_4': error_string1_4})

    else:
        speed_cat = SpeedForm()
        return render(request,'BAI_app_v2/form1_4.html',{'speed_cat':speed_cat,
                                                    'filled1_4':filled1_4})


@login_required(login_url='/BAI_app_v2/user_login/')
def form2_2(request):
    filled2_2 = False
    if request.method == 'POST':

        safety_cat = SafetynWellfareForm(request.POST,request.FILES)

        if safety_cat.is_valid():
            obj = UserCategory.objects.filter(users_name=request.user.username)
            safety_cat1 = safety_cat.save(commit=False)

            if 'safety_audits' in request.FILES:
                safety_cat1.safety_audits = request.FILES['safety_audits']

            safety_cat1.users_name=request.user.username
            safety_cat1.filled2_2 = 'True'
            safety_cat1.category_latest = obj[0].category_latest
            safety_cat1.save()

            filled2_2 = True
            return render(request,'BAI_app_v2/form2_3.html',{'safety_cat':safety_cat,'filled2_2':filled2_2})

        else:
            error_string2_2 = ' '.join([' '.join(x for x in l) for l in list(safety_cat.errors.values())])
            return render(request, 'BAI_app_v2/form2_2.html',
                          {'safety_cat': safety_cat,
                           'error2_2': error_string2_2})     

    else:
        safety_cat = SafetynWellfareForm()
        return render(request,'BAI_app_v2/form2_2.html',{'safety_cat':safety_cat,
                                                    'filled2_2':filled2_2})

@login_required(login_url='/BAI_app_v2/user_login/')
def form2_1(request):
    filled2_1 = False
    if request.method == 'POST':

        economy_cat = EconomyForm(request.POST)
        if economy_cat.is_valid():
            obj = UserCategory.objects.filter(users_name=request.user.username)
            economy_cat1 = economy_cat.save()

            economy_cat1.users_name = request.user.username
            economy_cat1.filled2_1 = 'True'
            economy_cat1.category_latest = obj[0].category_latest
            economy_cat1.save()

            filled2_1 = True
            return render(request,'BAI_app_v2/form2_2.html',{'economy_cat':economy_cat,'filled2_1':filled2_1})

        else:
            error_string2_1 = ' '.join([' '.join(x for x in l) for l in list(economy_cat.errors.values())])
            return render(request, 'BAI_app_v2/form2_1.html',
                          {'economy_cat': economy_cat,
                           'error2_1': error_string2_1})

    else:
        economy_cat = EconomyForm()
        return render(request,'BAI_app_v2/form2_1.html',{'economy_cat':economy_cat,
                                                    'filled2_1':filled2_1})


@login_required(login_url='/BAI_app_v2/user_login/')
def form2_3(request):
    filled2_3 = False
    if request.method == 'POST':

        others_cat = OthersForm(request.POST,request.FILES)
        if others_cat.is_valid():
            obj = UserCategory.objects.filter(users_name=request.user.username)
            others_cat1 = others_cat.save(commit=False)

            others_cat1.accomodation = request.FILES['accomodation']
            others_cat1.sanitary = request.FILES['sanitary']
            others_cat1.polution_measures = request.FILES['polution_measures']

            if 'school' in request.FILES:
                others_cat1.school = request.FILES['school']

            if 'renewable_energy_pic' in request.FILES:
                others_cat1.renewable_energy_pic = request.FILES['renewable_energy_pic']            

            others_cat1.users_name=request.user.username
            others_cat1.filled2_3 = 'True'
            others_cat1.category_latest = obj[0].category_latest
            others_cat1.save()
            filled2_3 = True
            return render(request,'BAI_app_v2/form3.html',{'others_cat':others_cat,'filled2_3':filled2_3})

        else:
            error_string2_3 = ' '.join([' '.join(x for x in l) for l in list(others_cat.errors.values())])
            return render(request, 'BAI_app_v2/form2_3.html',
                          {'others_cat': others_cat,
                           'error2_3': error_string2_3})

    else:
        others_cat = OthersForm()
        return render(request,'BAI_app_v2/form2_3.html',{'others_cat':others_cat,
                                                    'filled2_3':filled2_3})


@login_required(login_url='/BAI_app_v2/user_login/')
def form3(request):

    filled3 = False
    if request.method == 'POST':

        payment_cat = PaymentDetailsForm(data=request.POST)
        if payment_cat.is_valid():
            obj = UserCategory.objects.filter(users_name=request.user.username)
            payment_cat1 = payment_cat.save()
            payment_cat1.users_name = request.user.username
            payment_cat1.filled3 = 'True'
            payment_cat1.category_latest = obj[0].category_latest
            payment_cat1.save()

            filled3 = True
            return HttpResponse("Application Form Filled Successfully!")

        else:
            error_string3 = ' '.join([' '.join(x for x in l) for l in list(payment_cat.errors.values())])
            return render(request, 'BAI_app_v2/form3.html',
                          {'payment_cat': payment_cat,
                           'error3': error_string3})

    else:
        payment_cat = PaymentDetailsForm()
        return render(request,'BAI_app_v2/form3.html',{'payment_cat':payment_cat,'filled3':filled3})


@login_required(login_url='/BAI_app_v2/user_login/')
def change_pass(request):

    if request.method == 'POST':
        changePass = PasswordChangeForm(user=request.user,data=request.POST)
        if changePass.is_valid():
            changePass.save()
            # print(changePass)
            #update_session_auth_hash(request,changePass.user)
            return HttpResponse("Password Changed Successfully")

        # else:
        #     #print("old:{} new1:{} new2:{}".format(old_password,new_password1,new_password2))
        #     print(changePass)
        #     return HttpResponse("Request for Change Password Failed!")

    else:
        changePass = PasswordChangeForm(user=request.user)
    return render(request,'BAI_app_v2/changePassword.html',{'changePass':changePass})

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
        #email_verified = False
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        #email_verified = True
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        #return render(request, 'BAI_app_v2/signup.html', {'email_verified': email_verified})
    else:
        return HttpResponse('Activation link is invalid!')


cat = {
            1:"Residential (bungalow, row houses, standalone buildings)",
            2:"Residential (housing complex)",
            3:"Residential ( affordable housing)",
            4:"Commercial (malls, office, institution, hotel, hospital, cinema)",
            5:"Industrial (any size, any type)",
            6:"Infrastructure (bridges, flyovers, ESR etc.)",
            7:"Well equipped, well mechanized site",
            8:"Government, Semi-Govt., Public Works",
            9:"Work upto Bare Shell (includes RCC, Masonry and Plaster works)"
        }

def viewForm1_1(request,user,cat_id):
    category = cat[cat_id]
    q = Project_info.objects.get(users_name=user,category_latest=category)
    return render(request,'BAI_app_v2/viewForm1_1.html',{"Project_info":q,"cat_id":cat_id})
    
def viewForm1_2(request,user,cat_id):
    category = cat[cat_id]
    q1 = Project_info_1.objects.get(users_name=user,category_latest=category)
    return render(request,'BAI_app_v2/viewForm1_2.html',{"Project_info_1":q1,"cat_id":cat_id})

def viewForm1_3(request,user,cat_id):
    category = cat[cat_id]
    q2 = Quality.objects.get(users_name=user,category_latest=category)
    return render(request,'BAI_app_v2/viewForm1_3.html',{"Quality":q2,"cat_id":cat_id})

def viewForm1_4(request,user,cat_id):
    category = cat[cat_id]
    q3 = Speed.objects.get(users_name=user,category_latest=category)
    return render(request,'BAI_app_v2/viewForm1_4.html',{"Speed":q3,"cat_id":cat_id})

def viewForm2_1(request,user,cat_id):
    category = cat[cat_id]
    q = Economy.objects.get(users_name=user,category_latest=category)
    return render(request,'BAI_app_v2/viewForm2_1.html',{"Economy":q,"cat_id":cat_id})

def viewForm2_2(request,user,cat_id):
    category = cat[cat_id]
    q = SafetynWellfare.objects.get(users_name=user,category_latest=category)
    return render(request,'BAI_app_v2/viewForm2_2.html',{"SafetynWellfare":q,"cat_id":cat_id})

def viewForm2_3(request,user,cat_id):
    category = cat[cat_id]
    q = Others.objects.get(users_name=user,category_latest=category)
    return render(request,'BAI_app_v2/viewForm2_3.html',{"Others":q,"cat_id":cat_id})

def viewForm3(request,user,cat_id):
    category = cat[cat_id]
    q = PaymentDetails.objects.get(users_name=user,category_latest=category)
    return render(request,'BAI_app_v2/viewForm3.html',{"PaymentDetails":q,"cat_id":cat_id})

