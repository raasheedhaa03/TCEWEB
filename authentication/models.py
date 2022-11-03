from tabnanny import verbose
from django.db import models

# Create your models here.
class dept(models.Model):
    dept_name=models.CharField(max_length=10,verbose_name='Department')

class dept_events(models.Model):
    title=models.CharField(max_length=30,verbose_name='Title')
    venue=models.CharField(max_length=60,verbose_name='Venue',default='NULL')
    hover_description= models.TextField(default='', blank=True, null= True,verbose_name='Hover Description')
    time=models.CharField(max_length=30,verbose_name='Time',default='')
    image= models.ImageField(upload_to='static/dept',verbose_name='Image')
    conducted_by=models.CharField(max_length=30,verbose_name='Organized By')
    date=models.DateField(blank=True, null= True,verbose_name='Date')
    dashboard= models.ForeignKey(dept,on_delete=models.CASCADE,default=1,verbose_name='Department' )
    rules=models.TextField(verbose_name='Rules',default='')
    description=models.TextField(default='',verbose_name='Description')
    rewards=models.TextField(verbose_name='Rewards',default='')
    OD_CHOICES=[
        ('OD will be Provided','OD will be Provided'),
        ('OD will not be Provided','OD will not be Provided'),
    ]
    PARTICIPATIONTYPE_CHOICES=[
        ('Individual','Individual'),
        ('Team size-2','Team size-2'),
        ('Team size-3','Team size-3'),
        ('Team size-4','Team size-4'),
        ('Team size-5','Team size-5'),
        ('Team size-6','Team size-6'),
    ]
    PARTICIPANTS_CHOICES=[
        ('Inter-departmental','Inter-departmental'),
        ('Intra-departmental','Intra-departmental'),
    ]
    participants=models.CharField(max_length=40,verbose_name='Inter or Intra',choices=PARTICIPANTS_CHOICES,default='Intradepartmental')
    OD=models.CharField(max_length=40,verbose_name='Info about OD',choices=OD_CHOICES,default='OD will not be Provided')
    participation_type=models.CharField(max_length=40,verbose_name='Type of Participation',choices=PARTICIPATIONTYPE_CHOICES,default='Individual')
    contact_details=models.TextField(verbose_name='Contact details',default='')
    link=models.URLField(verbose_name='Registration Link',default='')

class clubs(models.Model):
    club_name=models.CharField(max_length=20,verbose_name='club name',default='')
    gs=models.CharField(max_length=20,verbose_name='GS',default='')
    gt=models.CharField(max_length=20,verbose_name='GT',default='')
    js=models.CharField(max_length=20,verbose_name='JS',default='')
    jt=models.CharField(max_length=20,verbose_name='JT',default='')
    gsn=models.CharField(max_length=20,verbose_name='GS Num',default='')
    gtn=models.CharField(max_length=20,verbose_name='GT Num',default='')
    jsn=models.CharField(max_length=20,verbose_name='JS Num',default='')
    jtn=models.CharField(max_length=20,verbose_name='JT Num',default='')
    desc=models.TextField(verbose_name='Description',default='')
    image=models.ImageField(upload_to='static/club',verbose_name='Image')
    whatsapp=models.URLField(verbose_name='Whatsapp Link',default='')
    instagram_link=models.URLField(verbose_name='Instagram Link',default='')

class club_events(models.Model):
    title=models.CharField(max_length=30,verbose_name='Title')
    venue=models.CharField(max_length=60,verbose_name='Venue')
    image= models.ImageField(upload_to='static/clubevents',verbose_name='Image')
    date=models.DateField(blank=True, null= True,verbose_name='Date')
    description=models.TextField(default='',verbose_name='Description')
    time=models.CharField(max_length=20,verbose_name='Time')
    contact_details=models.TextField(verbose_name='Contact details')
    clubs= models.ForeignKey(clubs,on_delete=models.CASCADE,default=1,verbose_name='Club')

class achievers(models.Model):
    dep_event_name=models.CharField(max_length=30,verbose_name='Event Name')
    first=models.CharField(max_length=30,verbose_name='1 Name-regno')
    second=models.CharField(max_length=30,verbose_name='2 Name-regno')
    third=models.CharField(max_length=30,verbose_name='3 Name-regno')
    first_dept=models.CharField(max_length=30,verbose_name='1st Department name')
    second_dept=models.CharField(max_length=30,verbose_name='2nd Department name')
    third_dept=models.CharField(max_length=30,verbose_name='3rd Department name')
    dept=models.ForeignKey(dept,on_delete=models.CASCADE,default=1,verbose_name='Event belongs to' )
    image1=models.ImageField(upload_to='static/ach',verbose_name='Image1')
    image2=models.ImageField(upload_to='static/ach',verbose_name='Image2')
    image3=models.ImageField(upload_to='static/ach',verbose_name='Image3')


