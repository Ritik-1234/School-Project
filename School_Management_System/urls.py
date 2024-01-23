"""
URL configuration for School_Management_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import view,Admin_view,Staff_view,Students_view,Teacher_view,Parents_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',view.BASE, name='base'),
    #login path
    path('',view.LOGIN, name='login'),
    path('doLogin',view.doLogin, name='doLogin'),
    path('doLogout',view.doLogout, name='logout'),
    
    # profile updtate
    path('profile',view.PROFILE , name='profile'),
    path('profile/update',view.PROFILE_UPDATE,name='profile_update'),



    # This is hod panel url
    
    # this is staff 
    path('Admin/Staff/Add',Admin_view.ADD_STAFF,name='add_staff'),
    path('Admin/Staff/View',Admin_view.VIEW_STAFF,name='view_staff'),
    path('Admin/Staff/Edit/<str:id>',Admin_view.EDIT_STAFF,name='edit_staff'),
    path('Admin/Staff/Update',Admin_view.UPDATE_STAFF,name='update_staff'),
    path('Admin/Staff/Delete/<str:admin>',Admin_view.DELETE_STAFF,name='delete_staff'),

    
    
    
    
    # this is student
    path('Admin/Home', Admin_view.HOME, name='Admin_home'),
    path('Admin/Student/Add',Admin_view.ADD_STUDENT,name='add_student'),
    path('Admin/Student/View',Admin_view.VIEW_STUDENT,name='view_student'),
    path('Admin/Student/Edit/<str:id>',Admin_view.EDIT_STUDENT,name='edit_student'),
    path('Admin/Student/Update',Admin_view.UPDATE_STUDENT,name='update_student'),
    path('Admin/Student/Delete/<str:admin>',Admin_view.DELETE_STUDENT,name='delete_student'),
    
    # this is course 
    path('Admin/Course/Add', Admin_view.ADD_COURSE,name='add_course'),
    path('Admin/Course/View', Admin_view.VIEW_COURSE,name='view_course'),
    path('Admin/Course/Edit/<str:id>', Admin_view.EDIT_COURSE,name='edit_course'),
    path('Admin/Course/Delete/<str:id>', Admin_view.DELETE_COURSE,name='delete_course'),

   # for subject
   
    path('Admin/Subject/Add', Admin_view.ADD_SUBJECT,name='add_subject'),
    path('Admin/Subject/View', Admin_view.VIEW_SUBJECT,name='view_subject'),
    path('Admin/Subject/Edit/<str:id>',Admin_view.EDIT_SUBJECT,name='edit_subject'),
    path('Admin/Subject/Update', Admin_view.UPDATE_SUBJECT,name='update_subject'),
    path('Admin/Subject/Delete/<str:id>',Admin_view.DELETE_SUBJECT,name='delete_subject'),

 # for session
 
     path('Admin/Session/Add', Admin_view.ADD_SESSION,name='add_session'),
     path('Admin/Session/View', Admin_view.VIEW_SESSION,name='view_session'),
     path('Admin/Session/Edit/<str:id>',Admin_view.EDIT_SESSION,name='edit_session'),
     path('Admin/Session/Update', Admin_view.UPDATE_SESSION,name='update_session'),
     path('Admin/Session/Delete/<str:id>',Admin_view.DELETE_SESSION,name='delete_session'),
     
# for notification
     
     path ('Admin/Staff/Send_Notification' , Admin_view.STAFF_SEND_NOTIFICATION, name = 'staff_send_notification'),
     path ('Admin/Staff/Save_Notification' , Admin_view.STAFF_SAVE_NOTIFICATION, name = 'staff_save_notification'),
     
     path ('Admin/Student/Send_Notification' , Admin_view.STUDENT_SEND_NOTIFICATION, name = 'student_send_notification'),
     path ('Admin/Student/Save_Notification' , Admin_view.STUDENT_SAVE_NOTIFICATION, name = 'student_save_notification'),
     
     
# for leave  
     path('Admin/Staff/Leave_View', Admin_view.STAFF_LEAVE_VIEW, name='staff_leave_view'),
     path('Admin/Staff/Approve_Leave/<str:id>', Admin_view.STAFF_APPROVE_LEAVE, name='staff_approve_leave'),
     path('Admin/Staff/Disapprove_Leave/<str:id>', Admin_view.STAFF_DISAPPROVE_LEAVE, name='staff_disapprove_leave'),
     
     
     path('Admin/Student/Leave_View', Admin_view.STUDENT_LEAVE_VIEW, name='student_leave_view'),
     path('Admin/Student/Approve_Leave/<str:id>', Admin_view.STUDENT_APPROVE_LEAVE, name='student_approve_leave'),
     path('Admin/Student/Disapprove_Leave/<str:id>', Admin_view.STUDENT_DISAPPROVE_LEAVE, name='student_disapprove_leave'),
     

# for feedback
     path('Admin/Staff/Feedback', Admin_view.STAFF_FEEDBACK_REPLY, name='staff_feedback_reply'),
     path('Admin/Staff/Feedback/save', Admin_view.STAFF_FEEDBACK_REPLY_SAVE, name='staff_feedback_reply_save'),
     
    
     path('Admin/Student/Feedback', Admin_view.STUDENT_FEEDBACK_REPLY, name='student_feedback_reply'),
     path('Admin/Student/Feedback/save', Admin_view.STUDENT_FEEDBACK_REPLY_SAVE, name='student_feedback_reply_save'),
     
     # view attendance 
     path('Admin/View_Attendance', Admin_view.VIEW_ATTENDANCE, name = 'view_attendance'),


    
# for staff panel
     path('Staff/Home', Staff_view.HOME, name='staff_home'),
     # for notification
     path('Staff/Notification', Staff_view.NOTIFICATION, name='notification'),
     path('Staff/mark_as_read/<str:status>', Staff_view.STAFF_NOTIFICATION_MARK_READ, name='staff_notification_mark_read'),
     
     # for apply leave
     path('Staff/Apply_leave', Staff_view.STAFF_APPLY_LEAVE, name='staff_apply_leave'),
     path('Staff/Apply_leave_save', Staff_view.STAFF_APPLY_LEAVE_SAVE, name='staff_apply_leave_save'),

     # for feedback
     
     path('Staff/Feedback', Staff_view.STAFF_FEEDBACK, name = 'staff_feedback'),
     path('Staff/Feedback/Save',Staff_view.STAFF_FEEDBACK_SAVE, name = 'staff_feedback_save'),
     
# for attendance
     path('Staff/Take_Attendance', Staff_view.STAFF_TAKE_ATTENDANCE, name = 'staff_take_attendance'),
     path('Staff/Save_Attendance', Staff_view.STAFF_SAVE_ATTENDANCE, name = 'staff_save_attendance'),
     path('Staff/View_Attendance', Staff_view.STAFF_VIEW_ATTENDANCE, name = 'staff_view_attendance'),

# add result
     path('Staff/Add_Result', Staff_view.STAFF_ADD_RESULT, name='staff_add_result'),
     path('Staff/Save_Result', Staff_view.STAFF_SAVE_RESULT, name='staff_save_result'),


        


# for student

     path('Student/Home', Students_view.HOME, name = 'student_home'),
     path('Student/Notification', Students_view.STUDENT_NOTIFICATION, name='student_notification'),
     path('Student/mark_as_read/<str:status>', Students_view.STUDENT_NOTIFICATION_MARK_READ, name='student_notification_mark_read'),

     path('Student/Feedback', Students_view.STUDENT_FEEDBACK, name = 'student_feedback'),
     path('Student/Feedback/Save',Students_view.STUDENT_FEEDBACK_SAVE, name = 'student_feedback_save'),
     
     path('Student/Apply_leave', Students_view.STUDENT_APPLY_LEAVE, name='student_apply_leave'),
     path('Student/Apply_leave_save', Students_view.STUDENT_APPLY_LEAVE_SAVE, name='student_apply_leave_save'),

#view attendance
     path('Student/View_Attendance', Students_view.STUDENT_VIEW_ATTENDANCE, name = 'student_view_attendance'),

# view result
     path('Student/View_Result', Students_view.STUDENT_VIEW_RESULT, name = 'student_view_result'),



    ] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


