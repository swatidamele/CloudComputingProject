def detect_faces_uri(uri):
    """Detects faces in the file located in Google Cloud Storage or the web."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    image = vision.Image()
    image.source.image_uri = uri
    # respose = client.annotate_image({'image': {'source': {'image_uri': uri}}, 'features': [{'maxResults':20, 'type': vision.Feature.Type.FACE_DETECTION}],})

    response = client.face_detection(image=image,max_results=50)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Faces:')
    count = 0
    for face in faces:
        count+=1
        print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in face.bounding_poly.vertices])

        print('face bounds: {}'.format(','.join(vertices)))
        print('Num faces: {}\n'.format(str(count)))
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))



detect_faces_uri("https://media.istockphoto.com/photos/group-of-happy-multiethnic-people-standing-on-a-white-background-picture-id484348057?k=20&m=484348057&s=612x612&w=0&h=kZzsxqlT7WYlgRioD_eqNqQr3L5_DB-OkLbV94WJsHk=")
