from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Language(models.Model):
    code = models.CharField()
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.title}: {self.code}"
    
    class Meta:
        verbose_name = "Язык программирования"
        verbose_name_plural = "Языки программирования"

class Task(models.Model): 
    title = models.CharField(max_length=255)
    description = models.TextField()
    time_limit = models.IntegerField()
    
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, 
        related_name = "created_tasks", 
        on_delete=models.CASCADE)
    
    languages = models.ManyToManyField(Language, through="TaskLanguage", related_name="tasks")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

class TaskLanguage(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ("task", "language")
    
    def __str__(self):
        return f"{self.task_id} -> {self.language.code}"
    
class TaskTest(models.Model):
    input_data = models.TextField()
    expected_output = models.TextField()
    
    task = models.ForeignKey(Task, on_delete=models.CASCADE,related_name="tests")
    
    def __str__(self):
        return f"Тест №{self.id} для задачи #{self.task}"
    
    class Meta: 
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"

class Submission(models.Model):
    submitted_at = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ('RUNNING', 'Проверка...'),
        ('AC', 'Все ок'),
        ('FAILED', 'Не прошел тесты'),
        ('CE', 'Ошибка компиляции'),
        ('RE', 'Упал во время теста'),
        ('TLE', 'Программа работает слишком долго'),
        ('MLE', 'Программа съела слишком много памяти'),
        ('SYSTEM_ERROR', 'Ошибка в системе')
    ]
    status = models.CharField(choices=status_choices, default='RUNNING')
    compiler_output = models.TextField(null=True, blank=True)
    source_code = models.TextField()
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             on_delete=models.CASCADE,
                             related_name='submissions')
    task = models.ForeignKey(Task, 
                             on_delete= models.CASCADE,
                             related_name='submissions')
    language = models.ForeignKey(Language, 
                                 on_delete=models.CASCADE,
                                 related_name='submissions')
    
    
    
    
    
    
    
# class Submission(models.Model):
#     submitted_at = models.DateTimeField(auto_now_add=True)
    
    
#     STATUS_CHOICES = [
#         # ("DRAFT", "Черновик")
#         ("RUNNING", "Проверка..."),
#         ("AC", "Все ок"),
#         # ("TLE", "Превысил время"),
#         # ("RE", "Упал во время компиляции"),
#         # ("CE", 'Не скомпилировалось'),
#         # ("SYSTEM_ERROR", "Ошибка в системе")
#         ("ERROR_TESTS", "Не прошел тесты")
#     ]
#     status = models.CharField(choices=STATUS_CHOICES, default="RUNNING")
#     compiler_output = models.TextField(null=True, blank=True)
#     source_code = models.TextField()
    
    
    
    


    
    
    