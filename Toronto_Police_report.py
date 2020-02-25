import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(7,7))
plt.interactive(False)
#set default path
os.chdir(r"C:\Users\Louis\Documents\Python\Python_Project")
os.getcwd()
pd.set_option('display.max_columns',20)
#Processing and Transforming the data
firs2012=pd.read_csv("2012_FIRS.csv")
firs2012.info()

plt.title('Missing values')
sns.heatmap(firs2012.isnull())
plt.show()

firs2012.head()

#data clean
firs2012.AGE.value_counts(ascending=True)
print(firs2012[firs2012.AGE==2011])
firs2012[firs2012.AGE>120]=np.nan

#number of contact per day
contact_perday=firs2012['CONTACT_DATE'].value_counts()

plt.title('The distribution of contacts per day')
sns.distplot(contact_perday)
plt.show()

#Type of contact
contact = firs2012['NATURE_OF_CONTACT'].value_counts()
print(contact)
labels=contact.index

plt.title('Nature of Contact')
plt.pie(contact,labels=labels,autopct='%.0f%%',radius=1.0)
plt.show()


#Age distribution
def category_age(age):
    if  age<14:
        return '0-13 yrs'
    elif age<31 :
        return '14-30 yrs'
    elif age<48:
        return '31-47 yrs'
    elif age<65:
        return '48-64 yrs'
    else:
        return '65+'  
firs2012['AGE_CATEGORY']=firs2012['AGE'].apply(category_age)
agegrp=firs2012['AGE_CATEGORY'].value_counts()
print(agegrp)
labels=agegrp.index

explode=(0,0.1,0,0,0)
plt.title('Distribution by Age groups')
plt.pie(agegrp,labels=labels,autopct='%.0f%%',explode=explode,shadow=True,radius=1.0)
plt.show()

#Gender distribution
firs2012.SEX.describe()
gender=firs2012['SEX'].value_counts()
print(gender)
labels=gender.index

explode=(0.1,0,0,0)
plt.title('Gender distribution')
plt.pie(gender,labels=labels,autopct='%.0f%%',explode=explode,shadow=True,radius=1.0)
plt.show()


#Skin color distribution
skincolor=firs2012['SKIN_COLOUR'].value_counts()
labels=skincolor.index

explode=(0,0.1,0,0)
plt.title('Distribution by skin colour')
plt.pie(skincolor,labels=labels,autopct='%.0f%%',explode=explode,shadow=True,radius=1.0)
plt.show()

#Month distribution 
date=firs2012['CONTACT_DATE'].str.split(pat='.',expand=True)
month=date[1].value_counts()
month=month.sort_index()
month.index
month.values

plt.title('Contacts per month')
plt.bar(month.index,height=month.values)
plt.show()
#Time of the day
datetime=pd.to_datetime(firs2012['CONTACT_TIME'])
time=datetime.dt.hour
print(time)

def category_time(time):
    if  time<4:
        return 0
    elif time<8 :
        return 1
    elif time<12:
        return 2
    elif time<16:
        return 3
    elif time<20:
        return 4
    else:
        return 5 
# 0-'0-4 am' 1-'4-8 am' 2- '8am-12pm' 3-'12-4pm' 4-'4-8pm' 5-'8pm-0am'    
time=time.apply(category_time)
time=time.value_counts()
time=time.sort_index()
print(time)
timelst=time.values.tolist()

daytime=['0-4am','4-8am','8am-12pm','12-4pm','4-8pm','8pm-0am']

plt.title('Hour and number of Contacts')
plt.bar(daytime,height=timelst,color=['black','red','yellow','blue','cyan','green'])
plt.show()


#Relation between agegroup & skin color.. use heatmap
black_age=firs2012[firs2012['SKIN_COLOUR']=='Black']['AGE']
white_age=firs2012[firs2012['SKIN_COLOUR']=='White']['AGE']
brown_age=firs2012[firs2012['SKIN_COLOUR']=='Brown']['AGE']
other_age=firs2012[firs2012['SKIN_COLOUR']=='Other']['AGE']

labels=['White','Black','Brown','Other']
skin_age=[white_age.values.tolist(),black_age.values.tolist(),brown_age.values.tolist(),other_age.values.tolist()]

plt.title('Age distribution by skin color')
box=plt.boxplot(skin_age, patch_artist=True,labels=labels)
colors = ['cyan', 'lightblue', 'lightgreen', 'tan']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
plt.show()
#top 5 TPS patrol zone file reports
tps=firs2012['TPS_PATROL_ZONE'].value_counts()
print(tps)








