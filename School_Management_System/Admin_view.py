import datetime
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from School.models import Course, Session_Year, CustomUser, Student, Blood_Group, Staff, Subject, Staff_Notification, Staff_Leave,Staff_Feedback, Student_Notification, Student_Feedback, Student_Leave, Attendance,Attendance_Report, StudentResult
from django.contrib import messages


@login_required(login_url='/')
def HOME(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subject.objects.all().count()
    
    student_gender_male = Student.objects.filter(gender= 'male').count()
    student_gender_female = Student.objects.filter(gender= 'female').count()

    
    context ={
        'student_count': student_count,
        'staff_count': staff_count,
        'course_count': course_count,
        'subject_count': subject_count,
        'student_gender_male': student_gender_male,
        'student_gender_female': student_gender_female,
    }
     
    return render(request, 'Admin/home.html' , context)

@login_required(login_url='/')
def ADD_STUDENT(request):
    course = Course.objects.all()
    session_year = Session_Year.objects.all()
    blood_group = Blood_Group.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        date_of_birth=request.POST.get('date_of_birth')
        blood_group_id = request.POST.get('blood_group_id')  
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        study_year = request.POST.get('study_year')
        department = request.POST.get('department')
        mobile_no = request.POST.get("mobile_no")
        parent_name = request.POST.get("parent_name")
        parent_mobile_no = request.POST.get("parent_mobile_no")
    
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('add_student')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=3
            )
            user.set_password(password)
            user.save()

            course= Course.objects.get(id=course_id)
            session_year = Session_Year.objects.get(id=session_year_id)
            blood_group = Blood_Group.objects.get(id=blood_group_id)
            
            
            student = Student(
                admin=user,
                address=address,
                session_year_id=session_year,
                course_id=course,
                gender=gender,
                date_of_birth=date_of_birth,
                blood_group_id=blood_group,
                department = department,
                study_year = study_year,
                mobile_no = mobile_no,
                parent_name = parent_name,
                parent_mobile_no = parent_mobile_no,
                
            )
            student.save()

            messages.success(request, f"{user.first_name} {user.last_name} was Successfully Added!")
            return redirect('add_student')
        
    context = {
        'course': course,
        'session_year': session_year,
        'blood_group': blood_group,
    }
    return render(request, 'Admin/add_student.html', context)

@login_required(login_url='/')
def VIEW_STUDENT(request):
    student = Student.objects.all()
    
    
    context = {
        'student': student,
    }
    
    return render(request, 'Admin/view_student.html', context)

@login_required(login_url='/')
def EDIT_STUDENT(request,id):
    student = Student.objects.filter(id =id)
    course =Course.objects.all()
    session_year = Session_Year.objects.all()
    blood_group = Blood_Group.objects.all()

    
    context ={
        'student':student,
        'course':course,
        'session_year':session_year,
        'blood_group':blood_group,
    } 
    
    return render(request,'Admin/edit_student.html',context)

@login_required(login_url='/')
def UPDATE_STUDENT(request):
    
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth') 
        blood_group_id = request.POST.get('blood_group_id')  
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        study_year = request.POST.get('study_year')
        department = request.POST.get('department')
        mobile_no = request.POST.get("mobile_no")
        parent_name = request.POST.get("parent_name")
        parent_mobile_no = request.POST.get("parent_mobile_no")
            
        user = CustomUser.objects.get(id=student_id)
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.username=username
        
        
        if password !=None and password != "":
                user.set_password(password)

        if profile_pic !=None and profile_pic != "":
                user.profile_pic=profile_pic
        user.save() 
        
        
        student = Student.objects.get(admin = student_id)
        student.address = address
        student.gender = gender
        student.department = department
        student.study_year = study_year
        student.mobile_no = mobile_no
        student.parent_name = parent_name
        student.parent_mobile_no = parent_mobile_no



        course = Course.objects.get(id = course_id)
        student.course_id = course

        blood_group = Blood_Group.objects.get(id = blood_group_id)
        student.blood_group_id = blood_group
        
        session_year = Session_Year.objects.get(id = session_year_id)
        student.session_year_id = session_year
        
        if date_of_birth:
            date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d').date()
            student.date_of_birth = date_of_birth

        student.save()
        messages.success(request, f"{user.first_name} {user.last_name} was Successfully Update!")
        return redirect('view_student')

    
    return render(request,'Admin/edit_student.html')

@login_required(login_url='/')
def DELETE_STUDENT(request, admin):
    Student=CustomUser.objects.get(id=admin)
    Student.delete()
    
    messages.success(request, 'Student Record are Successfully Deleted!')
    return redirect('view_student')

# for course admin 
 
@login_required(login_url='/')   
def ADD_COURSE(request):
    if request.method == "POST":
        course_name=request.POST.get('course_name')
        
        course= Course(
            name = course_name,
        )
        course.save()
        messages.success(request,'Course are Successfully Created!')
        return redirect('add_course')
    
    return render(request,'Admin/add_course.html')

@login_required(login_url='/')
def  VIEW_COURSE(request):
    course=Course.objects.all()
    
    context ={
        'course':course,
    }
    
    return render(request,'Admin/view_course.html', context)

@login_required(login_url='/')
def EDIT_COURSE(request,id):
    course = Course.objects.get(id = id)

    context ={
        'course':course,
    }
    
    return  render(request,'Admin/edit_course.html',context)

@login_required(login_url='/')
def UPDATE_COURSE(request):
    if request.method == 'POST':
            name = request.POST.get('name')
            course_id =request.POST.get('course_id')
            
            course = Course.objects.get(id = course_id)
            course.name = name
            course.save()
            
            messages.success(request,'Course are Successfully Updated!')
            return redirect('view_course')
            
    return render(request, 'Admin/edit_course.html')

@login_required(login_url='/')
def DELETE_COURSE(request, id):
    course = Course.objects.get(id = id)
    course.delete()
    messages.success(request, ' Course are Successfully Deleted!')
    
    return redirect('view_course')    


# for staff admin
@login_required(login_url='/')
def ADD_STAFF(request):
    blood_groups = Blood_Group.objects.all()

    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        blood_group_id = request.POST.get('blood_group_id')
        salary = request.POST.get('salary')
        department = request.POST.get('department')
        hire_date = request.POST.get('hire_date')
        highest_education = request.POST.get('highest_education')
        position = request.POST.get('position')
        mobile_no = request.POST.get('mobile_no')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('add_staff')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('add_staff')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=2
            )
            user.set_password(password)
            user.save()

            blood_group = Blood_Group.objects.get(id=blood_group_id)

            staff = Staff(
                admin=user,
                address=address,
                gender=gender,
                date_of_birth=date_of_birth,
                blood_group_id=blood_group,
                salary=salary,
                department=department,
                hire_date=hire_date,
                highest_education=highest_education,
                position=position,
                mobile_no=mobile_no
            )
            staff.save()
            messages.success(request, f"{user.first_name} {user.last_name} was Successfully Added!")
            return redirect('add_staff')

    context = {
        'blood_groups': blood_groups,
    }

    return render(request, 'Admin/add_staff.html', context)

@login_required(login_url='/')
def VIEW_STAFF(request):
    staff = Staff.objects.all()
    
    context= {
        'staff':staff,
    }
    
    return render(request,'Admin/view_staff.html',context)
 
@login_required(login_url='/') 
def EDIT_STAFF(request, id):
    staff = Staff.objects.get(id=id)
    blood_group = Blood_Group.objects.all()

    context = {
        'staff': staff,
        'blood_group': blood_group,
    }

    return render(request, 'Admin/edit_staff.html', context)
   
@login_required(login_url='/')  
def UPDATE_STAFF(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        blood_group_id = request.POST.get('blood_group_id')
        salary = request.POST.get('salary')
        department = request.POST.get('department')
        hire_date = request.POST.get('hire_date')
        highest_education = request.POST.get('highest_education')
        position = request.POST.get('position')
        mobile_no = request.POST.get('mobile_no')

        user = CustomUser.objects.get(id=staff_id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        if password and password != "":
            user.set_password(password)

        if profile_pic and profile_pic != "":
            user.profile_pic = profile_pic

        user.save()

        staff = Staff.objects.get(admin=user)
        blood_group = Blood_Group.objects.get(id=blood_group_id)

        staff.address = address
        staff.salary = salary
        staff.gender = gender
        staff.department = department
        staff.blood_group_id = blood_group
        staff.highest_education = highest_education
        staff.position = position
        staff.mobile_no = mobile_no

        if date_of_birth:
            date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d').date()
            staff.date_of_birth = date_of_birth

        if hire_date:
            hire_date = datetime.strptime(hire_date, '%Y-%m-%d').date()
            staff.hire_date = hire_date

        staff.save()
       
    
        messages.success(request, f"{user.first_name} {user.last_name} was Successfully Updated!")
        return redirect('view_staff')

    return render(request , 'Admin/edit_staff.html')

@login_required(login_url='/')
def DELETE_STAFF(request , admin):
    staff =CustomUser.objects.get(id = admin)
    
    staff.delete()
    
    messages.success(request, 'Staff Record are Successfully Deleted!')
    return redirect('view_staff')

# for subject
@login_required(login_url='/')
def ADD_SUBJECT(request):
    course = Course.objects.all()
    staff = Staff.objects.all()

    if request.method == 'POST':
        name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)

        subject = Subject(
             name=name,  
             course=course,
             staff=staff,
        )

        subject.save()

        messages.success(request, 'Subject Are Successfully Added!')
        return redirect('add_subject')

    context = {
        'course': course,
        'staff': staff,
    }
    return render(request, 'Admin/add_subject.html', context)

@login_required(login_url='/')
def VIEW_SUBJECT(request):
    
    subject = Subject.objects.all()
    context = {
        'subject': subject,
    }
    
    return render(request, 'Admin/view_subject.html' ,context)

@login_required(login_url='/')
def EDIT_SUBJECT(request, id):
    subject = Subject.objects.get(id = id)
    course = Course.objects.all()
    staff = Staff.objects.all()
    
    context = {
        'subject': subject,
        'course': course,
        'staff' : staff,
    }
    
    return render(request, 'Admin/edit_subject.html', context)

@login_required(login_url='/')
def UPDATE_SUBJECT(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')
        
        
        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)
        
        subject = Subject(
             id=subject_id,
             name = subject_name,  
             course=course,
             staff=staff,
        )

        subject.save()

        messages.success(request, 'Subject Are Successfully Updated!')
        return redirect('view_subject')
    
    return render(request, 'Admin/view_subject.html')

@login_required(login_url='/')
def DELETE_SUBJECT(request , id):
      subject = Subject.objects.filter(id =id)
      subject.delete()
      messages.success(request, 'Subject Are Successfully Deleted!')
      return redirect('view_subject')
    
    
#for session 

@login_required(login_url='/')
def  ADD_SESSION(request):
    if request.method == 'POST':
        session_year_start = request.POST.get('session_year_start')
        session_year_end =  request.POST.get('session_year_end')
        
        session = Session_Year(
            session_start = session_year_start,
            session_end = session_year_end,
        )
        session.save()
        messages.success(request, 'Session Are Successfully Created!')
        return redirect('add_session')
        
    return render(request, 'Admin/add_session.html')

@login_required(login_url='/')
def VIEW_SESSION(request):
    session = Session_Year.objects.all()
    
    context = {
        'session': session,
    }
    
    return render(request , 'Admin/view_session.html', context)

@login_required(login_url='/')
def EDIT_SESSION(request , id):
    session = Session_Year.objects.filter(id=id)
    
    context = {
        'session': session,
    }
    
    return render(request, 'Admin/edit_session.html', context)

@login_required(login_url='/')
def UPDATE_SESSION(request):
    if request.method == 'POST':
        session_id = request.POST.get('session_id')
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')
        
        session = Session_Year(
          id= session_id,
          session_start = session_year_start,
          session_end = session_year_end,
        )
        session.save()
        messages.success(request, 'Session Are Successfully Updated!')
        return redirect('view_session')
        
    
    return render(request, 'Admin/view_session.html')

@login_required(login_url='/')
def DELETE_SESSION(request , id):
    session = Session_Year.objects.get(id = id)
    session.delete()
    
    messages.success(request, 'Session Are Successfully Deleted!')
    return redirect('view_session')
    
# for notification
@login_required(login_url='/')
def STAFF_SEND_NOTIFICATION(request):
    staff = Staff.objects.all()
    see_notification = Staff_Notification.objects.all().order_by('-id')
    
    context = {
        'staff': staff,
        'see_notification' : see_notification,
    }
     
    return render(request,'Admin/staff_notification.html', context)

@login_required(login_url='/')
def STAFF_SAVE_NOTIFICATION(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')
        
        staff =Staff.objects.get(admin=staff_id)
        
        notification = Staff_Notification(
            staff_id=staff,
            message = message,
        )
        notification.save()
        messages.success(request, 'Notification Are Successfully Send')
        return redirect('staff_send_notification')
    
@login_required(login_url='/')
def STAFF_LEAVE_VIEW(request):
    staff_leave = Staff_Leave.objects.all()
    
    context = {
        'staff_leave' : staff_leave,
    }
        
    return render(request, 'Admin/staff_leave.html', context)

@login_required(login_url='/')
def STAFF_APPROVE_LEAVE(request ,id):
    leave = Staff_Leave.objects.get(id=id)
    leave.status  = 1
    leave.save()  
    return redirect('staff_leave_view')

@login_required(login_url='/')
def STAFF_DISAPPROVE_LEAVE( request, id):
    leave = Staff_Leave.objects.get(id=id)
    leave.status  = 2
    leave.save()  
    return redirect('staff_leave_view')

@login_required(login_url='/')
def STAFF_FEEDBACK_REPLY(request):
    feedback= Staff_Feedback.objects.all()
    
    context = {
        'feedback' : feedback,
    }
    
    return render (request , 'Admin/staff_feedback.html', context)

@login_required(login_url='/')
def STAFF_FEEDBACK_REPLY_SAVE(request):
    if request.method == 'POST':
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')
        
        feedback = Staff_Feedback.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1

        feedback.save()
        
        return redirect('staff_feedback_reply')
    
@login_required(login_url='/')
def STUDENT_SEND_NOTIFICATION(request):
    student = Student.objects.all()
    notification = Student_Notification.objects.all()
    
    context  = {
        'student' :student,
        'notification' : notification,
    }
    return render(request,'Admin/student_notification.html' , context)

@login_required(login_url='/')
def STUDENT_SAVE_NOTIFICATION(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        message = request.POST.get('message')
        
        student =Student.objects.get(admin=student_id)
        
        notification = Student_Notification(
            student_id=student,
            message = message,
        )
        notification.save()
        messages.success(request, 'Notification Are Successfully Send')
        return redirect('student_send_notification')
    

@login_required(login_url='/')
def STUDENT_FEEDBACK_REPLY(request):
    feedback= Student_Feedback.objects.all()
    
    context = {
        'feedback' : feedback,
        
    }
    
    return render (request , 'Admin/student_feedback.html', context)

@login_required(login_url='/')
def STUDENT_FEEDBACK_REPLY_SAVE(request):
    if request.method == 'POST':
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')
        
        feedback = Student_Feedback.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1
        feedback.save()
        
        return redirect('student_feedback_reply')
    

@login_required(login_url='/')
def STUDENT_LEAVE_VIEW(request):
    student_leave = Student_Leave.objects.all()
    
    context = {
        'student_leave' : student_leave,
    }
        
    return render(request, 'Admin/student_leave.html', context)

@login_required(login_url='/')
def STUDENT_APPROVE_LEAVE(request ,id):
    leave = Student_Leave.objects.get(id=id)
    leave.status  = 1
    leave.save()  
    return redirect('student_leave_view')

@login_required(login_url='/')
def STUDENT_DISAPPROVE_LEAVE( request, id):
    leave = Student_Leave.objects.get(id=id)
    leave.status  = 2
    leave.save()  
    return redirect('student_leave_view')

@login_required(login_url='/')
def VIEW_ATTENDANCE(request):
     
     subject = Subject.objects.all()
     
     session_year = Session_Year.objects.all()
     
     action = request.GET.get('action')
     
     get_subject = None
     get_session_year= None 
     attendance_date = None
     attendance_report = None
     
     if action is not None:
          if request.method == 'POST':
             subject_id = request.POST.get('subject_id')  
             session_year_id = request.POST.get('session_year_id') 
             attendance_date = request.POST.get('attendance_date')
             
             get_subject = Subject.objects.get(id = subject_id)
             get_session_year = Session_Year.objects.get(id = session_year_id)
             attendance = Attendance.objects.filter(subject_id= get_subject , attendance_date = attendance_date)
             
             #subject =Subject.objects.filter(id = subject_id)
             for i in attendance:
                 attendance_id = i.id
                 attendance_report = Attendance_Report.objects.filter(attendance_id = attendance_id)


     context = {
           'subject' : subject,
           'session_year' : session_year,
           'action' : action,
           'get_subject' : get_subject,
          'get_session_year' : get_session_year,
          'attendance_date' : attendance_date,
          'attendance_report' : attendance_report,
       }
     return render(request,'Admin/view_attendance.html', context)
