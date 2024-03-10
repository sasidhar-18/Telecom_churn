import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn import metrics
from flask import Flask, request, render_template
import pickle

app = Flask("__name__")

df_1=pd.read_csv("C:\\Users\\SASIDHAR\\Desktop\\cust_churn\\archive\\first_telc.csv")

q = ""

@app.route("/")
def loadPage():
	return render_template('C:\\User\\SASIDHAR\\Desktop\\cust_churn\\home.html', query="")


@app.route("/", methods=['POST'])
def predict():
    
    '''
Gender                                  
Age                                     
Married                                 
Number of Dependents                    
Number of Referrals                     
Tenure in Months                        
Offer                                   
Phone Service                           
Avg Monthly Long Distance Charges     
Multiple Lines                          
Internet Service                        
Internet Type                           
Avg Monthly GB Download              
Online Security                         
Online Backup                           
Device Protection Plan                  
Premium Tech Support                    
Streaming TV                            
Streaming Movies                        
Streaming Music                         
Unlimited Data                          
Contract                                
Paperless Billing                       
Payment Method                          
Monthly Charge                          
Total Charges                           
Total Refunds                           
Total Extra Data Charges                
Total Long Distance Charges             
Total Revenue      
    '''
    

    
    inputQuery1 = request.form['query1']
    inputQuery2 = request.form['query2']
    inputQuery3 = request.form['query3']
    inputQuery4 = request.form['query4']
    inputQuery5 = request.form['query5']
    inputQuery6 = request.form['query6']
    inputQuery7 = request.form['query7']
    inputQuery8 = request.form['query8']
    inputQuery9 = request.form['query9']
    inputQuery10 = request.form['query10']
    inputQuery11 = request.form['query11']
    inputQuery12 = request.form['query12']
    inputQuery13 = request.form['query13']
    inputQuery14 = request.form['query14']
    inputQuery15 = request.form['query15']
    inputQuery16 = request.form['query16']
    inputQuery17 = request.form['query17']
    inputQuery18 = request.form['query18']
    inputQuery19 = request.form['query19']
    inputQuery20 = request.form['query20']
    inputQuery21 = request.form['query21']
    inputQuery22 = request.form['query22']
    inputQuery23 = request.form['query23']
    inputQuery24 = request.form['query24']
    inputQuery25 = request.form['query25']
    inputQuery26 = request.form['query26']
    inputQuery27 = request.form['query27']
    inputQuery28 = request.form['query28']
    inputQuery29 = request.form['query29']
    inputQuery30 = request.form['query30']

    model = pickle.load(open("C:\\Users\\SASIDHAR\\Desktop\\cust_churn\\churn.sav", "rb"))
    
    data = [[inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5, inputQuery6, inputQuery7, 
             inputQuery8, inputQuery9, inputQuery10, inputQuery11, inputQuery12, inputQuery13, inputQuery14,
             inputQuery15, inputQuery16, inputQuery17, inputQuery18, inputQuery19,inputQuery20,inputQuery21, inputQuery22, inputQuery23, inputQuery24,
             inputQuery25, inputQuery26, inputQuery27, inputQuery28, inputQuery29,inputQuery30]]
    
    new_df = pd.DataFrame(data, columns = ['Gender','Age','Married','Number of Dependents','Number of Referrals','Offer','Phone Service',                           
                                             'Avg Monthly Long Distance Charges' ,'Multiple Lines','Internet Service','Internet Type','Avg Monthly GB Download',              
                                           'Online Security','Online Backup','Device Protection Plan' ,'Premium Tech Support','Streaming TV','Streaming Movies',                        
                                           'Streaming Music','Unlimited Data','Contract','Paperless Billing','Payment Method','Monthly Charge','Total Charges' ,                         
                                           'Total Refunds','Total Extra Data Charges','Total Long Distance Charges','Total Revenue','Tenure'])
    
    df_2 = pd.concat([df_1, new_df], ignore_index = True) 
    # Group the tenure in bins of 12 months
    labels = ["{0} - {1}".format(i, i + 11) for i in range(1, 72, 12)]
    
    df_2['tenure_group'] = pd.cut(df_2.Tenure.astype(int), range(1, 80, 12), right=False, labels=labels)
    #drop column customerID and tenure
    df_2.drop(columns= ['Tenure'], axis=1, inplace=True)   
    
    
    
    
    new_df__dummies = pd.get_dummies(df_2[['Gender','Age','Married','Number of Dependents','Number of Referrals','Offer','Phone Service',                           
                                            'Avg Monthly Long Distance Charges' ,'Multiple Lines','Internet Service','Internet Type','Avg Monthly GB Download',              
                                           'Online Security','Online Backup','Device Protection Plan' ,'Premium Tech Support','Streaming TV','Streaming Movies',                        
                                           'Streaming Music','Unlimited Data','Contract','Paperless Billing','Payment Method','Monthly Charge','Total Charges' ,                         
                                           'Total Refunds','Total Extra Data Charges','Total Long Distance Charges','Total Revenue','tenure_group']])
    
    
    #final_df=pd.concat([new_df__dummies, new_dummy], axis=1)
        
    
    single = model.predict(new_df__dummies.tail(1))
    probablity = model.predict_proba(new_df__dummies.tail(1))[:,1]
    
    if single==1:
        o1 = "This customer is likely to be churned!!"
        o2 = "Confidence: {}".format(probablity*100)
    else:
        o1 = "This customer is likely to continue!!"
        o2 = "Confidence: {}".format(probablity*100)
        
    return render_template('home.html', output1=o1, output2=o2, 
                           query1 = request.form['query1'], 
                           query2 = request.form['query2'],
                           query3 = request.form['query3'],
                           query4 = request.form['query4'],
                           query5 = request.form['query5'], 
                           query6 = request.form['query6'], 
                           query7 = request.form['query7'], 
                           query8 = request.form['query8'], 
                           query9 = request.form['query9'], 
                           query10 = request.form['query10'], 
                           query11 = request.form['query11'], 
                           query12 = request.form['query12'], 
                           query13 = request.form['query13'], 
                           query14 = request.form['query14'], 
                           query15 = request.form['query15'], 
                           query16 = request.form['query16'], 
                           query17 = request.form['query17'],
                           query18 = request.form['query18'], 
                           query19 = request.form['query19'],
                           query20 = request.form['query20'], 
                           query21 = request.form['query21'], 
                           query22 = request.form['query22'], 
                           query23 = request.form['query23'], 
                           query24 = request.form['query24'], 
                           query25 = request.form['query25'], 
                           query26 = request.form['query26'], 
                           query27 = request.form['query27'],
                           query28 = request.form['query28'], 
                           query29 = request.form['query29'],
                           query30 = request.form['query30'])
    
app.run(debug=True)
