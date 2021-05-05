# Vaccine spotter for India

Original Author: https://github.com/akshaynathr/Vaccine-Spotter-India

Modified Features:
1) Checks for age18+ Added
2) Pincode added in response
3) 2 API request every minute for today and tommorow
4) Formatted email subject so can appear as new email every time
5) Added district id for Maharashtra

Vaccine spotter is a simple tool for tracking the availability of Covid vaccines in any state in India
It uses the api from COWIN site to monitor for vaccine availability and sent an immediate email to user.
 ✨

## Features

- Run in the terminal and monitor the vaccine availability
- Sent email to email address set by user immediately when there is vaccines available

 

## Installation

Vaccine-spotter requires python3 to run

Set email details, district_id in the script 

``` sh 
# For gmail, the lesssecureapps connection needs to be turned on for email to work :  https://myaccount.google.com/lesssecureapps
# need to change the smpt address for other mail providers

email_user = 'test@gmail.com'
email_password = '<password>'

sent_from = email_user
to = ['<to_email@gmail.com>']

# time gap
minutes = 1

__district = "district_id"
'''
{
  "districts": [
    {
      "district_id": 391,
      "district_name": "Ahmednagar"
    },
    {
      "district_id": 364,
      "district_name": "Akola"
    },
    {
      "district_id": 366,
      "district_name": "Amravati"
    },
    {
      "district_id": 397,
      "district_name": "Aurangabad "
    },
    {
      "district_id": 384,
      "district_name": "Beed"
    },
    {
      "district_id": 370,
      "district_name": "Bhandara"
    },
    {
      "district_id": 367,
      "district_name": "Buldhana"
    },
    {
      "district_id": 380,
      "district_name": "Chandrapur"
    },
    {
      "district_id": 388,
      "district_name": "Dhule"
    },
    {
      "district_id": 379,
      "district_name": "Gadchiroli"
    },
    {
      "district_id": 378,
      "district_name": "Gondia"
    },
    {
      "district_id": 386,
      "district_name": "Hingoli"
    },
    {
      "district_id": 390,
      "district_name": "Jalgaon"
    },
    {
      "district_id": 396,
      "district_name": "Jalna"
    },
    {
      "district_id": 371,
      "district_name": "Kolhapur"
    },
    {
      "district_id": 383,
      "district_name": "Latur"
    },
    {
      "district_id": 395,
      "district_name": "Mumbai"
    },
    {
      "district_id": 365,
      "district_name": "Nagpur"
    },
    {
      "district_id": 382,
      "district_name": "Nanded"
    },
    {
      "district_id": 387,
      "district_name": "Nandurbar"
    },
    {
      "district_id": 389,
      "district_name": "Nashik"
    },
    {
      "district_id": 381,
      "district_name": "Osmanabad"
    },
    {
      "district_id": 394,
      "district_name": "Palghar"
    },
    {
      "district_id": 385,
      "district_name": "Parbhani"
    },
    {
      "district_id": 363,
      "district_name": "Pune"
    },
    {
      "district_id": 393,
      "district_name": "Raigad"
    },
    {
      "district_id": 372,
      "district_name": "Ratnagiri"
    },
    {
      "district_id": 373,
      "district_name": "Sangli"
    },
    {
      "district_id": 376,
      "district_name": "Satara"
    },
    {
      "district_id": 374,
      "district_name": "Sindhudurg"
    },
    {
      "district_id": 375,
      "district_name": "Solapur"
    },
    {
      "district_id": 392,
      "district_name": "Thane"
    },
    {
      "district_id": 377,
      "district_name": "Wardha"
    },
    {
      "district_id": 369,
      "district_name": "Washim"
    },
    {
      "district_id": 368,
      "district_name": "Yavatmal"
    }
  ],
  "ttl": 24
}
'''
``` 

Run the script after setting the values 
```sh
python vaccine_spotter.py

```
No data is collected from users . The script is open to verify
 
## Development

Want to contribute? Great!


