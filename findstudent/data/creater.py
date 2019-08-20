from datetime import datetime
import pytz

from .models import Continent, Country, Timezone, City, StudentGroup, Student, Institute, StudentPhoto, DetectedFace, \
    Sex, EmotionType, Emotion, LandmarkType, Landmark, StudentSearch, IdentifiedFace, UniversalIdentifiedFace
from .amazon import Amazon
from .vk import VK


def transliteration_to_latin(text):
    cyrillic = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    latin = 'a|b|v|g|d|e|e|zh|z|i|i|k|l|m|n|o|p|r|s|t|u|f|kh|tc|ch|sh|shch||y||e|iu|ia|A|B|V|G|D|E|E|Zh|Z|' \
            'I|I|K|L|M|N|O|P|R|S|T|U|F|Kh|Tc|Ch|Sh|Shch||Y||E|Iu|Ia'.split('|')
    return text.translate({ord(k): v for k, v in zip(cyrillic, latin)})


def get_city_by_item(i):
    try:
        return City.objects.get(name_ru=i['city']['title'])
    except (City.DoesNotExist, KeyError):
        return None


def get_home_town_by_item(i):
    try:
        return City.objects.get(name_ru=i['home_town'])
    except (City.DoesNotExist, KeyError):
        return None


def get_user_info_by_item(i):
    is_deactivated = False
    try:
        is_closed = bool(i['is_closed'])
        has_photo = bool(i['has_photo'])
        nickname = i['screen_name']
        status = i['status']
    except KeyError:
        is_closed = True
        has_photo = False
        nickname = None
        status = None
        is_deactivated = True
    return nickname, is_deactivated, is_closed, has_photo, status


def get_birthday_by_item(i):
    try:
        return datetime.strptime(i['bdate'], '%d.%m.%Y')
    except ValueError:
        return datetime.strptime(i['bdate'], '%d.%m')
    except KeyError:
        return None


def create_student_group(name, group_id, institute_id):
    avatar_url = VK().get_groups_info([group_id], ["photo_200"])[0]['photo_200']
    institute = Institute.objects.get(pk=institute_id)
    student_group, created = StudentGroup.objects.update_or_create(group_id=group_id,
                                                                   defaults={'name_en': transliteration_to_latin(name),
                                                                             'name_ru': name,
                                                                             'institute': institute,
                                                                             'avatar_url': avatar_url})
    answer = VK().get_group_members(group_id=group_id, fields=['sex', 'bdate', 'screen_name', 'city', 'home_town',
                                                               'photo_max', 'photo_max_orig', 'education', 'status',
                                                               'has_photo'])
    for i in answer:
        first_name = transliteration_to_latin(i['first_name'])
        first_name_ru = i['first_name']
        last_name = transliteration_to_latin(i['last_name'])
        last_name_ru = i['last_name']
        sex_id = int(i['sex'])
        city = get_city_by_item(i)
        home_town = get_home_town_by_item(i)
        nickname, is_deactivated, is_closed, has_photo, status = get_user_info_by_item(i)
        birthday = get_birthday_by_item(i)
        institute = Institute.objects.get(id=institute_id)
        university = institute.university
        avatar_url = i['photo_max']
        avatar_original_url = i['photo_max_orig']

        defaults = {
            'first_name': first_name,
            'first_name_ru': first_name_ru,
            'last_name': last_name,
            'last_name_ru': last_name_ru,
            'sex_id': sex_id,
            'nickname': nickname,
            'is_closed': is_closed,
            'has_photo': has_photo,
            'is_deactivated': is_deactivated,
            'status': status,
            'birthday': birthday,
            'city': city,
            'home_town': home_town,
            'student_group': student_group,
            'avatar_url': avatar_url,
            'avatar_original_url': avatar_original_url,
            'university': university
        }

        try:
            Student.objects.update_or_create(user_id=i['id'], defaults=defaults)
        except OSError:
            defaults['avatar_url'] = None
            defaults['avatar_original_url'] = None
            defaults['has_photo'] = False
            Student.objects.update_or_create(user_id=i['id'], defaults=defaults)


def create_student_photos_by_user_id(user_id):
    student = Student.objects.get(user_id=user_id)
    answer = VK().get_user_photos(owner_id=user_id)
    for picture in answer:
        photo_url = picture['sizes'].pop()['url']
        create_date = datetime.utcfromtimestamp(picture['date']).replace(tzinfo=pytz.utc)
        try:
            StudentPhoto.objects.update_or_create(
                owner=student,
                photo_url=photo_url,
                defaults={
                    'photo_create_date': create_date
                }
            )
        except OSError:
            continue


def create_student_photos_by_group(group_id):
    students = Student.objects.filter(student_group__group_id=group_id)
    for student in students:
        if student.has_photo and not student.is_closed and not student.is_deactivated:
            create_student_photos_by_user_id(student.user_id)


def create_face_details(face):
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

    for emotion in face["Emotions"]:
        my_emotion = Emotion.objects.create(emotion_type=EmotionType.objects.get(system_name=emotion["Type"]),
                                            emotion_confidence=emotion["Confidence"])
        details.emotions.add(my_emotion)

    for landmark in face["Landmarks"]:
        my_landmark = Landmark.objects.create(landmark_type=LandmarkType.objects.get(system_name=landmark["Type"]),
                                              x_coordinate=landmark["X"],
                                              y_coordinate=landmark["Y"])
        details.landmarks.add(my_landmark)

    details.save()

    return details, created


def create_face_detail_search(face):
    try:
        photo = StudentPhoto.objects.get(id=face["Face"]["ExternalImageId"])
        owner = photo.owner
    except Student.DoesNotExist:
        return False, False
    details, created = IdentifiedFace.objects.get_or_create(
        bounding_box_width=face["Face"]["BoundingBox"]["Width"],
        bounding_box_height=face["Face"]["BoundingBox"]["Height"],
        bounding_box_left=face["Face"]["BoundingBox"]["Left"],
        bounding_box_top=face["Face"]["BoundingBox"]["Top"],
        confidence=face["Face"]["Confidence"],
        similarity=face["Similarity"],
        face_id=face["Face"]["FaceId"],
        image_id=face["Face"]["ImageId"],
        student=owner,
    )

    return details, created


def detect_and_index_photo(picture):
    picture_name = picture.photo.name
    detected_faces = Amazon().detect_by_image(picture_name=picture_name)['FaceDetails']
    for face in detected_faces:
        details, created = create_face_details(face=face)

        picture.detected_faces.add(details)
        details.save()
    Amazon().index_faces(picture_name=picture.photo.name,
                         external_image_id=str(picture_name))


def old_index_student_photo(photo_id):
    picture = StudentPhoto.objects.get(pk=photo_id)
    if picture.detected_faces.count() is 1:
        return

    detected_faces = Amazon().detect_by_image(picture_name=picture.photo.name)['FaceDetails']
    user_id = picture.owner.user_id

    for face in detected_faces:
        details, created = create_face_details(face=face)

        picture.detected_faces.add(details)

        if picture.detected_faces.count() is 1:
            new_details = Amazon().index_faces(picture_name=picture.photo.name,
                                               external_image_id=str(user_id))
            # I don't know, why Amazon detect one face, but Amazon index don't return params
            if len(new_details) is 1:
                details.face_id = new_details[0]["Face"]["FaceId"]
                details.image_id = new_details[0]["Face"]["ImageId"]
                details.save()


def index_student_photos_by_user_id(user_id):
    pictures = StudentPhoto.objects.filter(owner__user_id=user_id)
    for picture in pictures:
        print(picture.pk)
        old_index_student_photo(photo_id=picture.pk)


def index_student_photos_by_group(group_id):
    students = Student.objects.filter(student_group__group_id=group_id)
    for student in students:
        if student.has_photo and not student.is_closed and not student.is_deactivated:
            index_student_photos_by_user_id(student.user_id)


def student_search(photo_id):
    photo = StudentSearch.objects.get(id=photo_id)

    result_detect = Amazon().detect_by_image(picture_name=photo.photo.name)["FaceDetails"]
    if len(result_detect) is 0:
        return 1
    for face in result_detect:
        details, created = create_face_details(face=face)
        photo.detected_faces.add(details)

    result_search = Amazon().search_faces_by_image(picture_name=photo.photo.name, max_faces=200,
                                                   face_match_threshold=70)
    for face in result_search:
        details, created = create_face_detail_search(face=face)
        if details is not False:
            photo.identified_faces.add(details)
    return 0


def get_search_details(search_code):
    search = StudentSearch.objects.get(code=search_code).identified_faces.all()
    my_list = []
    for i in search:
        print(i.student.user_id, i.similarity)
        my_list.append((i.student.user_id, i))

    reg_dict = {}
    for acct_num, value in my_list:
        if acct_num in reg_dict:
            reg_dict[acct_num].append(value)
        else:
            reg_dict[acct_num] = [value]

    for student_id in reg_dict:
        student = Student.objects.get(user_id=student_id)
        universal = UniversalIdentifiedFace.objects.create(student=student)
        for detail in reg_dict[student_id]:
            universal.identified_faces.add(detail)
            universal.save()
        StudentSearch.objects.get(code=search_code).universal_identified_face.add(universal)
