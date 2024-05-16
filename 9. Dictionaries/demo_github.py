# Write a program to fetch all the pull request login id & counts from kubernetes github repo
import requests
# /repos/{owner}/{repo}/pulls
url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"
response = requests.get(url)

if response.status_code == 200:
    # convert response in Json
    pull_requests = response.json()
    # create a empty dictinary to store login id details
    pr_creaters = {}
    
    for pull in pull_requests:
        creater = pull['user']['login']
        
        if creater in pr_creaters:
            pr_creaters[creater] = +1
        else:
            pr_creaters[creater] = 1
        
        # Display the dictionary of pr_creaters and their couts
        print("PR creaters and their counts")
        for creater, count in pr_creaters.items():
            print(f'{creater} : {count}')

else:
    print(f'Failed to fetch PR(s) status code: {response.status_code}')  

