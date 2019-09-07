## San-Francisco-Crime-Classification
Participating in Kaggle competition

- This dataset contains incidents derived from SFPD Crime Incident Reporting system. 
- The data ranges from 1/1/2003 to 5/13/2015. The training set and test set rotate every week, meaning week 1,3,5,7... belong to test set, week 2,4,6,8 belong to training set. 

- The dataset is so big having 87K collumns for training data;
- We can deal with GPS data including address, latitude and longitude.

**Data fields**
1. Dates - timestamp of the crime incident
2. Category - category of the crime incident (only in train.csv). This is the target variable you are going to predict.
3. Descript - detailed description of the crime incident (only in train.csv)
4. DayOfWeek - the day of the week
5. PdDistrict - name of the Police Department District
6. Resolution - how the crime incident was resolved (only in train.csv)
7. Address - the approximate street address of the crime incident 
8. X - Longitude
9. Y - Latitude



-------
Connect address :

%%html
<script src="https://livebook.dsschool.co.kr/alex/loader.js"></script>
