Parametrize Test 'credentials', utils.load_json('accounts.json')
Test Name With Accounts login
Set Credentials credentials["username"], credentials["password"]
Open Page "http://127.0.0.1:8000/login"
Login Wait Page Load submit="css=.w3-button"
Take Screenshot filename="login.png"
Open Page Wait Page Load "http://127.0.0.1:8000/logout"