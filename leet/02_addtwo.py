### Add Two Numbers ###

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

### EXAMPLE ###
#	Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#	Output: 7 -> 0 -> 8
#	Explanation: 342 + 465 = 807. 


# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

def addTwoNumbers(l1, l2):
	s = r = ListNode(l1.val + l2.val) 	
	l1 = l1.next
	l2 = l2.next
	
	while l1 != None or l2 != None:
		if l1 == None:
			r.next = ListNode(l2.val)
			l2 = l2.next
			r = r.next
		elif l2 == None:
			r.next = ListNode(l1.val)
			l1 = l1.next
			r = r.next
		else:
			r.next = ListNode(l1.val + l2.val)
			l1 = l1.next
			l2 = l2.next			
			r = r.next
	
	l = s
	while l != None:
		if l.val > 9:
			if l.next == None:
				l.next = ListNode(1)
				l.val = l.val % 10
			else:
				l.next.val += 1
				l.val = l.val % 10		

		l = l.next

	return s
	
	
two = ListNode(2)
four = ListNode(4)
three = ListNode(3)
five = ListNode(5)
six = ListNode(6)
four2 = ListNode(4)

two.next = four
four.next = three
five.next = six
six.next = four2

result =  addTwoNumbers(ListNode(5), ListNode(5))
#result =  addTwoNumbers(two, five)


print result.val,
result = result.next
while result != None:
	print " -> ", result.val,
	result = result.next
