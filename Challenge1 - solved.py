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

meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]  # entry data
expected_merge = [[0, 1], [3, 8], [9, 12]]  # expected meeting times - whatever is out of range is availability hours


def merge_meetings(list_of_meetings):
    sorted_list = sorted(list_of_meetings)    # sorted() != .sort() - the former only sorts the instance of the object,
    # the latter sets the object in an order
    merged_list = (list(sorted_list[0]),)     # we start with the first item of sorted_list;
    # the after coma is the end time --> a = (0,3)

    for meeting in sorted_list:  # O(n) complexity
        start1 = merged_list[-1][0]     # "in the last item on the list ([-1]) get the first item ([0])"
        end1 = merged_list[-1][1]
        start2 = meeting[0]
        end2 = meeting[1]

        print(meeting)

        if end1 >= start2:
            merged_list[-1][1] = end2 if end2 > end1 else end1 #
        else:
            merged_list.append(meeting)

    return merged_list

""" 1) What is it with wrong attribute in append (l. 44)?
    2) 'Process finished with exit code 0' """


