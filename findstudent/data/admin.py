from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Continent, Country, Timezone, City, University, StudentGroup, Room, Institute, Department, \
    Lecturer, Period, Sex, Student, StudentPhoto, EmotionType, LandmarkType, Emotion, Landmark, DetectedFace, \
    IdentifiedFace, StudentSearch, UniversalIdentifiedFace


@admin.register(Continent)
class ContinentAdmin(TranslationAdmin):
    list_display = ['name_en', 'name_ru', 'name_de', 'alpha2']


@admin.register(Country)
class CountryAdmin(TranslationAdmin):
    list_display = ['name_en', 'name_ru', 'name_de', 'alpha2', 'alpha3', 'iso_code', 'area', 'population',
                    'rating']
    list_filter = ['name_en']


@admin.register(Timezone)
class TimezoneAdmin(TranslationAdmin):
    list_display = ['name_en', 'name_ru', 'name_de', 'abbr_long_en', 'abbr_long_ru', 'abbr_long_de', 'abbr_short',
                    'raw_offset', 'dst_offset', 'rating']


@admin.register(City)
class CityAdmin(TranslationAdmin):
    list_display = ['name_en', 'name_ru', 'name_de', 'iata_code', 'latitude', 'longitude', 'altitude', 'area',
                    'population', 'capital', 'rating']
    list_filter = ['continent', 'country']


@admin.register(University)
class UniversityAdmin(TranslationAdmin):
    list_display = ['name_en', 'name_ru', 'name_de', 'abbr_en', 'student_count', 'founded',
                    'latitude', 'longitude', 'rating']
    list_filter = ['city']


@admin.register(StudentGroup)
class StudentGroupAdmin(TranslationAdmin):
    list_display = ['name_en', 'name_ru', 'name_de', 'group_id', 'rating']
    list_filter = ['institute', 'department']


@admin.register(Room)
class RoomAdmin(TranslationAdmin):
    list_display = ['campus_en', 'number', 'rating']
    list_filter = ['university']


@admin.register(Institute)
class InstituteAdmin(TranslationAdmin):
    list_display = ['name_en', 'name_ru', 'name_de', 'abbr_en', 'rating']
    list_filter = ['university']


@admin.register(Department)
class DepartmentAdmin(TranslationAdmin):
    list_display = ['name_en', 'name_ru', 'name_de', 'abbr_en', 'rating']
    list_filter = ['institute']


@admin.register(Lecturer)
class LecturerAdmin(TranslationAdmin):
    list_display = ['last_name_en', 'first_name_en', 'rating']
    list_filter = ['department__abbr']


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ['number', 'start_time', 'end_time']
    list_filter = ['university']


@admin.register(Sex)
class SexAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'sex', 'birthday', 'user_id', 'nickname',
                    'has_photo', 'is_closed', 'city', 'home_town']
    list_filter = ['student_group']


@admin.register(StudentPhoto)
class StudentPhotoAdmin(admin.ModelAdmin):
    list_display = ['owner', 'photo_create_date', 'record_create_date', 'record_update_date']
    list_filter = ['owner__student_group']
    search_fields = ['owner__last_name']


@admin.register(EmotionType)
class EmotionTypeAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_ru', 'system_name']


@admin.register(LandmarkType)
class LandmarkTypeAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_ru', 'system_name']


@admin.register(Emotion)
class EmotionAdmin(admin.ModelAdmin):
    list_display = ['emotion_type', 'emotion_confidence']


@admin.register(Landmark)
class LandmarkAdmin(admin.ModelAdmin):
    list_display = ['landmark_type', 'x_coordinate', 'y_coordinate']


@admin.register(DetectedFace)
class FaceDetailAdmin(admin.ModelAdmin):
    list_display = ['face_id', 'image_id', 'age_range_low', 'age_range_high']


@admin.register(IdentifiedFace)
class FaceDetailSearchAdmin(admin.ModelAdmin):
    list_display = ['face_id', 'image_id', 'student']


@admin.register(StudentSearch)
class StudentSearchAdmin(admin.ModelAdmin):
    list_display = ['owner', 'record_create_date', 'record_update_date', 'code', 'photo_url']


@admin.register(UniversalIdentifiedFace)
class StudentUniversalSearchDetailsAdmin(admin.ModelAdmin):
    list_display = ['student']
