from django.shortcuts import render ,redirect
from School.models import Course, Session_Year, CustomUser, Student, Subject,   Student_Notification, Student_Feedback , Student_Leave, Attendance, Attendance_Report, StudentResult
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def HOME(request):
    
    return render(request, 'Students/home.html')

@login_required(login_url='/')
def STUDENT_NOTIFICATION(request):
    student = Student.objects.filter(admin= request.user.id)
    for i in student:
          # print(i.id)
          student_id = i.id
      
          notification = Student_Notification.objects.filter(student_id= student_id)    
          
          context = {
               'notification' :notification,
          }
     
          return render(request, 'Students/notification.html', context)
        
@login_required(login_url='/')
def STUDENT_NOTIFICATION_MARK_READ (request, status):
     notification = Student_Notification.objects.get(id= status) 
     notification.status = 1
     notification.save()

     return redirect('student_notification')
 
@login_required(login_url='/')
def STUDENT_FEEDBACK(request):
    student_id  = Student.objects.get(admin = request.user.id)
     
    feedback_history = Student_Feedback.objects.filter(student_id = student_id)
     
    context= {
         'feedback_history' : feedback_history,
     }
     
    return render(request, 'Students/feedback.html', context)

@login_required(login_url='/')
def STUDENT_FEEDBACK_SAVE(request):
     if request.method == 'POST':
        feedback = request.POST.get('feedback') 
        student = Student.objects.get(admin = request.user.id)
        
        feedbacks = Student_Feedback(
             student_id = student,
             feedback = feedback,
             feedback_reply = "",
        )
        feedbacks.save()
     
        return redirect('student_feedback')

@login_required(login_url='/')
def STUDENT_APPLY_LEAVE(request):
     student = Student.objects.filter(admin = request.user.id)
     for i in student:
          student_id = i.id
          
          staff_leave_history = Student_Leave.objects.filter(student_id= student_id)
          
          context = {
               'staff_leave_history': staff_leave_history,
          }
     return render(request,'Students/apply_leave.html', context)

@login_required(login_url='/')
def STUDENT_APPLY_LEAVE_SAVE(request):
     if request.method == 'POST':
         leave_date = request.POST.get('leave_date')
         leave_reason = request.POST.get('leave_reason')
         
         student = Student.objects.get(admin = request.user.id)
         
         leave = Student_Leave(
              student_id = student,
              date = leave_date,
              message = leave_reason,
         )
         
         leave.save()
         messages.success(request, 'Apply Leave Successfully Send')

         return redirect('student_apply_leave')
    
@login_required(login_url='/')
def STUDENT_VIEW_ATTENDANCE (request):
     student = Student.objects.get(admin = request.user.id)
     subject = Subject.objects.filter(course= student.course_id)
     
     action = request.GET.get('action')
     
     get_subject = None
     attendance_report = None
     
     if action is not None:
          if request.method == 'POST':
             subject_id = request.POST.get('subject_id')  
             get_subject = Subject.objects.get(id = subject_id)
             attendance_report = Attendance_Report.objects.filter(student_id = student,attendance_id__subject_id= subject_id )
    
     context = {
          'subject' : subject,
          'action': action,
          'get_subject' : get_subject,
          'attendance_report' : attendance_report,
     }
     return render(request, 'Students/view_attendance.html' , context)

@login_required(login_url='/')
def STUDENT_VIEW_RESULT(request):
    student = Student.objects.get(admin=request.user.id)
    
    result = StudentResult.objects.filter(student_id=student)
    total_mark = None
    for i in result:
        exam_mark = i.exam_mark
        assignment_mark = i.assignment_mark
        grace_mark = i.grace_mark
        midsem_mark = i.midsem_mark
        practical_mark = i.practical_mark
        
        total_mark = exam_mark + assignment_mark + grace_mark + midsem_mark + practical_mark

    context = {
        'result': result,
        'total_mark': total_mark,
    }
    return render(request, 'Students/view_result.html', context)
