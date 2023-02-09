import requests
from stackapi import StackAPI
import json
import time



"""
TODO
-->make a function that start from startpage  (with pagesize  100) and go up till maxpagesize=100
and collect 10000 questions.

-->call that function until the property "hasmore"=false 

-->dump in a jsonfile
rquestions = SITE.fetch('questions', tagged='R',page=....)
"""


"""This function takes as parameter the page it should start and fetch the next 10k questions and returns them"""
def fetch_bath_questions(startpage):
    tempquestions = SITE.fetch('questions', tagged='R', page=startpage)
    return tempquestions['items']




"""This function takes as a parameter the starting page and increment it by"""
def get_next_pages(pages):
    pages += 100
    return pages


"""This function fetch all 480000 questions"""
def fetch_all_data(rquestions):
    startpage = 0
    for x in range(2):
        pages = get_next_pages(startpage)
        tempquestions = fetch_bath_questions(pages)
        rquestions.extend(tempquestions)
        """time.sleep(2)"""
    print(pages)

"""This function takes as a parameter a dict of questions and extract all the owners of them"""
def create_owners(questions):
    tempowners = []
    for x in range(len(questions)):
        tempowners.append(questions[x]["owner"])
    return tempowners



SITE = StackAPI('stackoverflow', key="z4*7kJUg2KkWHjeqU4N7zw((")
SITE.page_size = 2
SITE.max_pages = 1

questions = []

fetch_all_data(questions)


owners = create_owners(questions)
print(questions)
print(owners)

print(len(questions))
print(len(owners))





"""

with open("4questions.json", "w") as f:
    json.dump(questions, f)

print(len(questions['items']))
"""



