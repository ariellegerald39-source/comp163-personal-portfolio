# COMP 163: Assignment 3 - Personal Data
# Portfolio & Git Collaboration
# Arielle Gerald
# Date: September 18, 2025
# Description: Stores and displays academic, personal, and financial
# information using Chapter 3 Python data types and operations.


# Personal Information Storage
full_name = "Arielle Gerald"
student_email = "amgerald@aggies.ncat.edu"
hometown = "Raleigh, NC"
graduation_semester = "Spring 2029"
major = "Computer Engineering"

# Academic Data Organization
current_courses_list = ["COMP 163", "MATH 131", "ECEN 101", "SPCH 250", "HIST 103"]
completed_courses_list = ["English I", "Microeconomics", "College Transfer Success", "Art Appreciation"]
gpa_history_list = [3.2, 3.6, 3.4, 3.7]
credit_hours_list = [3, 3, 3, 3]  # Each current course is 3 credits

# Contact Information Storage
emergency_contact_tuple = ("Mom", "Dad", "704-555-0199")
home_address_tuple = ("3632 Marble Ridge Ln", "Raleigh, NC", "27610")
instagram_info_tuple = ("Instagram", "@its.ari3ll3", 144)
twitter_info_tuple = ("Twitter", "@its.ari3ll3", 127)
birthday_tuple = ("Birthday", 2, 16, 2007)

# Interests Tracking
current_skills_set = {"Team Collaboration", "Problem Solving", "Time management", "Safety Protocols", "Effective Communication"}
skills_to_learn_set = {"JavaScript", "Data structures", "Git", "Web design", "Cyber Security"}
career_interests_set = {"Computer engineering", "Cybersecurity", "Data science", "Robotics"}
hobbies_set = {"Shopping", "Traveling", "Listening to music"}
entertainment_backlog_set = {"One Piece", "Barry", "Life", "Incantation", "Memento"}

# Organizational Mapping
course_credits_dictionary = {"COMP 163": 3, "MATH 131": 3, "ECEN 101": 3, "SPCH 250": 3, "HIST 103": 3}
course_professors_dictionary = {"COMP 163": "Prof. Rhodes", "MATH 131": "Dr. Johnson", "ECEN 101": "Dr. Horne", "HIST 103": "Dr. Wadelington", "SPCH 250": "Dr. Crossen"}
course_rooms_dictionary = {"COMP 163": "McNair 130", "MATH 131": "Marteena 233", "ECEN 101": "McNair Auditorium", "HIST 103": "Gibbs 109", "SPCH 250": "Online Course"}
monthly_budget_dictionary = {"Food": 200, "Entertainment": 50, "Going out": 70 , "Personal care": 100}
study_hours_per_subject_dictionary = {"Programming": 3, "Math": 4, "Engineering": 4, "History": 1}
contact_directory_dictionary = {"Mom": "704-555-0199", "Dad": "336-555-7821", "Academic Advisor": "336-334-5000"}


# Required Calculations


# Total current credits from credit hours list
total_current_credits = sum(course_credits_dictionary.values())  # Mathematical operation

# Cumulative GPA from GPA history list
cumulative_gpa = round(sum(gpa_history_list) / len(gpa_history_list), 2)  # Mathematical operation

# Total weekly study hours from study hours dictionary
total_weekly_study_hours = sum(study_hours_per_subject_dictionary.values())  # Mathematical operation

# Academic investment (monthly food budget divided by total study hours per month)
academic_investment = round(monthly_budget_dictionary["Food"] / (total_weekly_study_hours * 3.6), 1)  # 4 weeks in a month

# Daily food budget (food amount ÷ 30, rounded to 2 decimals)
daily_food_budget = round(monthly_budget_dictionary["Food"] / 30, 2)  # Mathematical operation

# Annual budget projection (monthly total × 12)
annual_projection = monthly_budget_total = sum(monthly_budget_dictionary.values()) * 12  # Mathematical operation

# Total social media followers from platform tuples
total_followers = instagram_info_tuple[2] + twitter_info_tuple[2]  # Tuple indexing

# Contact directory size analysis
key_contacts_count = len(contact_directory_dictionary)  # Dictionary key access

# Total courses completed (length of completed courses list)
total_courses_completed = len(completed_courses_list)  # List indexing

# Academic workload assessment
current_academic_load = total_current_credits + total_weekly_study_hours  # Mathematical operation

# Entertainment backlog management count
entertainment_backlog_count = len(entertainment_backlog_set)  # Set creation

# Current hobbies count (length of set)
current_hobbies_count = len(hobbies_set)  # Set creation

# ================================================================
# Professional Output Formatting
# ================================================================

print("="*64)
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("="*64)
print(f"Student: {full_name} | Email: {student_email}")
print(f"From: {hometown} | Graduating: {graduation_semester}")
print(f"Major: {major}\n")

print("=== ACADEMIC PROFILE ===")
print(f"Current Semester: {total_current_credits} credits across {len(current_courses_list)} courses")
print(f"Cumulative GPA: {cumulative_gpa:.2f}")
print(f"Weekly Study Time: {total_weekly_study_hours} hours")
print(f"Academic Investment: ${academic_investment} per study hour\n")

print("Current Courses:")
print(f"{current_courses_list[0]} - {course_credits_dictionary[current_courses_list[0]]} credits - {course_professors_dictionary[current_courses_list[0]]} - {course_rooms_dictionary[current_courses_list[0]]}")
print(f"{current_courses_list[1]} - {course_credits_dictionary[current_courses_list[1]]} credits - {course_professors_dictionary[current_courses_list[1]]} - {course_rooms_dictionary[current_courses_list[1]]}")
print(f"{current_courses_list[2]} - {course_credits_dictionary[current_courses_list[2]]} credits - {course_professors_dictionary[current_courses_list[2]]} - {course_rooms_dictionary[current_courses_list[2]]}")
print(f"{current_courses_list[3]} - {course_credits_dictionary[current_courses_list[3]]} credits - {course_professors_dictionary[current_courses_list[3]]} - {course_rooms_dictionary[current_courses_list[3]]}")
print(f"{current_courses_list[4]} - {course_credits_dictionary[current_courses_list[4]]} credits - {course_professors_dictionary[current_courses_list[4]]} - {course_rooms_dictionary[current_courses_list[4]]}\n")

print("=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {current_skills_set}")
print(f"Learning Goals: {skills_to_learn_set}")
print(f"Career Interests: {career_interests_set}")
print(f"Skills Currently Have: {len(current_skills_set)}")
print(f"Skills Want to Learn: {len(skills_to_learn_set)}\n")

print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${sum(monthly_budget_dictionary.values())}")
print(f"Food: ${monthly_budget_dictionary['Food']} (${daily_food_budget}/day)")
print(f"Entertainment: ${monthly_budget_dictionary['Entertainment']}")
print(f"Going out: ${monthly_budget_dictionary['Going out']}")
print(f"Personal care: ${monthly_budget_dictionary['Personal care']}")
print(f"Annual Projection: ${annual_projection}\n")

print("=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contact_tuple[1]} ({emergency_contact_tuple[0]}) - {emergency_contact_tuple[2]}")
print(f"Home Address: {home_address_tuple[0]}, {home_address_tuple[1]} {home_address_tuple[2]}")
print(f"Social Media Presence: {total_followers} followers across 2 platforms")
print(f"Key Contacts: {key_contacts_count} people in directory\n")

print("=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {total_courses_completed}")
print(f"Current Academic Load: {current_academic_load} weekly commitments")
print(f"Entertainment Backlog: {entertainment_backlog_count} items")
print(f"Current Hobbies: {current_hobbies_count} activities")
print("="*64)