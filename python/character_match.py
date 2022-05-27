# Don't forget to run your tests
def is_character_match(string1, string2):
#removing spaces and taking alpha to uppercase
	s1 = string1.replace(" ", "").upper()
	s2 = string2.replace(" ", "").upper()
#casting to list
	unsort_list1 = list(s1)
	unsort_list2 = list(s2)
#creating empty lists to append sorted contents to	
	sort_list1 = []
	sort_list2 = []
#while loop to take the min character append to sort list and remove from unsort list
	while unsort_list1:
		smallest = min(unsort_list1)
		sort_list1.append(smallest)
		unsort_list1.pop(unsort_list1.index(smallest))
#while loop to take the min character append to sort list and remove from unsort list
	while unsort_list2:
		smallest = min(unsort_list2)
		sort_list2.append(smallest)
		unsort_list2.pop(unsort_list2.index(smallest))
#return boolean for comparison of the two lists
	return sort_list1 == sort_list2
