from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from .amazon import Amazon


class Continent(models.Model):
    """!
        Continents of the Earth

        This model stores the data of the continents of the Earth.
        @param name name of continent
        @param alpha2 2-character ISO code
        @param image image of the continent on the map
    """
    name = models.CharField(max_length=32, unique=True, verbose_name=_('Name'))
    alpha2 = models.CharField(max_length=2, unique=True, verbose_name=_('Alpha2'))
    image = ProcessedImageField(upload_to='data/continent/',
                                format='PNG',
                                options={'quality': 60},
                                null=True,
                                verbose_name=_('Image'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Continents')
        verbose_name_plural = _('Continents')
        ordering = ["name"]


class Country(models.Model):
    """!
        Countries of the Earth

        This model stores the data of the countries of the Earth.
        @param name simple name of country
        @param official_name official name of country
        @param alpha2 2-character ISO code
        @param alpha3 3-character ISO code
        @param isocode digital ISO code
        @param area area of country
        @param population population of country
        @param independent dependent or independent country
        @param rating findstudent rating of country
        @param flag flag of country
    """

    name = models.CharField(max_length=64, unique=True, verbose_name=_('Name'))
    official_name = models.CharField(max_length=64, unique=True, verbose_name=_('Official name'))
    alpha2 = models.CharField(max_length=2, unique=True, verbose_name=_('Alpha2'))
    alpha3 = models.CharField(max_length=3, unique=True, verbose_name=_('Alpha3'))
    iso_code = models.IntegerField(unique=True, verbose_name=_('ISO code'))
    independent = models.BooleanField(default=True, verbose_name=_('Independent'))
    rating = models.IntegerField(default=0, verbose_name=_('Rating'))

    area = models.IntegerField(null=True, blank=True, verbose_name=_('Area'))
    population = models.IntegerField(null=True, blank=True, verbose_name=_('Population'))
    flag = ProcessedImageField(processors=[ResizeToFill(68, 45)],
                               upload_to='data/country/',
                               format='PNG',
                               options={'quality': 60},
                               null=True,
                               verbose_name=_('Flag'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
        ordering = ["-rating", "name"]


class Timezone(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name=_('Name'))
    abbr_short = models.CharField(max_length=64, unique=True, verbose_name=_('Short abbreviation'))
    abbr_long = models.CharField(max_length=64, unique=True, verbose_name=_('Long abbreviation'))
    raw_offset = models.IntegerField(default=0, verbose_name=_('GMT offset'))
    dst_offset = models.IntegerField(default=0, verbose_name=_('DST offset'))
    rating = models.IntegerField(default=0, verbose_name=_('Rating'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Timezone')
        verbose_name_plural = _('Timezones')
        ordering = ["-rating", "name"]


class City(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name=_('Name'))
    iata_code = models.CharField(max_length=3, unique=True, verbose_name=_('IATA code'))
    latitude = models.FloatField(verbose_name=_('Latitude'))
    longitude = models.FloatField(verbose_name=_('Longitude'))
    altitude = models.IntegerField(verbose_name=_('Altitude'))
    capital = models.BooleanField(default=False, verbose_name=_('Capital'))
    rating = models.IntegerField(default=0, verbose_name=_('Rating'))

    area = models.IntegerField(null=True, blank=True, verbose_name=_('Area'))
    population = models.IntegerField(null=True, blank=True, verbose_name=_('Population'))
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE,
                                  verbose_name=_('Continent'))
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name=_('Country'))
    timezone = models.ForeignKey(Timezone, on_delete=models.CASCADE,
                                 verbose_name=_('Timezone'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')
        ordering = ["-rating", "name"]
        unique_together = ("latitude", "longitude")


class University(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name=_('Name'))
    abbr = models.CharField(max_length=16, unique=True, verbose_name=_('Abbreviation'))
    latitude = models.FloatField(verbose_name=_('Latitude'))
    longitude = models.FloatField(verbose_name=_('Longitude'))
    student_count = models.IntegerField(verbose_name=_('Student count'))
    rating = models.IntegerField(default=0, verbose_name=_('Rating'))

    slogan = models.CharField(max_length=128, null=True, blank=True, verbose_name=_('Slogan'))
    founded = models.DateField(null=True, blank=True, verbose_name=_('Founded'))
    website = models.URLField(null=True, blank=True, verbose_name=_('Website'))
    logo = ProcessedImageField(upload_to='data/university/',
                               format='PNG',
                               options={'quality': 60},
                               null=True,
                               verbose_name=_('Logo'))
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name=_('City'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('University')
        verbose_name_plural = _('Universities')
        ordering = ["-rating", "name"]
        unique_together = ("latitude", "longitude")


class Room(models.Model):
    campus = models.CharField(max_length=1, verbose_name=_('Campus'))
    number = models.CharField(max_length=64, verbose_name=_('Number'))
    rating = models.IntegerField(default=0, verbose_name=_('Rating'))
    university = models.ForeignKey(University, on_delete=models.CASCADE, verbose_name=_('University'))
    location = ProcessedImageField(upload_to='data/room/',
                                   format='PNG',
                                   options={'quality': 60},
                                   null=True,
                                   blank=True,
                                   verbose_name=_('Location'))

    def __str__(self):
        s = "{} {}".format(self.campus, self.number)
        return s

    class Meta:
        verbose_name = _('Room')
        verbose_name_plural = _('Rooms')
        ordering = ["campus", "number"]


class Institute(models.Model):
    name = models.CharField(max_length=64, verbose_name=_('Name'))
    abbr = models.CharField(max_length=64, verbose_name=_('Abbreviation'))
    rating = models.IntegerField(default=0, verbose_name=_('Rating'))
    website = models.URLField(null=True, blank=True, verbose_name=_('Website'))
    logo = ProcessedImageField(upload_to='data/institute/',
                               format='PNG',
                               options={'quality': 60},
                               null=True,
                               verbose_name=_('Logo'))
    university = models.ForeignKey(University, on_delete=models.CASCADE, verbose_name=_('University'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Institute')
        verbose_name_plural = _('Institutes')
        ordering = ["-rating", "name"]


class Department(models.Model):
    name = models.CharField(max_length=128, verbose_name=_('Name'))
    abbr = models.CharField(max_length=64, verbose_name=_('Abbreviation'))
    rating = models.IntegerField(default=0, verbose_name=_('Rating'))
    website = models.URLField(null=True, blank=True, verbose_name=_('Website'))
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, verbose_name=_('Institute'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')
        ordering = ["-rating", "name"]


class Lecturer(models.Model):
    last_name = models.CharField(max_length=64, verbose_name=_('Last name'))
    first_name = models.CharField(max_length=64, verbose_name=_('First name'))
    patronymic = models.CharField(max_length=64, null=True, blank=True, verbose_name=_('Patronymic'))
    photo = ProcessedImageField(upload_to='data/lecturer/',
                                format='PNG',
                                null=True,
                                blank=True,
                                verbose_name=_('Photo'))
    rating = models.IntegerField(default=0, verbose_name=_('Rating'))
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name=_('Department'))

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = _('Lecturer')
        verbose_name_plural = _('Lecturers')
        ordering = ["-rating", "last_name"]


class Period(models.Model):
    number = models.IntegerField(verbose_name=_('Number'))
    start_time = models.TimeField(verbose_name=_('Start time'))
    end_time = models.TimeField(verbose_name=_('End time'))
    university = models.ForeignKey(University, on_delete=models.CASCADE, verbose_name=_('University'))

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = _('Period')
        verbose_name_plural = _('Periods')
        ordering = ["number"]


class StudentGroup(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name=_('Name'))
    group_id = models.IntegerField(unique=True, verbose_name=_('VK group id'))
    rating = models.IntegerField(default=0, verbose_name=_('Rating'))
    avatar = ProcessedImageField(upload_to='data/student_group/',
                                 format='PNG',
                                 null=True,
                                 blank=True,
                                 verbose_name=_('Avatar'))
    avatar_url = models.URLField(null=True, blank=True, verbose_name=_('Avatar URL'))
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, verbose_name=_('Institute'))
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True,
                                   verbose_name=_('Department'))

    def save(self, *args, **kwargs):
        from django.core.files.temp import NamedTemporaryFile
        import shutil
        import requests
        import uuid

        if self.avatar_url is not None:
            response = requests.get(self.avatar_url, stream=True)
            img_temp = NamedTemporaryFile()
            shutil.copyfileobj(response.raw, img_temp)
            random_name = uuid.uuid4().hex + ".png"
            self.avatar.save(random_name, img_temp, save=False)
        # now image data are in img_temp, how to pass that to ProcessedImageField?

        super(StudentGroup, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('StudentGroup')
        verbose_name_plural = _('StudentGroup')
        ordering = ["-rating", "name"]


class Sex(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name=_('Name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Sex')
        verbose_name_plural = _('Sexs')


class EmotionType(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name=_('Name'))
    system_name = models.CharField(max_length=64, unique=True, verbose_name=_('System name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Emotion type')
        verbose_name_plural = _('Emotion types')


class LandmarkType(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name=_('Name'))
    system_name = models.CharField(max_length=64, unique=True, verbose_name=_('System name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Landmark type')
        verbose_name_plural = _('Landmark types')


class Emotion(models.Model):
    emotion_type = models.ForeignKey(EmotionType, on_delete=models.CASCADE, verbose_name=_('Emotion type'))
    emotion_confidence = models.FloatField(verbose_name=_('Emotion confidence'))

    def __str__(self):
        return self.emotion_type.name

    class Meta:
        verbose_name = _('Emotion')
        verbose_name_plural = _('Emotions')
        ordering = ["-emotion_confidence"]


class Landmark(models.Model):
    landmark_type = models.ForeignKey(LandmarkType, on_delete=models.CASCADE, verbose_name=_('Landmark type'))
    x_coordinate = models.FloatField(verbose_name=_('X coordinate'))
    y_coordinate = models.FloatField(verbose_name=_('Y coordinate'))

    def __str__(self):
        return self.landmark_type.name

    class Meta:
        verbose_name = _('Landmark')
        verbose_name_plural = _('Landmarks')


class DetectedFace(models.Model):
    bounding_box_width = models.FloatField(verbose_name=_('Bounding box width'))
    bounding_box_height = models.FloatField(verbose_name=_('Bounding box height'))
    bounding_box_left = models.FloatField(verbose_name=_('Bounding box left'))
    bounding_box_top = models.FloatField(verbose_name=_('Bounding box top'))
    age_range_low = models.IntegerField(verbose_name=_('Age range low'))
    age_range_high = models.IntegerField(verbose_name=_('Age range high'))
    smile_value = models.BooleanField(verbose_name=_('Smile value'))
    smile_confidence = models.FloatField(verbose_name=_('Smile confidence'))
    eyeglasses_value = models.BooleanField(verbose_name=_('Eyeglasses value'))
    eyeglasses_confidence = models.FloatField(verbose_name=_('Eyeglasses confidence'))
    sunglasses_value = models.BooleanField(verbose_name=_('Sunglasses value'))
    sunglasses_confidence = models.FloatField(verbose_name=_('Sunglasses confidence'))
    gender_value = models.ForeignKey(Sex, on_delete=models.CASCADE, verbose_name=_('Gender value'))
    gender_confidence = models.FloatField(verbose_name=_('Gender confidence'))
    beard_value = models.BooleanField(verbose_name=_('Beard value'))
    beard_confidence = models.FloatField(verbose_name=_('Beard confidence'))
    mustache_value = models.BooleanField(verbose_name=_('Mustache value'))
    mustache_confidence = models.FloatField(verbose_name=_('Mustache confidence'))
    open_eyes_value = models.BooleanField(verbose_name=_('Eyes open value'))
    open_eyes_confidence = models.FloatField(verbose_name=_('Eyes open confidence'))
    open_mouth_value = models.BooleanField(verbose_name=_('Mouth open value'))
    open_mouth_confidence = models.FloatField(verbose_name=_('Mouth open confidence'))
    emotions = models.ManyToManyField(Emotion, verbose_name=_('Emotions'))
    landmarks = models.ManyToManyField(Landmark, verbose_name=_('Landmarks'))
    roll_pose = models.FloatField(verbose_name=_('Roll pose'))
    yam_pose = models.FloatField(verbose_name=_('Yaw pose'))
    pitch_pose = models.FloatField(verbose_name=_('Pitch pose'))
    brightness_quality = models.FloatField(verbose_name=_('Brightness quality'))
    sharpness_quality = models.FloatField(verbose_name=_('Sharpness quality'))
    confidence = models.FloatField(verbose_name=_('Confidence'))
    face_id = models.CharField(max_length=64, null=True, blank=True, verbose_name=_('Face ID'))
    image_id = models.CharField(max_length=64, null=True, blank=True, verbose_name=_('Image ID'))

    def __str__(self):
        return "{}x{}".format(self.bounding_box_width, self.bounding_box_height)

    class Meta:
        verbose_name = _('Detected Face')
        verbose_name_plural = _('Detected Faces')
        ordering = ["id"]


class Student(models.Model):
    last_name = models.CharField(max_length=64, verbose_name=_('Last name'))
    first_name = models.CharField(max_length=64, verbose_name=_('First name'))
    user_id = models.IntegerField(unique=True, verbose_name=_('User ID'))
    nickname = models.CharField(max_length=64, verbose_name=_('Nickname'), null=True, blank=True)
    birthday = models.DateField(null=True, blank=True, verbose_name=_('Birthday'))
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE, verbose_name=_('Sex'))
    rating = models.IntegerField(default=0, verbose_name=_('Rating'))

    real_last_name = models.CharField(max_length=64, null=True, blank=True, verbose_name=_('Real last name'))
    real_first_name = models.CharField(max_length=64, null=True, blank=True, verbose_name=_('Real first name'))
    patronymic = models.CharField(max_length=64, null=True, blank=True, verbose_name=_('Patronymic'))
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True, related_name="city",
                             verbose_name=_('City'))
    home_town = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True, related_name="home_town",
                                  verbose_name=_('Home town'))
    status = models.CharField(max_length=128, null=True, blank=True, verbose_name=_('Status'))
    has_photo = models.BooleanField(default=False, verbose_name=_('Has photo'))
    is_closed = models.BooleanField(default=False, verbose_name=_('Is closed'))
    is_deactivated = models.BooleanField(default=False, verbose_name=_('Is deactivated'))
    record_create_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Record create date'))
    record_update_date = models.DateTimeField(auto_now=True, verbose_name=_('Record update date'))
    avatar = ProcessedImageField(upload_to='data/student/avatar/',
                                 format='PNG',
                                 null=True,
                                 blank=True,
                                 verbose_name=_('Avatar'))
    avatar_original = ProcessedImageField(upload_to='data/student/avatar_original/',
                                          format='PNG',
                                          null=True,
                                          blank=True,
                                          verbose_name=_('Original avatar'))
    avatar_url = models.URLField(null=True, blank=True, verbose_name=_('Avatar URL'))
    avatar_original_url = models.URLField(null=True, blank=True, verbose_name=_('Original avatar URL'))
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True, blank=True,
                                   verbose_name=_('University'))
    student_group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, null=True, blank=True,
                                      verbose_name=_('Student Group'))

    def save(self, *args, **kwargs):
        from django.core.files.temp import NamedTemporaryFile
        import shutil
        import requests
        import uuid

        if self.avatar_url is not None:
            response = requests.get(self.avatar_url, stream=True)
            img_temp = NamedTemporaryFile()
            shutil.copyfileobj(response.raw, img_temp)
            random_name = uuid.uuid4().hex + ".png"
            self.avatar.save(random_name, img_temp, save=False)

        if self.avatar_original_url is not None:
            response = requests.get(self.avatar_original_url, stream=True)
            img_temp = NamedTemporaryFile()
            shutil.copyfileobj(response.raw, img_temp)
            random_name = uuid.uuid4().hex + ".png"
            self.avatar_original.save(random_name, img_temp, save=False)

        # now image data are in img_temp, how to pass that to ProcessedImageField?

        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return "{} {}".format(self.last_name, self.first_name)

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')
        ordering = ["-rating", "last_name"]


class StudentPhoto(models.Model):
    owner = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name=_('Student'))
    photo_create_date = models.DateTimeField(verbose_name=_('Photo create date'))
    record_create_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Record create date'))
    record_update_date = models.DateTimeField(auto_now=True, verbose_name=_('Record update date'))
    detected_faces = models.ManyToManyField(DetectedFace, verbose_name=_('Faces details'))
    photo = ProcessedImageField(upload_to='data/student_photos/',
                                format='PNG',
                                verbose_name=_('Photo'))
    photo_url = models.URLField(unique=True, verbose_name=_('Photo URL'))

    def save(self, *args, **kwargs):
        from django.core.files.temp import NamedTemporaryFile
        import shutil
        import requests
        import uuid

        if self.photo_url is not None:
            response = requests.get(self.photo_url, stream=True)
            img_temp = NamedTemporaryFile()
            shutil.copyfileobj(response.raw, img_temp)
            random_code = uuid.uuid4().hex
            random_name = random_code + ".png"
            self.photo.save(random_name, img_temp, save=False)

        super(StudentPhoto, self).save(*args, **kwargs)
        picture_name = self.photo.name
        detected_faces = Amazon().detect_by_image(picture_name=picture_name)['FaceDetails']
        for face in detected_faces:
            details, created = DetectedFace.objects.get_or_create(
                bounding_box_width=face["BoundingBox"]["Width"],
                bounding_box_height=face["BoundingBox"]["Height"],
                bounding_box_left=face["BoundingBox"]["Left"],
                bounding_box_top=face["BoundingBox"]["Top"],
                age_range_high=face["AgeRange"]["High"],
                age_range_low=face["AgeRange"]["Low"],
                smile_value=face["Smile"]["Value"],
                smile_confidence=face["Smile"]["Confidence"],
                eyeglasses_value=face["Eyeglasses"]["Value"],
                eyeglasses_confidence=face["Eyeglasses"]["Confidence"],
                sunglasses_value=face["Sunglasses"]["Value"],
                sunglasses_confidence=face["Sunglasses"]["Confidence"],
                gender_value=Sex.objects.get(name_en=face["Gender"]["Value"]),
                gender_confidence=face["Gender"]["Confidence"],
                beard_value=face["Beard"]["Value"],
                beard_confidence=face["Beard"]["Confidence"],
                mustache_value=face["Mustache"]["Value"],
                mustache_confidence=face["Mustache"]["Confidence"],
                open_eyes_value=face["EyesOpen"]["Value"],
                open_eyes_confidence=face["EyesOpen"]["Confidence"],
                open_mouth_value=face["MouthOpen"]["Value"],
                open_mouth_confidence=face["MouthOpen"]["Confidence"],
                roll_pose=face["Pose"]["Roll"],
                yam_pose=face["Pose"]["Yaw"],
                pitch_pose=face["Pose"]["Pitch"],
                brightness_quality=face["Quality"]["Brightness"],
                sharpness_quality=face["Quality"]["Sharpness"],
                confidence=face["Confidence"]
            )

            self.detected_faces.add(details)
            details.save()
        Amazon().index_faces(picture_name=self.photo.name,
                             external_image_id=str(self.id))

    def __str__(self):
        return "{} {}".format(self.owner.last_name, self.owner.first_name)

    class Meta:
        verbose_name = _('Student Photo')
        verbose_name_plural = _('Student Photos')
        ordering = ["-photo_create_date"]


class IdentifiedFace(models.Model):
    bounding_box_width = models.FloatField(verbose_name=_('Bounding box width'))
    bounding_box_height = models.FloatField(verbose_name=_('Bounding box height'))
    bounding_box_left = models.FloatField(verbose_name=_('Bounding box left'))
    bounding_box_top = models.FloatField(verbose_name=_('Bounding box top'))
    confidence = models.FloatField(verbose_name=_('Confidence'))
    similarity = models.FloatField(verbose_name=_('Similarity'))
    face_id = models.CharField(max_length=64, verbose_name=_('Face ID'))
    image_id = models.CharField(max_length=64, verbose_name=_('Image ID'))
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name=_('Student'))

    def __str__(self):
        return self.face_id

    class Meta:
        verbose_name = _('Identified Face')
        verbose_name_plural = _('Identified Faces')
        ordering = ["-similarity"]


class UniversalIdentifiedFace(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name=_('Student'))
    identified_faces = models.ManyToManyField(IdentifiedFace, verbose_name=_('Identified faces'))

    def __str__(self):
        return str(self.student.user_id)

    class Meta:
        verbose_name = _('Universal Identified Face')
        verbose_name_plural = _('Universal Identified Faces')


class StudentSearch(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('Owner'))
    code = models.CharField(max_length=64, unique=True, verbose_name=_('Code'))
    record_create_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Record create date'))
    record_update_date = models.DateTimeField(auto_now=True, verbose_name=_('Record update date'))
    detected_faces = models.ManyToManyField(DetectedFace, verbose_name=_('Detected faces'))
    identified_faces = models.ManyToManyField(IdentifiedFace, verbose_name=_('Identified faces'))
    universal_identified_face = models.ManyToManyField(UniversalIdentifiedFace,
                                                       verbose_name=_('Universal identified faces'))
    photo = ProcessedImageField(upload_to='data/student_search/',
                                format='PNG',
                                verbose_name=_('Photo'))
    photo_url = models.URLField(null=True, blank=True, verbose_name=_('Photo URL'))

    def __str__(self):
        return "{}".format(self.owner)

    class Meta:
        verbose_name = _('Student Search')
        verbose_name_plural = _('Student Searches')
        ordering = ["-owner", '-record_create_date']

    def save(self, *args, **kwargs):
        from django.core.files.temp import NamedTemporaryFile
        import shutil
        import requests
        import uuid

        if self.photo_url is not None:
            self.code = uuid.uuid4().hex
            response = requests.get(self.photo_url, stream=True)
            img_temp = NamedTemporaryFile()
            shutil.copyfileobj(response.raw, img_temp)
            random_name = uuid.uuid4().hex + ".png"
            self.photo.save(random_name, img_temp, save=False)
        else:
            self.code = uuid.uuid4().hex
            random_name = uuid.uuid4().hex + ".png"
            self.photo.save(random_name, self.photo, save=False)
        super(StudentSearch, self).save(*args, **kwargs)
