from django.db import models

class Department(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=300)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200,null=False,blank=False)
    roll_no=models.CharField(max_length=50,null=True,blank=True)
    date_of_joining=models.DateField(null=True,blank=True)
    current_semester=models.CharField(max_length=50,null=True,blank=True)
    branch=models.ForeignKey(Department,related_name="students",on_delete=models.CASCADE)
    address=models.CharField(max_length=200,null=False,blank=False)
    phone_number=models.CharField(max_length=200,null=False,blank=False)
    father_name=models.CharField(max_length=200,null=False,blank=False)
    image=models.CharField(max_length=200,null=True,blank=True)
    
    def __str__(self):
        return self.name

class Complaint(models.Model):
    id=models.AutoField(primary_key=True)
    text=models.CharField(max_length=200,null=False,blank=False)
    date_of_complaint=models.DateField(null=True,blank=True)
    student=models.ForeignKey(Student,related_name="complaints",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text+"_"+self.student.name
    
class Payment(models.Model):
    id=models.AutoField(primary_key=True)
    amount=models.CharField(max_length=10,null=False,blank=False)
    date_of_payment=models.DateField(null=False,blank=False)
    student=models.ForeignKey(Student,related_name="payments",on_delete=models.CASCADE)
    remarks=models.CharField(max_length=500)
    def __str__(self):
        return self.student.name+"-"+self.amount

    