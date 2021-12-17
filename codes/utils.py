import requests 


def sendSMS(body , reciver):
    res = requests.post(url='https://RestfulSms.com/api/Token',  data={
	"UserApiKey":"9b39cbd08d0834c88a2dcf59",
	"SecretKey":"etehadi2000mahdi"
    }).json()

    token = res['TokenKey']

    verify_code = requests.post(url='https://RestfulSms.com/api/VerificationCode', headers={'x-sms-ir-secure-token':token},data={
    "Code": body,
    "MobileNumber": reciver
    }).json()

    #res = requests.get(f'https://www.payam-resan.com/APISend.aspx?Username=etehadie&Password=97471631&From=50002060372089&To={reciver}&Text={body}').status_code
    
    print(res)
    print(verify_code)