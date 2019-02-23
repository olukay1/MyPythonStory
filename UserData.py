Rcd = {'UserName' : input("Enter your User name: "), 'pwd' : input("Enter your password: "), 'ID': '20'}

if Rcd['UserName' ] in ('kay', 'Kay', 'KAY'):
    print ('You have already registered')
else:
    print ('No record found, Try and register')
