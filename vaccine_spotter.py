import requests
from datetime import date,timedelta,datetime
import os
import smtplib
from time import time,ctime,sleep

email_user = 'youremailid@gmail.com'
email_password = 'yourpassword'

sent_from = email_user
to = ['whotosend0@gmail.com'] # supports multiple comma seperated ['xyz@gmail.com','abc@gmail.com']

minutes = 1

today = date.today()


__district = "363" #kannur




d1 = today.strftime("%d/%m/%Y") #For Todays slot
d2 = today + timedelta(1) # For 2mrw slot

__date = str(d1).replace("/","-")
__date2 = str(d2).replace("/","-")

def send_email(res):
	# turn on allow less secure apps to get email
	#  https://myaccount.google.com/lesssecureapps
	# suggest to use a backup account for this to preserve security
	
	subject = "Pune: Slot Trigger on "+ctime(time())+"\n\n" + res
	body = "Version 1(18+): For Todays & Tommorow. Author: Pratik Kelwalkar"

	email_text = """\
From: %s
To: %s 
Subject: %s
%s
""" % (sent_from, ", ".join(to), subject, body)
	print (email_text)

	try:
	    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	    server.ehlo()
	    server.login(email_user, email_password)
	    server.sendmail(sent_from, to, email_text)
	    server.close()

	    print ('Email sent!')
	except Exception as e:
	    print ('Something went wrong...')
	    print (e)
	


def parse_json(result):
	output = []
	centers = result['centers']
	for center in centers:
		sessions = center['sessions']
		for session in sessions:
			if session['available_capacity'] > 0 and session['min_age_limit'] <= 18:
				res = { 'name': center['name'], 'block_name':center['block_name'],'age_limit':session['min_age_limit'], 'vaccine_type':session['vaccine'] , 'date':session['date'],'available_capacity':session['available_capacity'], 'pincode': center['pincode']}
				output.append(res)
	return output


def call2mrw_api():
    print(ctime(time()))
    api = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=" + __district+ "&date="+ __date2
    
    response = requests.get(api)

    if response.status_code == 200:
        print ("API call success tommorow")
        result = response.json()
        output = parse_json(result)
        if len(output) > 0:
            print ("Vaccines available Tommorow")
            print('\007')
            result_str = ""
            for center in output:

                '''print center['name']
                print "block:"+center['block_name']
                print "vaccine count:"+str(center['available_capacity'])
                print "vaccines type:" + center['vaccine_type']
                print center['date']
                print "age_limit:"+ str(center['age_limit'])
                print "---------------------------------------------------------" '''
                result_str = result_str + str(center['pincode']) + "\n"
                result_str = result_str + center['name'] + "\n"
                result_str = result_str + "block:"+center['block_name'] + "\n"
                result_str = result_str + "available tommorow:"+str(center['available_capacity']) + "\n"
                result_str = result_str + "vaccine type:"+ center['vaccine_type'] + "\n"
                result_str = result_str + center['date'] + "\n"
                result_str = result_str + "age_limit:"+str(center['age_limit'])+"\n"
                result_str = result_str + "---------------\n"
            send_email(result_str)

        else:
            
            print ("Vaccines not available for tommorow\n")

				
	
def call_api():
    print(ctime(time()))
    api = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=" + __district+ "&date="+ __date
    apitmrw = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=" + __district+ "&date="+ __date2
    
    response = requests.get(api)

    if response.status_code == 200:
        print ("API call success today")
        result = response.json()
        output = parse_json(result)
        if len(output) > 0:
            print ("Vaccines available today")
            print('\007')
            result_str = ""
            for center in output:

                '''print center['name']
                print "block:"+center['block_name']
                print "vaccine count:"+str(center['available_capacity'])
                print "vaccines type:" + center['vaccine_type']
                print center['date']
                print "age_limit:"+ str(center['age_limit'])
                print "---------------------------------------------------------" '''
                result_str = result_str + str(center['pincode']) + "\n"
                result_str = result_str + center['name'] + "\n"
                result_str = result_str + "block:"+center['block_name'] + "\n"
                result_str = result_str + "available now:"+str(center['available_capacity']) + "\n"
                result_str = result_str + "vaccine type:"+ center['vaccine_type'] + "\n"
                result_str = result_str + center['date'] + "\n"
                result_str = result_str + "age_limit:"+str(center['age_limit'])+"\n"
                result_str = result_str + "---------------\n"
            send_email(result_str)

        else:
            
            print ("Vaccines not available for today\n")

t = datetime.now()

if __name__ == '__main__':
    call_api()
    call2mrw_api()
    while True:
        delta = datetime.now()-t
        if delta.seconds >= minutes * 60:
            call_api()
            call2mrw_api()
            t = datetime.now()
#   	#sleep(minutes * 60)
        
