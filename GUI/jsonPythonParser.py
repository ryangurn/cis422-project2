import json

data = json.load(open("SPOILER_data.json"))

#print(data["CIS 407 - [Sem Career/Internships]"]["name"])

#print(data["CIS 407 - [Sem Career/Internships]"]["sections"][0]["instructor"])

class_keys_full = []

# Populates all keys into a python list
for i in range(len(data)):
	class_keys_full.append([key for key in data.keys()][i])


def get_keys():
	return class_keys_full

def get_credits(class_key):
	return data[class_key]["credits"]

def get_grading(class_key):
	return data[class_key]["grading"]

def get_name(class_key):
	return data[class_key]["name"]

def get_subject(class_key):
	return data[class_key]["subject"]

def get_number_of_sections(class_key):
	return len(data[class_key]["sections"])

def get_sec_url(class_key, sections_num):
	return data[class_key]["sections"][sections_num]["instructor"]

def get_sec_days(class_key, sections_num):
	return data[class_key]["sections"][sections_num]["day"]	

def get_sec_times(class_key, sections_num):
	return data[class_key]["sections"][sections_num]["time"]	

def get_sec_max_seats(class_key, sections_num):
	return data[class_key]["sections"][sections_num]["max"]

def get_sec_instructor(class_key, sections_num):
	return data[class_key]["sections"][sections_num]["instructor"]	

def get_sec_location(class_key, sections_num):
	return data[class_key]["sections"][sections_num]["location"]	

def get_sec_notes(class_key, sections_num):
	return data[class_key]["sections"][sections_num]["notes"]

def get_sec_type(class_key, sections_num):
	return data[class_key]["sections"][sections_num]["type"]

def get_sec_available_seats(class_key, sections_num):
	return data[class_key]["sections"][sections_num]["avail"]

def get_sec_taken_seats(class_key, sections_num):
	return data[class_key]["sections"][sections_num]["taken"]

def get_sec_crn(class_key, sections_num):
	return data[class_key]["sections"][sections_num]["crn"]

def get_course_number(class_key):
	return data[class_key]["number"]