import random,string,httpx,time

def solve(clientkey:str,service:str) -> dict:
    if 'capsolver' in service:
        resp = httpx.post('https://api.capsolver.com/createTask',json={
    "clientKey": clientkey,
    "task": {
        "type": "HCaptchaTaskProxyLess",
        "websiteURL": "https://discord.com",
        "websiteKey": "4c672d35-0701-42b2-88c3-78380b0db560",
        "pageAction": "signup",
        }
    }).json()

        taskId = resp.get('taskId')
        if not taskId:
            return {
            "solved" : False,
            "excp" : f"{resp.get('errorCode')} : {resp.get('errorDescription')}"
        }
        for j in range(30):

            getTask = httpx.post('https://api.capsolver.com/getTaskResult',json={
    "clientKey": clientkey,
    "taskId": taskId
}).json()

            getTaskStatus = getTask.get('status')
            if getTaskStatus == 'ready':
            
                return {
                "solved" : True,
                "gcap" : getTask.get('solution').get("gRecaptchaResponse")
            }
            time.sleep(2)
        else:
            return {
            "solved" : False,
            "excp" : "Captcha Timeout!"
        }
    elif 'capmonster' in service:
        resp = httpx.post('https://api.capmonster.cloud/createTask',json={
    "clientKey":clientkey,
    "task":
    {
        "type":"HCaptchaTaskProxyless",
        "websiteURL":"https://discord.com",
        "websiteKey":"4c672d35-0701-42b2-88c3-78380b0db560",
        "pageAction": "signup"
    }
}).json()
        taskId = resp.get('taskId')
        if not taskId:
            return {
            "solved" : False,
            "excp" : resp.get('errorCode')
        }
        for j in range(30):
            getTask = httpx.post('https://api.capmonster.cloud/getTaskResult',json={
    "clientKey":clientkey,
    "taskId": taskId
}).json()
            if getTask.get('errorCode'):
                return {
                    "solved" : False,
                    "excp" : resp.get('errorCode')
                }
                
            getTaskStatus = getTask.get('status')
            if getTaskStatus == 'ready':
                return {
                "solved" : True,
                "gcap" : getTask.get('solution').get("gRecaptchaResponse")
            }
            time.sleep(2)
        else:
            return {
            "solved" : False,
            "excp" : "Captcha Timeout!"
        }
