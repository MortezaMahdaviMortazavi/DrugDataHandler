from bs4 import BeautifulSoup
import requests

# URL of the website
url = "https://zinc20.docking.org/substances/home/"

# Fetch the webpage content
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')

# Find the textarea element and modify its value
textarea = soup.find('textarea', {'id': 'paste', 'name': 'paste'})
inchi = "InChI=1S/C8H9Cl2NO3S/c1-8(2-9)4(7(13)14)11-5(12)3(10)6(11)15-8/h3-4,6H,2H2,1H3,(H,13,14)/t3-,4-,6+,8-/m0/s1"
textarea.string = inchi

# Find the search button
search_button = soup.find('button', {'class': 'btn btn-default pull-right'})

# Extract the form action URL and other form data
form = search_button.find_parent('form')
form_action = form['action']
other_form_data = {
    # Add any other form data here if needed
}
print(form_action)
# Simulate submitting the form
submit_response = requests.post(form_action, data=other_form_data)

# Print the response or do further processing
print(submit_response.content)
