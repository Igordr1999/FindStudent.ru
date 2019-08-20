from rest_framework import serializers

from .models import Continent, Country, Timezone, City, University, Room, Institute, Department, Lecturer, \
    Period, StudentGroup, Sex, EmotionType, LandmarkType, Emotion, Landmark, DetectedFace, Student, \
    StudentPhoto, IdentifiedFace, UniversalIdentifiedFace, StudentSearch


class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = ('name', 'alpha2', 'image')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name', 'official_name', 'alpha2', 'alpha3', 'iso_code', 'independent', 'rating', 'area',
                  'population', 'flag')


class TimezoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timezone
        fields = ('name', 'abbr_short', 'abbr_long', 'raw_offset', 'dst_offset', 'rating')


class CitySerializer(serializers.ModelSerializer):
    continent = ContinentSerializer()
    country = CountrySerializer()
    timezone = TimezoneSerializer()

    class Meta:
        model = City
        fields = ('name', 'iata_code', 'latitude', 'longitude', 'altitude', 'capital', 'area', 'population',
                  'continent', 'country', 'timezone')


class UniversitySerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = University
        fields = ('name', 'abbr', 'latitude', 'longitude', 'student_count', 'rating', 'slogan', 'founded',
                  'website', 'logo', 'city')


class RoomSerializer(serializers.ModelSerializer):
    university = UniversitySerializer()

    class Meta:
        model = Room
        fields = ('campus', 'number', 'rating', 'university', 'location')


class InstituteSerializer(serializers.ModelSerializer):
    university = UniversitySerializer()

    class Meta:
        model = Institute
        fields = ('name', 'abbr', 'rating', 'website', 'logo', 'university')


class DepartmentSerializer(serializers.ModelSerializer):
    institute = InstituteSerializer()

    class Meta:
        model = Department
        fields = ('name', 'abbr', 'rating', 'website', 'institute')


class LecturerSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = Lecturer
        fields = ('last_name', 'first_name', 'patronymic', 'photo', 'rating', 'department')


class PeriodSerializer(serializers.ModelSerializer):
    university = UniversitySerializer()

    class Meta:
        model = Period
        fields = ('number', 'start_time', 'end_time', 'university')


class StudentGroupSerializer(serializers.ModelSerializer):
    institute = InstituteSerializer()
    department = DepartmentSerializer()

    class Meta:
        model = StudentGroup
        fields = ('name', 'group_id', 'rating', 'avatar', 'avatar_url', 'institute', 'department')


class SexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sex
        fields = ('name',)


class EmotionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmotionType
        fields = ('name',)


class LandmarkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandmarkType
        fields = ('name',)


class EmotionSerializer(serializers.ModelSerializer):
    emotion_type = EmotionTypeSerializer()

    class Meta:
        model = Emotion
        fields = ('emotion_type', 'emotion_confidence')


class LandmarkSerializer(serializers.ModelSerializer):
    landmark_type = LandmarkTypeSerializer()

    class Meta:
        model = Landmark
        fields = ('landmark_type', 'x_coordinate', 'y_coordinate')


class DetectedFaceSerializer(serializers.ModelSerializer):
    gender_value = SexSerializer()
    emotions = EmotionSerializer(many=True)
    landmarks = LandmarkSerializer(many=True)

    class Meta:
        model = DetectedFace
        fields = ('bounding_box_width', 'bounding_box_height', 'bounding_box_left', 'bounding_box_top',
                  'age_range_low', 'age_range_high', 'smile_value', 'smile_confidence',
                  'eyeglasses_value', 'eyeglasses_confidence', 'sunglasses_value', 'sunglasses_confidence',
                  'gender_value', 'gender_confidence', 'beard_value', 'beard_confidence',
                  'mustache_value', 'mustache_confidence', 'open_eyes_value', 'open_eyes_confidence',
                  'open_mouth_value', 'open_mouth_confidence', 'emotions', 'landmarks',
                  'roll_pose', 'yam_pose', 'pitch_pose', 'brightness_quality', 'sharpness_quality',
                  'confidence')


class StudentSerializer(serializers.ModelSerializer):
    sex = SexSerializer()
    city = CitySerializer()
    home_town = CitySerializer()
    university = UniversitySerializer()
    student_group = StudentGroupSerializer()

    class Meta:
        model = Student
        fields = ('last_name', 'first_name', 'user_id', 'nickname', 'birthday', 'sex', 'rating', 'real_last_name',
                  'real_first_name', 'patronymic', 'city', 'home_town', 'status', 'has_photo', 'is_closed',
                  'is_deactivated', 'avatar', 'avatar_original', 'avatar_url', 'avatar_original_url',
                  'university', 'student_group')


class StudentPhotoSerializer(serializers.ModelSerializer):
    owner = StudentSerializer()
    detected_faces = DetectedFaceSerializer(many=True)

    class Meta:
        model = StudentPhoto
        fields = ('owner', 'photo_create_date', 'detected_faces', 'photo', 'photo_url')


class IdentifiedFaceSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = IdentifiedFace
        fields = ('bounding_box_width', 'bounding_box_height', 'bounding_box_left', 'bounding_box_top',
                  'confidence', 'similarity', 'student')


class UniversalIdentifiedFaceSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    identified_faces = IdentifiedFaceSerializer(many=True)

    class Meta:
        model = UniversalIdentifiedFace
        fields = ('student', 'identified_faces')


class StudentSearchCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentSearch
        fields = ('code', 'record_create_date', 'record_update_date', 'photo', 'photo_url')


class StudentSearchSerializer(serializers.ModelSerializer):
    detected_faces = DetectedFaceSerializer(many=True)
    identified_faces = IdentifiedFaceSerializer(many=True)
    universal_identified_face = UniversalIdentifiedFaceSerializer(many=True)

    class Meta:
        model = StudentSearch
        fields = ('code', 'record_create_date', 'record_update_date', 'detected_faces', 'identified_faces',
                  'universal_identified_face', 'photo', 'photo_url')


class StudentSearchCreateByURLSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentSearch
        fields = ('code', 'record_create_date', 'photo', 'photo_url')
        read_only_fields = ('code', 'record_create_date', 'photo')


class StudentSearchCreateByPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentSearch
        fields = ('code', 'record_create_date', 'photo', 'photo_url')
        read_only_fields = ('code', 'record_create_date', 'photo_url')


