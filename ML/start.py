import pandas as pd

df = pd.read_csv('train.csv')

df.drop(['id', 'bdate'], axis=1, inplace=True)

def convert_mobile(has_mobile):
    return int(has_mobile)

df['has_mobile'] = df['has_mobile'].apply(convert_mobile)

def check_city(city):
    if pd.isnull(city):
        return 0
    return 1

df['has_city'] = df['city'].apply(check_city)
df.drop(['city'], axis=1, inplace=True)

def convert_ed_status(ed_status):
    if ed_status == 'None':
        return 0
    elif ed_status == 'Undergraduate applicant':
        return 1
    elif ed_status == "Student (Bachelor's)":
        return 2
    elif ed_status == "Alumnus (Bachelor's)":
        return 3
    elif ed_status == 'Student (Specialist)':
        return 4
    elif ed_status == 'Alumnus (Specialist)':
        return 5
    elif ed_status == "Student (Master's)":
        return 6
    elif ed_status == "Alumnus (Master's)":
        return 7
    elif ed_status == 'PhD':
        return 8
    elif ed_status == 'Candidate of Sciences':
        return 9

df['education_status'] = df['education_status'].apply(convert_ed_status)
df.drop(['langs', 'life_main', 'people_main', 'last_seen', 'occupation_name'], axis=1, inplace=True)

# 1 & 2 группа
def make_occupation(occupation_type):
    if occupation_type == 'work':
        return 1
    else:
        return 0

df['occupation_type'] = df['occupation_type'].apply(make_occupation)
# 1 & 2 группа

# 1 группа
def career_start(date):
    if date == 'False':
        return 2009
    else:
        return int(date)

df['career_start'] = df['career_start'].apply(career_start)

def get_experience(date_start):
    return 2022 - date_start

df['experience'] = df['career_start'].apply(get_experience)

df.drop(['career_start', 'career_end'], axis=1, inplace=True)
# 1 группа

# 2 группа
def get_education_form(ed_form):
    if ed_form == 'Distance Learning':
        return 1
    elif ed_form == 'Part-time':
        return 2
    else:
        return 0

df['education_form'] = df['education_form'].apply(get_education_form)
# 2 группа


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

x = df.drop('result', axis=1)
y = df['result']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)
print('Процент правильно предсказанных исходов:', round(accuracy_score(y_test, y_pred) * 100, 2) )
print('Confusion matrix:')
print(confusion_matrix(y_test, y_pred))
