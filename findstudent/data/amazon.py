from findstudent.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_REGION_NAME
import boto3


class Amazon:
    access_key = AWS_ACCESS_KEY_ID
    secret_key = AWS_SECRET_ACCESS_KEY
    bucket_name = AWS_STORAGE_BUCKET_NAME
    region_name = AWS_REGION_NAME
    service = 'rekognition'
    collection_id ='findstudentrelease'
    client = boto3.client(service, aws_access_key_id=access_key,
                          aws_secret_access_key=secret_key, region_name=region_name)

    def detect_by_image(self, picture_name):
        response = self.client.detect_faces(
            Image={
                'S3Object': {
                    'Bucket': self.bucket_name,
                    'Name': picture_name,
                }
            },
            Attributes=['ALL'])
        return response

    def get_faces_details(self, picture_name):
        return self.detect_by_image(picture_name=picture_name)['DetectedFace']

    def get_faces_count(self, picture_name):
        return len(self.detect_by_image(picture_name=picture_name)['DetectedFace'])

    def list_faces(self, max_results=100):
        response = self.client.list_faces(
            CollectionId=self.collection_id,
            MaxResults=max_results
        )
        return response['Faces']

    def index_faces(self, picture_name, external_image_id, max_faces=100):
        response = self.client.index_faces(
            CollectionId=self.collection_id,
            Image={
                'S3Object': {
                    'Bucket': self.bucket_name,
                    'Name': picture_name,
                }
            },
            ExternalImageId=external_image_id,
            DetectionAttributes=['ALL'],
            MaxFaces=max_faces,
        )
        return response["FaceRecords"]

    def search_faces_by_image(self, picture_name, max_faces=100, face_match_threshold=70):
        response = self.client.search_faces_by_image(
            CollectionId=self.collection_id,
            Image={
                'S3Object': {
                    'Bucket': self.bucket_name,
                    'Name': picture_name,
                }
            },
            MaxFaces=max_faces,
            FaceMatchThreshold=face_match_threshold
        )
        return response['FaceMatches']
