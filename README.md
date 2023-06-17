# Heart-risk
• The model implements SVM to classify wether the individual is facing a high risk of heart failure.	
The features:
1.	Age (in years): When one enters his/her name, age and other personal details in the app while starting, the app can make a count of the user’s age.
2.	Sex (male:1 female:0)
3.	CP: Chest Pain, this feature is omitted while creating the model since it is taken once the patient is admitted/ is under treatment.
4.	Chol: Serum cholesterol, omitted while making the model since it is taken from a physical blood test.
5.	Fbs: Fasting blood sugar, omitted due to the similar reason as Chol.
6.	RestECG: Resting electrocardiogram results, Value 0 refers to normal , Value 1 refers to having ST-T wave abnormality and value 2 refers to a condition known as left ventricular hypertrophy. The values 1 and 2 can be assessed in the app from the ECG pattern.
7.	Thalach: Refers to the maximum heart rate achieved by the user. Note that this value will be under the exercise header.
8.	Exang: exercise induced angina, omitted since it is measured at the time of hospital diagnosis.
9.	Oldpeak: ST depression induced by exercise relative to rest (value determined by subtracting the lowest ST segment points during exercise and rest)
10.	Slope: the slope of the peak ST segment of the ECG during exercise, ST-T abnormalities are considered to be a crucial indicator for identifying presence of ischaemia, Value 0 refers to upsloping, Value 1 is flat and value 2 is down sloping.
11.	Ca: value is omitted. It refers to fluoroscopy of blood vessels which cannot be done using sensors.
12.	Thal: value is omitted. It refers to a specification of the heart disease.
13.	Target: value 1 refers to the person having a heart disease and value 0 refers to the fact that the person doesn’t have a heart disease.


•	Parameters like Oldpeak, Exang, Slope and RestECG are to be measured in the app from the ECG data that the app receives from the device. 
•	From the analog output of the ecg sensor from the Arduino, the values are sent to the app in the form of a matrix (the analog output and the corresponding time at which the output was received). 
•	To detect the Q point/Q wave, one can traverse through the analog array/column by measuring the approximate slop(a2-a1)/(t2-t1). At the start of the Q point, the slope increases drastically and we can use a threshold to get that point. To detect R, we can traverse the column values after the q value such that the particular analog value exceeds its successor and predecessor.
•	After R, the analog value decreases steeply until we arrive at the point S whose successor and predecessor exceeds it.
•	After S, we proceed on similar lines to get the next maxima which is T.
•	The slope right after S gives the Slope parameter. To get RestECG, an approximate measure is to find the difference between the Q point and S point. By comparing the values of S at exercise and rest, one can get Oldpeak.
•	The above procedure is a rudimentary procedure. For improved precision, one may refer to an available MATLAB algorithm.
•	By leaving out the omitted features, built a simple ML model based on SVM algorithm and implemented it using Sci-kit Learn

•	Using 80% of the available data as training data and the rest as testing data, the model classifies the given data set with an accuracy of around 0.7 and recall score of about 0.7
