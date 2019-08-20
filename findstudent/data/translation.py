from modeltranslation.translator import TranslationOptions, translator

from .models import Continent, Country, Timezone, City, University, StudentGroup, Room, Institute, Department, \
    Lecturer, Sex, Student, EmotionType, LandmarkType


class ContinentTranslationOptions(TranslationOptions):
    fields = ('name',)


class CountryTranslationOptions(TranslationOptions):
    fields = ('name', 'official_name',)


class TimezoneTranslationOptions(TranslationOptions):
    fields = ('name', 'abbr_long')


class CityTranslationOptions(TranslationOptions):
    fields = ('name',)


class UniversityTranslationOptions(TranslationOptions):
    fields = ('name', 'abbr', 'slogan',)


class StudentGroupTranslationOptions(TranslationOptions):
    fields = ('name',)


class RoomTranslationOptions(TranslationOptions):
    fields = ('campus',)


class InstituteTranslationOptions(TranslationOptions):
    fields = ('name', 'abbr',)


class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name', 'abbr',)


class LecturerTranslationOptions(TranslationOptions):
    fields = ('last_name', 'first_name', 'patronymic')


class SexTranslationOptions(TranslationOptions):
    fields = ('name',)


class EmotionTypeTranslationOptions(TranslationOptions):
    fields = ('name',)


class LandmarkTypeTranslationOptions(TranslationOptions):
    fields = ('name',)


class StudentTranslationOptions(TranslationOptions):
    fields = ('last_name', 'first_name', 'real_last_name', 'real_first_name', 'patronymic',)


translator.register(Continent, ContinentTranslationOptions)
translator.register(Country, CountryTranslationOptions)
translator.register(Timezone, TimezoneTranslationOptions)
translator.register(City, CityTranslationOptions)
translator.register(University, UniversityTranslationOptions)
translator.register(StudentGroup, StudentGroupTranslationOptions)
translator.register(Room, RoomTranslationOptions)
translator.register(Institute, InstituteTranslationOptions)
translator.register(Department, DepartmentTranslationOptions)
translator.register(Lecturer, LecturerTranslationOptions)
translator.register(Sex, SexTranslationOptions)
translator.register(EmotionType, EmotionTypeTranslationOptions)
translator.register(LandmarkType, LandmarkTypeTranslationOptions)
translator.register(Student, StudentTranslationOptions)
