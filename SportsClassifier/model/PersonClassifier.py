#%%
from os import path
from cv2 import data
from numpy.core.numeric import True_
import pandas as pd 
from matplotlib import pyplot as plt
import numpy as np
import matplotlib
import cv2
# %%
img = cv2.imread("./test_images/sharapova1.jpg")
# %%
img.shape
# %%
plt.imshow(img)
# %%
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# %%
plt.imshow(gray)
# %%
gray
# %%
#cropping out face from the whole image
face_cascade = cv2.CascadeClassifier('./opencv/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier("./opencv/haarcascade_eye.xml")

faces = face_cascade.detectMultiScale(gray,1.3,5)
faces
# %%
(x,y,w,h) = faces[0]
# %%
face_img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
plt.imshow(face_img)
# %%
#drawing out eyes 
cv2.destroyAllWindows()
for (x,y,w,h) in faces:
    face_img - cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0),2)
    roi_gray = gray[y:y+h,x:x+w]
    roi_color = face_img[y:y+h,x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

plt.figure()
plt.imshow(face_img,cmap='gray')
plt.show()
# %%
#getting our region of interest(roi)
def get_cropped_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = img[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) >=2:
            return roi_color
        
# %%
cropped_img = get_cropped_image("./test_images/sharapova1.jpg")
plt.imshow(cropped_img)
# %%
path_to_data = './dataset/'
path_to_cr_data = './dataset/cropped/'
# %%
import os
img_dirs = []
for entry in os.scandir(path_to_data):
    if entry.is_dir():
        img_dirs.append(entry.path)
# %%
img_dirs
# %%
#deleting cropped floder if it already exists
import shutil
if os.path.exists(path_to_cr_data):
    shutil.rmtree(path_to_cr_data)
os.mkdir(path_to_cr_data)
# %%
cropped_image_dirs = []
celebrity_file_names_dict = {}
for img_dir in img_dirs:
    count = 1
    celebrity_name = img_dir.split('/')[-1]
    celebrity_file_names_dict[celebrity_name] = []
    for entry in os.scandir(img_dir):
        roi_color = get_cropped_image(entry.path)
        if roi_color is not None:
            cropped_folder = path_to_cr_data + celebrity_name
            if not os.path.exists(cropped_folder):
                os.makedirs(cropped_folder)
                cropped_image_dirs.append(cropped_folder)
                print("Generating cropped images in folder: ",cropped_folder)
            cropped_file_name = celebrity_name + str(count) + ".png"
            cropped_file_path = cropped_folder + "/" + cropped_file_name
            cv2.imwrite(cropped_file_path, roi_color)
            celebrity_file_names_dict[celebrity_name].append(cropped_file_path)
            count += 1
            
# %%
#wavlet transform for extracting features
import pywt
def w2d(img, mode = 'haar', level=1):
    imArray = img
    imArray = cv2.cvtColor(imArray,cv2.COLOR_BGR2GRAY)
    
    #converting image to float
    imArray = np.float32(imArray)
    imArray/=255;
    
    #computing coefficients
    coeff = pywt.wavedec2(imArray,mode,level=level)
    coeff_h = list(coeff)
    coeff_h[0] *= 0;
    
    #reconstruction
    imArray_h = pywt.waverec2(coeff_h,mode);
    imArray_h *= 255;
    imArray_h = np.uint8(imArray_h)
    
    return imArray_h
# %%
im_har = w2d(cropped_img,'db1',5)
plt.imshow(im_har,cmap='gray')
# %%
celebrity_file_names_dict = {}
for img_dir in cropped_image_dirs:
    celebrity_name = img_dir.split('/')[-1]
    file_list = []
    for entry in os.scandir(img_dir):
        file_list.append(entry.path)
    celebrity_file_names_dict[celebrity_name] = file_list
celebrity_file_names_dict
#%%
class_dict = {}
count = 0
for celebrity_name in celebrity_file_names_dict.keys():
    class_dict[celebrity_name] = count
    count = count + 1
class_dict
# %%
X, y = [], []
for celebrity_name, training_files in celebrity_file_names_dict.items():
    for training_image in training_files:
        img = cv2.imread(training_image)
        scalled_raw_img = cv2.resize(img, (32, 32))
        img_har = w2d(img,'db1',5)
        scalled_img_har = cv2.resize(img_har, (32, 32))
        combined_img = np.vstack((scalled_raw_img.reshape(32*32*3,1),scalled_img_har.reshape(32*32,1)))
        X.append(combined_img)
        y.append(class_dict[celebrity_name])   
# %%
len(X)
# %%
len(X[0])
# %%
32*32*3+32*32
# %%
X= np.array(X).reshape(len(X),4096).astype(float)
# %%
X.shape
# %%
X[0]
# %%
#data cleaning done
#training model
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
# %%
#creating a pipeline and scaling and training on SVM
X_train,X_test, y_train, y_test = train_test_split(X,y,random_state=0)

pipe = Pipeline([('scaler', StandardScaler()),('svc',SVC(kernel='rbf',C=10))])
pipe.fit(X_train,y_train)
pipe.score(X_test,y_test)
# %%
print(classification_report(y_test, pipe.predict(X_test)))
#%%
#Using GridSearchCV for hyhperparameter tuning
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
# %%
model_param = {
    'svm': {
        'model': svm.SVC(gamma='auto',probability=True),
        'params' : {
            'svc__C': [1,10,100,1000],
            'svc__kernel': ['rbf','linear']
        }  
    },
    'random_forest': {
        'model': RandomForestClassifier(),
        'params' : {
            'randomforestclassifier__n_estimators': [1,5,10]
        }
    },
    'logistic_regression' : {
        'model': LogisticRegression(solver='liblinear',multi_class='auto'),
        'params': {
            'logisticregression__C': [1,5,10]
        }
    }
}
# %%
scores = []
best_estimators = {}
import pandas as pd
for algo, mp in model_param.items():
    pipe = make_pipeline(StandardScaler(), mp['model'])
    clf =  GridSearchCV(pipe, mp['params'], cv=5, return_train_score=False)
    clf.fit(X_train, y_train)
    scores.append({
        'model': algo,
        'best_score': clf.best_score_,
        'best_params': clf.best_params_
    })
    best_estimators[algo] = clf.best_estimator_
    
df = pd.DataFrame(scores,columns=['model','best_score','best_params'])
df
# %%
best_estimators
# %%
best_estimators['svm'].score(X_test,y_test)
# %%
best_estimators['random_forest'].score(X_test,y_test)
# %%
best_estimators['logistic_regression'].score(X_test,y_test)
# %%
#choosing our best model
best_clf = best_estimators['svm']
# %%
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,best_clf.predict(X_test))
# %%
import seaborn as sns
sns.heatmap(cm,annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')
# %%
#saving our model
import joblib
joblib.dump(best_clf, 'SportsClassifier.pkl')
# %%
import json
with open('class_dictionary.json','w') as f:
    f.write(json.dumps(class_dict))
# %%
