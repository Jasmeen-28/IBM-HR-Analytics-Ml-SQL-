from django.db import models

class Employee(models.Model):

    BUSINESS_TRAVEL_CHOICES = [
        ('Travel_Rarely', 'Travel_Rarely'),
        ('Travel_Frequently', 'Travel_Frequently'),
        ('Non-Travel', 'Non-Travel'),
    ]

    DEPARTMENT_CHOICES = [
        ('Sales', 'Sales'),
        ('Research & Development', 'Research & Development'),
        ('Human Resources', 'Human Resources'),
    ]

    EDUCATION_CHOICES = [
        (1, 'Below College'),
        (2, 'College'),
        (3, 'Bachelor'),
        (4, 'Master'),
        (5, 'Doctor'),
    ]

    EDUCATION_FIELD_CHOICES = [
        ('Life Sciences', 'Life Sciences'),
        ('Medical', 'Medical'),
        ('Marketing', 'Marketing'),
        ('Technical Degree', 'Technical Degree'),
        ('Human Resources', 'Human Resources'),
        ('Other', 'Other'),
    ]

    ENVIRONMENT_SATISFACTION = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4')
        
    ]
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    JOB_INVOLVE = [
        (1, '1'),
        (2,'2'),
        (3, '3'),
        (4, '4')
    ]

    JOB_LEVEL = [
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5')
    ]

    JOB_ROLE_CHOICES = [
        ('Manufacturing Director', 'Manufacturing Director'),
        ('Research Scientist', 'Research Scientist'),
        ('Research Director', 'Research Director'),
        ('Laboratory Technician', 'Laboratory Technician'),
        ('Sales Executive', 'Sales Executive'),
        ('Healthcare Representative', 'Healthcare Representative'),
        ('Manager', 'Manager'),
        ('Human Resources', 'Human Resources'),
        ('Sales Representative', 'Sales Representative'),
    ]

    JOB_SAT = [
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
    ]

    OVERTIME_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    PERFOR = [
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
    ]

    RSS = [
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
    ]

    STOCK_OPTION_CHOICES = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
    ]

    TRAINING_TIMES_CHOICES = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
    ]

    WORK = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
    ]

    
    Age = models.IntegerField()
    BusinessTravel = models.CharField(max_length=50, choices=BUSINESS_TRAVEL_CHOICES, default='Travel_Rarely')
    DailyRate = models.IntegerField(help_text='Daily Wage..')
    Department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, default='Sales')
    DistanceFromHome = models.IntegerField(default=10)
    Education = models.IntegerField(choices=EDUCATION_CHOICES, default=3)
    EducationField = models.CharField(max_length=50, choices=EDUCATION_FIELD_CHOICES, default='Life Sciences')
    EnvironmentSatisfaction = models.IntegerField(choices= ENVIRONMENT_SATISFACTION, default=4, help_text="1: Low, 2: Medium, 3: high, 4: Very High")
    Gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    HourlyRate = models.IntegerField(default=93, help_text='Hourly wage (for hourly roles)...')
    JobInvolvement = models.IntegerField(default=4, choices= JOB_INVOLVE, help_text="1: Low, 2: Medium, 3: high, 4: Very High" )
    JobLevel = models.IntegerField( choices= JOB_LEVEL,help_text="1: Entry Level, 2: Mid-Level, 3: Senior Level, 4: Lead, 5: Executive")
    JobRole = models.CharField(max_length=50, choices=JOB_ROLE_CHOICES, default='Sales Executive')
    JobSatisfaction = models.IntegerField(choices=JOB_SAT, help_text="1: Low, 2: Medium, 3: high, 4: Very High")
    MaritalStatus = models.CharField(max_length=50, choices=MARITAL_STATUS_CHOICES, default='Single') 
    MonthlyIncome = models.IntegerField(help_text = 'Enter You Monthly Salary.....')
    MonthlyRate = models.IntegerField(help_text = 'Enter Your Performance Based salary...')   
    NumCompaniesWorked = models.IntegerField(help_text = 'Enter No. of companies you Worked..') 
    OverTime = models.CharField(max_length=10, choices=OVERTIME_CHOICES, default='No')
    PercentSalaryHike = models.IntegerField('How many % salary hike did you get..') 
    PerformanceRating = models.IntegerField(help_text="1: Low, 2: Good, 3: Excellent, 4: Outstanding", choices=PERFOR)
    RelationshipSatisfaction = models.IntegerField(default=4,  help_text="1: Low, 2: Medium, 3: high, 4: Very High", choices=RSS)
    StockOptionLevel = models.IntegerField(choices=STOCK_OPTION_CHOICES, default=0, help_text="0: None, 1: Low, 2: Medium, 3: High")  
    TotalWorkingYears = models.IntegerField(help_text='Enter your Total Working Years...')
    TrainingTimesLastYear = models.IntegerField(choices=TRAINING_TIMES_CHOICES, default=3) 
    WorkLifeBalance = models.IntegerField(choices=WORK, default=3, help_text="1: Bad, 2: Good, 3: Better, 4: Best") 
    YearsAtCompany = models.IntegerField(help_text = 'No. of years at company..')
    YearsInCurrentRole = models.IntegerField(help_text = 'No. of years in current role..')
    YearsSinceLastPromotion = models.IntegerField(help_text = 'No. of years since last promotion..')
    YearsWithCurrManager = models.IntegerField(help_text = 'No. of years with manager...')

    # Prediction output field
    Attrition = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"Employee {self.id}"
