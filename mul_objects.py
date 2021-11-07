
def localize_objects(path):
    """Localize objects in the local image.
    Args:
    path: The path to the local file.
    """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    # objects = client.object_localization(
    #     image=image).localized_object_annotations
    objects = client.object_localization(
        image=image, max_results=100).localized_object_annotations
    count=0
    print('Number of objects found: {}'.format(len(objects)))
    for object_ in objects:
        if(object_.name == 'Person'):
            count+=1
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        print('Normalized bounding polygon vertices: ')
        for vertex in object_.bounding_poly.normalized_vertices:
            print(' - ({}, {})'.format(vertex.x, vertex.y))
    print("numPerson",count)


def localize_objects_uri(uri):
    """Localize objects in the image on Google Cloud Storage
    Args:
    uri: The path to the file in Google Cloud Storage (gs://...)
    """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    image = vision.Image()
    image.source.image_uri = uri

    objects = client.object_localization(
        image=image, max_results=100).localized_object_annotations
    count=0
    print('Number of objects found: {}'.format(len(objects)))
    for object_ in objects:
        if(object_.name == 'Person'):
            count+=1
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        print('Normalized bounding polygon vertices: ')
        for vertex in object_.bounding_poly.normalized_vertices:
            print(' - ({}, {})'.format(vertex.x, vertex.y))
    print("numPerson",count)


# localize_objects_uri("https://storage.googleapis.com/kaggle-media/competitions/google-research/1.png")
# localize_objects_uri("https://lh3.googleusercontent.com/proxy/fCkpS0e5dvNARBMtn-9nB-hX8hEsEl79VdTA87cb7oMlfPKQAUhiGRz1Ap_GVeyc7k6KE8DzL64NE8yXPmW3r7GtsFhCQkm0boePFwEmfcR7AqCyKlsTVfG5r8nm3s3o4p38")
# localize_objects_uri("https://media.istockphoto.com/photos/group-of-happy-multiethnic-people-standing-on-a-white-background-picture-id484348057?k=20&m=484348057&s=612x612&w=0&h=kZzsxqlT7WYlgRioD_eqNqQr3L5_DB-OkLbV94WJsHk=")
localize_objects("/home/aoj7250/MicrosoftTeams-image (1).png")