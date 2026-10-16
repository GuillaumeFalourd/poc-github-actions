import os
import urllib2
import json

repoResultsPerPage=100
repoPageNumber=1
gitHubOrganization='${{ inputs.organization }}'
token='${{ inputs.token }}'
allRepos = []
allRepoNames = []
allRepoNamesList = ''
output_file = os.getenv('GITHUB_OUTPUT')

# URL to send the request to
url = '/api/v3/orgs/%s/repos?page=%s&per_page=%s' % (gitHubOrganization, repoPageNumber, repoResultsPerPage)

# Custom headers to include in the request
headers = {'content-type': 'application/json', 'Authorization': 'token %s' % (token)}

# Create a Request object with the URL and headers
req = urllib2.Request(url, headers=headers)

# Send the request and store the response in a variable
response = urllib2.urlopen(req)

# Read the response data
result = response.read()
while result != '[]':
  print('PageNumber: %s' % (repoPageNumber))
  # Parse json
  json_data = json.loads(result)
  allRepos = allRepos + json_data
  repoPageNumber = repoPageNumber + 1
  url = 'api/v3/orgs/%s/repos?page=%s&per_page=%s' % (gitHubOrganization, repoPageNumber, repoResultsPerPage)
  req = urllib2.Request(url, headers=headers)
  response = urllib2.urlopen(req)
  result = response.read()
for repo in allRepos:
  allRepoNames.append(repo['name'])
  allRepoNamesList = ','.join(allRepoNames)
  print("List:", allRepoNamesList)
  with open(output_file, "a") as myfile:
    myfile.write(f"TEST={allRepoNamesList}")