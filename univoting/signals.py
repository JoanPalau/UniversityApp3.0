from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from univoting.models.course import Course
from univoting.models.subject import Subject


@receiver(post_save, sender=Subject)
def create_course(sender, instance, created, **kwargs):
    if created:
        Course.objects.create(subject_id=instance, degree_id=instance.get_degree(), course=instance.get_course())


@receiver(pre_delete, sender=Subject)
def remove_course(sender, instance, **kwargs):
        Course.objects.filter(subject_id=instance).delete()
