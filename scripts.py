import random


from datacenter.models import Schoolkid, Mark, Chastisement
from datacenter.models import Lesson, Commendation
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist


text_commendations = [
    'Молодец!',
    'Отлично!',
    'Хорошо!',
    'Гораздо лучше, чем я ожидал!',
    'Ты меня приятно удивил!',
    'Великолепно!',
    'Прекрасно!',
    'Ты, как всегда, точен!',
    'Очень хороший ответ!',
    'Талантливо!',
    'Ты сегодня прыгнул выше головы!',
]


def get_schoolkid(full_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=full_name)
        return schoolkid
    except ObjectDoesNotExist:
        print('Ученик не найден.')
    except MultipleObjectsReturned:
        print('Найдено более одного ученика, попробуйте уточнить запрос.')


def fix_marks(schoolkid):
    schoolkid_bad_marks = Mark.objects.filter(
        schoolkid=schoolkid, points__in=[2,3]
    )
    for mark in schoolkid_bad_marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid):
    schoolkid_chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    schoolkid_chastisements.delete()


def create_commendation(schoolkid, subject_name):
    subject = Subject.objects.get(
        title=subject_name,
        year_of_study=schoolkid.year_of_study
    )

    lesson = Lesson.objects.filter(
        subject=subject,
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter
    ).order_by('-date').first()

    new_commendation = Commendation.objects.create(
        text=random.choice(text_commendations),
        created=lesson.date,
        schoolkid=schoolkid,
        teacher_id=lesson.teacher.id,
        subject=lesson.subject
    )

    new_commendation.save()
