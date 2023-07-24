import pandas as pd




data=pd.read_csv("C:/Users/M/Downloads/DOHMH_New_York_City_Restaurant_Inspection_Results.csv")
data.head()


# Checking for missing data
data.isnull().any()
data.loc[data.DBA.isnull(), 'DBA']='Unnamed'
# replacing null data
data.loc[data.BUILDING.isnull(), 'BUILDING']='Unavailable'
data.loc[data.STREET.isnull(), 'STREET']='Unavailable'
data.loc[data.STREET.str.match("@ WEST 43 STREET"), 'STREET']='WEST 43 STREET'
data.loc[data.STREET.str.match("@ GRAND CENTRAL"), 'STREET']='GRAND CENTRAL'
data.loc[data.STREET.str.match("& GRAND CENTRAL"), 'STREET']='GRAND CENTRAL'
data.ZIPCODE.astype(str)
data.loc[data.ZIPCODE.isnull(), 'ZIPCODE']='Unavailable'
data.PHONE.astype(str)
data.loc[data.PHONE.isnull(), 'PHONE']='Unavailable'
data.loc[data.CUISINE_DESCRIPTION.isnull(), 'CUISINE_DESCRIPTION']='Other'
data.loc[data.ACTION.isnull(), 'ACTION']='Not yet inspected'
data.loc[data.VIOLATION_CODE.isnull(), 'VIOLATION_CODE']='-'
data.loc[data.VIOLATION_DESCRIPTION.isnull(), 'VIOLATION_DESCRIPTION']='-'
data.loc[data.SCORE.isnull(), 'SCORE']=-1
data.loc[(data.GRADE.isnull()) & (data.SCORE<=13) & (data.SCORE>=0), 'GRADE']='A'
data.loc[(data.GRADE.isnull()) & (data.SCORE<=27) & (data.SCORE>=14), 'GRADE']='B'
data.loc[(data.GRADE.isnull()) & (data.SCORE>=28), 'GRADE']='C'
data.loc[(data.GRADE.isnull()) & (data.SCORE==-1), 'GRADE']='N'
#data.loc[data.grade_date.isnull()]

data.GRADE_DATE=pd.to_datetime(data.GRADE_DATE)
data.loc[data.GRADE_DATE.isnull(), 'GRADE_DATE']=pd.Timestamp('2000-01-01')

data.loc[data.INSPECTION_TYPE.isnull(), 'INSPECTION_TYPE']='Unavailable'

data.loc[data.Latitude.isnull(), 'LATITUDE']=0
data.loc[data.Longitude.isnull(), 'LONGITUDE']=0


data.isnull().any()


data[data.duplicated(keep='first')].shape

data=data[~data.duplicated(keep='first')]

data.to_csv('C:/Users/M/Downloads/DOHMH_New_York_City_Restaurant_Inspection_Results.csv')