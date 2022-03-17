import requests
import os
username = input("Enter the github username:")
repo_count = input("Enter your repositary count:")
request = requests.get('https://api.github.com/users/'+username+'/repos?per_page='+str(repo_count))
json = request.json()
for i in range(0,len(json)):
  print("[*] Project Number:",i+1)
  print("[*] Project Name:",json[i]['name'])
  print("[*] Project URL:",json[i]['svn_url'])
  try:
    command = "git clone "+str(json[i]['svn_url'])+".git"
    os.system(command)
    print("[+] [STATUS]("+str(json[i]['name'])+") Cloned")
  except:
    print("[-] [STATUS]("+str(json[i]['name'])+") Cloning Failed")
  print("\n")
