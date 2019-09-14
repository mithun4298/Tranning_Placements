from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from testapp.models import info, student
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def home(request):
    request.session.set_expiry(0)
    return render(request, 'testapp/home.html')
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = auth.authenticate(username = username,password = password)
            if user is None:
                messages.error(request, "Please provide a valid username and password")
                return render(request, 'testapp/login.html')
            else:
                request.session.set_expiry(0)
                auth.login(request, user)
                if user.is_staff:
                    messages.success(request, "Login successfully")
                    return redirect('selectstudent')
                else:
                    messages.success(request, "Login successfully")
                    return redirect('sdetails')

        except ObjectDoesNotExist:
            return render(request, 'testapp/login.html',{'error' : 'contact to admin'})

    else:
        return render(request,'testapp/login.html')
def logout(request):
    auth.logout(request)
    return render(request, 'testapp/logout.html')

def about(request):
    request.session.set_expiry(0)
    return render(request, 'testapp/about.html')

@login_required(login_url = 'login')
def infoo(request):
    request.session.set_expiry(0)
    obj = info.objects.all()
    return render(request, 'testapp/info.html', {'data' : obj})

@login_required(login_url = 'login')
def student_form(request):
    request.session.set_expiry(0)
    if request.method == 'POST':
        currentuser = request.user
        usr = User.objects.filter(username = currentuser)
        name = usr[0].first_name + " " + usr[0].last_name
        sam = request.POST['semester']
        branch = request.POST['branch']
        tenthmarks = request.POST['tenthmarks']
        twelthmarks = request.POST['twelthmarks']
        cgpa = request.POST['currentcgpa']
        skill = request.POST['skills']
        prolang = request.POST['proglang']    
        mob = request.POST['mobno'] 
     
        if len(student.objects.filter(s_username = currentuser)) == 0:
            try:
                r1 = request.FILES['resume1']
                r2 = request.FILES['resume2']
            except MultiValueDictKeyError:
                pass
            new = student.objects.create(
                s_username = currentuser,s_name = name, s_semester = sam, s_branch = branch,
                s_tenthmarks = tenthmarks, s_twelthmarks = twelthmarks, s_currentcgpa = cgpa,
                s_skills = skill, s_proglang = prolang, s_mobno = mob, s_resume1 = r1, s_resume2 = r2
            )
            new.save()
            return redirect('sdetails')

        else:
            up = student.objects.get(s_username = currentuser)
            if request.POST['semester'] is not None:
                up.s_semester = request.POST['semester']
            else:
                pass
            if request.POST['branch']:
                up.s_branch = request.POST['branch']
            else:
                pass
            if request.POST['tenthmarks']:
                up.s_tenthmarks = request.POST['tenthmarks']
            else:
                pass
            if request.POST['twelthmarks']:
                up.s_twelthmarks = request.POST['twelthmarks']
            else:
                pass
            if request.POST['currentcgpa']:
                up.s_currentcgpa = request.POST['currentcgpa']
            else:
                pass
            if request.POST['skills']:
                up.s_skills = request.POST['skills']
            else:
                pass
            if request.POST['proglang']:
                up.s_proglang = request.POST['proglang']    
            else:
                pass
            if request.POST['mobno'] :
                up.s_mobno = request.POST['mobno'] 
            else:
                pass
            try:
                if request.FILES['resume1']:
                    up.s_resume1 = request.FILES['resume1']
                else:
                    pass
            except MultiValueDictKeyError:
                up.s_resume1 = up.s_resume1
            try:
                if request.FILES['resume2']:
                    up.s_resume2 = request.FILES['resume2']
                else:
                    pass
            except MultiValueDictKeyError:
                up.s_resume2 = up.s_resume2
            up.save()
            return redirect('sdetails')
    else:
        return render(request, 'testapp/student_form.html')


@login_required(login_url = 'login')
def select_student(request):
    request.session.set_expiry(0)
    if request.method == 'POST':
        search_language = request.POST['lang']
        search_language = list(search_language.upper().split(","))
        finalsearch = []
        for search in search_language:
            finalsearch.append(search.strip())
        messages.add_message(request, messages.SUCCESS, search_language)
        # final search wich is in uppercase without space in between them
        stu = student.objects.all()
        talent = []
        username = []
        name = []
        branch = []
        semester = []
        tenthmarks = []
        twelthmarks = []
        currentcgpa = []
        mobno = []
        resume = []
        for st in stu:
            if talent:
                del talent
                talent = []
            else:
                talent = []
            for skill in st.s_skills.upper().split(","):
                talent.append(skill)
            for pro in st.s_proglang.upper().split(","):
                talent.append(pro)
            print("talent",talent)
            finaltalent = []
            for tal in talent:
                finaltalent.append(tal.strip())
            print("fianl talent",finaltalent)
            if set(finalsearch).issubset(set(finaltalent)):
                print("compare",finalsearch,finaltalent)
                username.append(st.s_username)
                name.append(st.s_name)
                branch.append(st.s_branch)
                semester.append(st.s_semester)
                tenthmarks.append(st.s_tenthmarks)
                twelthmarks.append(st.s_twelthmarks)
                currentcgpa.append(st.s_currentcgpa)
                mobno.append(st.s_mobno)
                resume.append(st.s_resume1)
            else:
                pass
        myzip = zip(username,name,branch,semester,tenthmarks,twelthmarks,currentcgpa,mobno,resume)
        return render(request, 'testapp/selectstudent.html', {'myzip': myzip})

    else:
        return render(request, 'testapp/selectstudent.html')

@login_required(login_url = 'login')
def sdetails(request):
    request.session.set_expiry(0)
    current_user = request.user
    allstudent = student.objects.filter(s_username = current_user)
    if len(allstudent) == 0:
        return redirect('student_form')
    else:
        current_user = request.user
        stu = student.objects.filter(s_username = current_user)
        return render(request, 'testapp/sdetails.html',{'student' : stu})