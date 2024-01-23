from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPES = (
        (1, 'ADMIN'),
        (2, 'STAFF'),
        (3, 'STUDENT'),
    )

    user_type = models.CharField(choices=USER_TYPES, max_length=100, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Session_Year(models.Model):
    session_start = models.CharField(max_length=255)
    session_end = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.session_start} To {self.session_end}"

class Blood_Group(models.Model):
    blood_group = models.CharField(max_length=5)

    def __str__(self):
        return self.blood_group

class Student(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True, default=timezone.now)
    blood_group_id = models.ForeignKey(Blood_Group, on_delete=models.DO_NOTHING)
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    session_year_id = models.ForeignKey(Session_Year, on_delete=models.DO_NOTHING)
    department = models.CharField(max_length=255, null=True)
    study_year = models.IntegerField(default=0)
    mobile_no = models.BigIntegerField(default=0)
    parent_name = models.CharField(max_length=255, default = '')
    parent_mobile_no = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.admin.first_name} {self.admin.last_name}"

class Staff(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    position = models.CharField(max_length=255, null=True )
    mobile_no = models.BigIntegerField(default=0)
    highest_education = models.TextField(default = '')
    date_of_birth = models.DateField(null=True, blank=True, default=timezone.now)
    blood_group_id = models.ForeignKey(Blood_Group, on_delete=models.DO_NOTHING)
    salary = models.BigIntegerField(default=0)
    hire_date = models.DateField(null=True, blank=True)
    department = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.admin.first_name} {self.admin.last_name} - {self.department}"



class Subject(models.Model):
     name = models.CharField(max_length = 255)
     course = models.ForeignKey(Course, on_delete=models.CASCADE)
     staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
     created_at = models.DateTimeField(auto_now_add=True ,null= True)
     updated_at = models.DateTimeField(auto_now=True)
     
     def __str__(self):
        return self.name
    
    
    
class Staff_Notification(models.Model):
    staff_id = models.ForeignKey(Staff,on_delete = models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True )
    status = models.IntegerField(null=True, default = 0)
    
    def __str__(self) :
        return self.staff_id.admin.first_name + self.staff_id.admin.last_name
    

class Staff_Leave(models.Model):
           staff_id = models.ForeignKey(Staff,on_delete = models.CASCADE)
           date = models.CharField(max_length=255)
           message = models.TextField()
           status = models.IntegerField( default = 0)
           created_at = models.DateTimeField(auto_now_add=True )
           updated_at = models.DateTimeField(auto_now_add=True )
           
           def __str__(self) :
               return self.staff_id.admin.first_name + self.staff_id.admin.last_name


           
class Staff_Feedback(models.Model):
            staff_id = models.ForeignKey(Staff,on_delete = models.CASCADE)
            feedback = models.TextField()
            feedback_reply = models.TextField()
            status = models.IntegerField(null=True, default = 0)
            created_at = models.DateTimeField(auto_now_add=True )
            updated_at = models.DateTimeField(auto_now_add=True )
            
            def __str__(self) :
               return self.staff_id.admin.first_name + self.staff_id.admin.last_name

    
class Student_Notification(models.Model):
    student_id = models.ForeignKey(Student,on_delete = models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True )
    status = models.IntegerField(null=True, default = 0)
    
    def __str__(self) :
        return self.student_id.admin.first_name + self.student_id.admin.last_name
    
    
class Student_Feedback(models.Model):
            student_id = models.ForeignKey(Student,on_delete = models.CASCADE)
            feedback = models.TextField()
            feedback_reply = models.TextField()
            status = models.IntegerField(null=True, default = 0)
            created_at = models.DateTimeField(auto_now_add=True )
            updated_at = models.DateTimeField(auto_now_add=True )
            
            def __str__(self) :
               return self.student_id.admin.first_name + self.student_id.admin.last_name


class Student_Leave(models.Model):
           student_id = models.ForeignKey(Student,on_delete = models.CASCADE)
           date = models.CharField(max_length=255)
           message = models.TextField()
           status = models.IntegerField( default = 0)
           created_at = models.DateTimeField(auto_now_add=True )
           updated_at = models.DateTimeField(auto_now_add=True )
           
           def __str__(self) :
               return self.student_id.admin.first_name + self.student_id.admin.last_name

class Attendance(models.Model):
            subject_id = models.ForeignKey(Subject,on_delete = models.CASCADE)
            attendance_date= models.DateField()
            session_year_id =  models.ForeignKey(Session_Year,on_delete = models.CASCADE)
            created_at = models.DateTimeField(auto_now_add=True )
            updated_at = models.DateTimeField(auto_now_add=True )
           
            def __str__(self) :
               return self.subject_id.name

class Attendance_Report(models.Model):
    
            student_id = models.ForeignKey(Student,on_delete = models.CASCADE)
            attendance_id = models.ForeignKey(Attendance,on_delete = models.CASCADE)
            created_at = models.DateTimeField(auto_now_add=True )
            updated_at = models.DateTimeField(auto_now_add=True )
            
            def __str__(self) :
               return self.student_id.admin.first_name +  self.student_id.admin.last_name


class StudentResult(models.Model):
            student_id = models.ForeignKey(Student,on_delete = models.CASCADE)
            subject_id = models.ForeignKey(Subject,on_delete = models.CASCADE)
            assignment_mark = models.IntegerField()
            practical_mark = models.IntegerField()
            midsem_mark = models.IntegerField()
            exam_mark = models.IntegerField()
            grace_mark = models.IntegerField()
            grade_mark = models.TextField(default='None')
            created_at = models.DateTimeField(auto_now_add=True )
            updated_at = models.DateTimeField(auto_now_add=True )
                     
            def __str__(self) :
               return self.student_id.admin.first_name +  self.student_id.admin.last_name


             
    
    