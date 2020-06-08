from os import listdir
import os
import face_recognition
from email_notification import send_email
import pandas as pd
import glob

def detect_face_names(unknown_image_encoding):
    list_val = []
    person_name = 'not available'
    filenames = listdir('./actual_faces/')
    if '.DS_Store' in filenames:
        filenames.remove('.DS_Store')
    print(filenames)
    for f in filenames:

        actual_image = face_recognition.load_image_file(os.path.join('./actual_faces/',f))
        actual_image_encoding = face_recognition.face_encodings(actual_image)[0]
        result = face_recognition.face_distance([actual_image_encoding],unknown_image_encoding)
        print(result)
        if result<0.45:
            person_name = f
            break
    return person_name.split('.')[0]

def get_names():
    person_name = 'not available'
    employee_name = 'not available'
    email_id = ''
    list_personname = []
    if not os.path.exists('./cropped_images'):
        os.makedirs('./cropped_images')
    filenames = listdir('./cropped_images/')
    print(filenames)
    if '.DS_Store' in filenames:
        filenames.remove('.DS_Store')
    for f in filenames:
        unknown_image = face_recognition.load_image_file(os.path.join('./cropped_images/',f))
        unknown_image_encoding = face_recognition.face_encodings(unknown_image)
        if len(unknown_image_encoding)>0:
            person_name = detect_face_names(unknown_image_encoding[0])
            if person_name not in list_personname and person_name != 'not available':
                list_personname.append(person_name)
    print(person_name)
    df = pd.read_excel('employee_database.xlsx')
    if len(list_personname)!=0:
        for i in range(df.shape[0]):
            if list_personname[0] == df['EMP_ID'][i]:
                email_id = df['Emp_emaiil_id'][i]
                employee_name = df['Emp_name'][i]
        if email_id!='':
            send_email(email_id)
    print("The name of the person is ",employee_name)
    files = glob.glob('./cropped_images/*')
    for f in files:
        os.remove(f)
    return employee_name
