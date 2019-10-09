"""Your company built an in-house calendar tool called HiCal. You want to add a
feature to see the times in a day when everyone is available.
To do this, you’ll need to know when any team is having a meeting. In HiCal, a meeting is
stored as a tuple ↴of integers (start_time, end_time). These integers represent the
number of 30-minute blocks past 9:00am.
For example:
 (2, 3) # Meeting from 10:00 – 10:30 am
(6, 9) # Meeting from 12:00 – 1:30 pm
Write a function merge_ranges() that takes a list of multiple meeting time ranges and
returns a list of condensed ranges.
For example, given:
 [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
your function would return:
 [(0, 1), (3, 8), (9, 12)]
Do not assume the meetings are in order. The meeting times are coming from multiple
teams.
Write a solution that's efficient even when we can't put a nice upper bound on the
numbers representing our time ranges. Here we've simplified our times down to the
number of 30-minute slots past 9:00 am. But we want the function to work even for very
large numbers, like Unix timestamps. In any case, the spirit of the challenge is to merge
meetings where start_time and end_time don't have an upper bound."""


a = (0,3) # it's a tuple so this is short for (0,1,2,3), inclusively
b = (3,3)

meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
expected_merge = [(0, 1), (3, 8), (9, 12)] # the time slots taken by meetings, all put together (=merged :))

def merge_meetings(list_of_meetings):
	results = []
	# tmp_list = list_of_meetings.copy() <-- this is because assert works on the entity, not an instance/copy of it, 
	# and any changes are made on that entity (i.e. may be irreversible)

	for meeting in list_of_meetings:	# O(n) - we iterate over the first value in the tuples
		for m in list_of_meetings:		# 0(n) - we iterate over the second value in the tuples
		print(meeting, " - ", m)
# O(n * n) --> computational complexity of the for loop above
	return results

assert merge_meetings(meetings) == expected_merge
assert merge_meetings([(1, 2), (3, 4)]) == [(1, 2), (3, 4)]
assert merge_meetings([(1, 4), (3, 4)]) == [(1, 4)]
assert merge_meetings([(4, 5), (1, 4)]) == [(1, 5)]
