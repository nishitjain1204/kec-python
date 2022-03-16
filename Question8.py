# 8. A school camp is organized by a school to support the process of preparing their students for an
# examination. They are in need of a study timetable that has the following assumptions:
# Assumptions:
# 1. TotalDaysofCamp - 5 Days
# 2. TotalHoursaday - 5 Hours
# 3. TotalSubjects - 5 Subjects
# Note: The timetable should not follow the same order and should be at random order everyday.
# Prepare a code to help the School.

subs = ['a','b','c','d','e','f']

import random 

existing = []

while len(existing) < 5 :
    random.shuffle(subs)
    new_comb = tuple(subs)
    if  new_comb not in existing:
        existing.append(new_comb)
        
for day in existing:
    print(" ".join(day))
