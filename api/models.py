from django.db import models

# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=10, null=False, unique=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=15)

    def __str__(self):
        return self.first_name


class BusinessClient(models.Model):
    company = models.CharField(max_length=10, null=False)
    contact = models.CharField(max_length=10, null=False)
    phone = models.CharField(max_length=10, null=False, unique=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=15)

    def __str__(self):
        return self.company


class Employee(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class PersonalAppointment(models.Model):
    appointment_date = models.DateField(null=False)
    appointment_time = models.TimeField(null=False)
    confirmed = models.BooleanField()
    date_added = models.DateTimeField()
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.client_id.first_name+self.employee_id.name


class BusinessAppointment(models.Model):
    appointment_date = models.DateField(null=False)
    appointment_time = models.TimeField(null=False)
    confirmed = models.BooleanField()
    date_added = models.DateTimeField()
    bclient_id = models.ForeignKey(BusinessClient, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.bclient_id.company+self.employee_id.name


class Company(models.Model):
    phone = models.CharField(max_length=10, null=False, unique=True)
    company = models.CharField(null=False, max_length=255)
    address = models.CharField(null=False, max_length=255)
    city = models.CharField(null=False, max_length=255)
    state = models.CharField(null=False, max_length=2)
    zipcode = models.CharField(null=False, max_length=15)
    appointment_confirm_message = models.TextField()
    appointment_cancel_message = models.TextField()
    employee_cancel_message = models.TextField()
    appointment_reminder_message = models.TextField()

    def __str__(self):
        return self.company
