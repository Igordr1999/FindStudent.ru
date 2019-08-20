from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics

from .models import Continent, Country, Timezone, City, University, Room, Institute, Department, Lecturer, \
    Period, StudentGroup, Sex, EmotionType, LandmarkType, Emotion, Landmark, DetectedFace, Student, \
    StudentPhoto, IdentifiedFace, UniversalIdentifiedFace, StudentSearch
from .serializers import ContinentSerializer, CountrySerializer, TimezoneSerializer, CitySerializer, \
    UniversitySerializer, RoomSerializer, InstituteSerializer, DepartmentSerializer, LecturerSerializer, \
    PeriodSerializer, StudentGroupSerializer, SexSerializer, EmotionTypeSerializer, LandmarkTypeSerializer, \
    EmotionSerializer, LandmarkSerializer, DetectedFaceSerializer, StudentSerializer, StudentPhotoSerializer, \
    IdentifiedFaceSerializer, UniversalIdentifiedFaceSerializer, StudentSearchSerializer, StudentSearchCodeSerializer, \
    StudentSearchCreateByURLSerializer, StudentSearchCreateByPhotoSerializer


class ContinentListView(generics.ListAPIView):
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('name', 'alpha2')
    ordering_fields = ('name', 'alpha2')
    search_fields = ('name', 'alpha2')


class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('name', 'official_name', 'alpha2', 'alpha3', 'iso_code', 'independent', 'rating', 'area',
                     'population')
    ordering_fields = ('name', 'official_name', 'alpha2', 'alpha3', 'iso_code', 'independent', 'rating', 'area',
                       'population')
    search_fields = ('name', 'official_name', 'alpha2', 'alpha3', 'iso_code', 'independent', 'rating', 'area',
                     'population')


class TimezoneListView(generics.ListAPIView):
    queryset = Timezone.objects.all()
    serializer_class = TimezoneSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('name', 'abbr_short', 'abbr_long', 'raw_offset', 'dst_offset', 'rating')
    ordering_fields = ('name', 'abbr_short', 'abbr_long', 'raw_offset', 'dst_offset', 'rating')
    search_fields = ('name', 'abbr_short', 'abbr_long', 'raw_offset', 'dst_offset', 'rating')


class CityListView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('name', 'iata_code', 'latitude', 'longitude', 'altitude', 'capital', 'area', 'population',
                     'continent__name', 'country__name', 'timezone__name')
    ordering_fields = ('name', 'iata_code', 'latitude', 'longitude', 'altitude', 'capital', 'area', 'population',
                       'continent__name', 'country__name', 'timezone__name')
    search_fields = ('name', 'iata_code', 'latitude', 'longitude', 'altitude', 'capital', 'area', 'population',
                     'continent__name', 'country__name', 'timezone__name')


class UniversityListView(generics.ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('name', 'abbr', 'latitude', 'longitude', 'student_count', 'rating', 'slogan', 'founded',
                     'website', 'city__name')
    ordering_fields = ('name', 'abbr', 'latitude', 'longitude', 'student_count', 'rating', 'slogan', 'founded',
                       'website', 'city__name')
    search_fields = ('name', 'abbr', 'latitude', 'longitude', 'student_count', 'rating', 'slogan', 'founded',
                     'website', 'city__name')


class RoomListView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('campus', 'number', 'rating', 'university__name')
    ordering_fields = ('campus', 'number', 'rating', 'university__name')
    search_fields = ('campus', 'number', 'rating', 'university__name')


class InstituteListView(generics.ListAPIView):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('name', 'abbr', 'rating', 'website', 'university__name')
    ordering_fields = ('name', 'abbr', 'rating', 'website', 'university__name')
    search_fields = ('name', 'abbr', 'rating', 'website', 'university__name')


class DepartmentListView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('name', 'abbr', 'rating', 'website', 'institute__name')
    ordering_fields = ('name', 'abbr', 'rating', 'website', 'institute__name')
    search_fields = ('name', 'abbr', 'rating', 'website', 'institute__name')


class LecturerListView(generics.ListAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('last_name', 'first_name', 'patronymic', 'rating', 'department__name')
    ordering_fields = ('last_name', 'first_name', 'patronymic', 'rating', 'department__name')
    search_fields = ('last_name', 'first_name', 'patronymic', 'rating', 'department__name')


class PeriodListView(generics.ListAPIView):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('number', 'start_time', 'end_time', 'university__name')
    ordering_fields = ('number', 'start_time', 'end_time', 'university__name')
    search_fields = ('number', 'start_time', 'end_time', 'university__name')


class StudentGroupListView(generics.ListAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('name', 'group_id', 'rating', 'avatar_url', 'institute__name', 'department__name')
    ordering_fields = ('name', 'group_id', 'rating', 'avatar_url', 'institute__name', 'department__name')
    search_fields = ('name', 'group_id', 'rating', 'avatar_url', 'institute__name', 'department__name')


class SexListView(generics.ListAPIView):
    queryset = Sex.objects.all()
    serializer_class = SexSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('name',)
    ordering_fields = ('name',)
    search_fields = ('name',)


class EmotionTypeListView(generics.ListAPIView):
    queryset = EmotionType.objects.all()
    serializer_class = EmotionTypeSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('name',)
    ordering_fields = ('name',)
    search_fields = ('name',)


class LandmarkTypeListView(generics.ListAPIView):
    queryset = LandmarkType.objects.all()
    serializer_class = LandmarkTypeSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('name',)
    ordering_fields = ('name',)
    search_fields = ('name',)


class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('last_name', 'first_name', 'user_id', 'nickname', 'birthday', 'sex__name', 'rating',
                     'real_last_name', 'real_first_name', 'patronymic', 'city__name', 'home_town__name',
                     'status', 'has_photo', 'is_closed', 'is_deactivated', 'avatar_url', 'avatar_original_url',
                     'university__name', 'student_group__name')
    ordering_fields = ('last_name', 'first_name', 'user_id', 'nickname', 'birthday', 'sex__name', 'rating',
                       'real_last_name', 'real_first_name', 'patronymic', 'city__name', 'home_town__name',
                       'status', 'has_photo', 'is_closed', 'is_deactivated', 'avatar_url', 'avatar_original_url',
                       'university__name', 'student_group__name')
    search_fields = ('last_name', 'first_name', 'user_id', 'nickname', 'birthday', 'sex__name', 'rating',
                     'real_last_name', 'real_first_name', 'patronymic', 'city__name', 'home_town__name',
                     'status', 'has_photo', 'is_closed', 'is_deactivated', 'avatar_url', 'avatar_original_url',
                     'university__name', 'student_group__name')


class StudentPhotoListView(generics.ListAPIView):
    queryset = StudentPhoto.objects.all()
    serializer_class = StudentPhotoSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('owner__last_name', 'owner__first_name', 'owner__user_id', 'owner__nickname',
                     'photo_create_date', 'photo_url')
    ordering_fields = ('owner__last_name', 'owner__first_name', 'owner__user_id', 'owner__nickname',
                       'photo_create_date', 'photo_url')
    search_fields = ('owner__last_name', 'owner__first_name', 'owner__user_id', 'owner__nickname',
                     'photo_create_date', 'photo_url')


class StudentSearchCodeView(generics.ListAPIView):
    serializer_class = StudentSearchCodeSerializer
    filter_fields = ('code', 'record_create_date', 'record_update_date', 'photo_url')
    ordering_fields = ('code', 'record_create_date', 'record_update_date', 'photo_url')
    search_fields = ('code', 'record_create_date', 'record_update_date', 'photo_url')

    def get_queryset(self):
        return StudentSearch.objects.filter(owner_id=self.request.user.id)


class StudentSearchListView(generics.ListAPIView):
    serializer_class = StudentSearchSerializer
    filter_fields = ('code', 'record_create_date', 'record_update_date', 'photo_url')
    ordering_fields = ('code', 'record_create_date', 'record_update_date', 'photo_url')
    search_fields = ('code', 'record_create_date', 'record_update_date', 'photo_url')

    def get_queryset(self):
        return StudentSearch.objects.filter(owner_id=self.request.user.id)


class StudentSearchRetrieveView(generics.RetrieveAPIView):
    serializer_class = StudentSearchSerializer
    lookup_field = 'code'

    def get_queryset(self):
        return StudentSearch.objects.filter(owner_id=self.request.user.id)


class StudentSearchCreateByURLView(generics.CreateAPIView):
    serializer_class = StudentSearchCreateByURLSerializer

    def perform_create(self, serializer):
        serializer.save(owner_id=self.request.user.id)


class StudentSearchCreateByPhotoView(generics.CreateAPIView):
    serializer_class = StudentSearchCreateByPhotoSerializer

    def perform_create(self, serializer):
        serializer.save(owner_id=self.request.user.id)
