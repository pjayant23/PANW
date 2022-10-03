B = '236788'
A = '40000023'


#Approach 1 -Naive implementation
naive = str(int(A)+int(B))
print(naive)


#Approch2 - using list reversal, size of list (the logic I was trying to implement on call)
#Time Complexity: O(1)
def approach2(A,B):
	a1 = len(A)
	b1 = len(B)
	n = max(a1, b1)

	A1 = list(map(str, A)) #converting string to list
	B1 = list(map(str, B)) #converting string to list

	A1 = A1[::-1] #reversing list
	B1 = B1[::-1] #reversing list

	ans = [0]
	for i in range(n): #iterating over max length of both inputs
		nA = 0
		nB = 0
		try:
			nA = int(A1[i]) #extracting individual elements from A
		except:
			nA = 0 #error handling incase size(A) < n
		try:
			nB = int(B1[i]) #extracting individual elements frm B
		except:
			nB = 0 ##error handling incase size(B) < n

		num  = ans[i] + nA +nB #addnng digits of the strings A and B from end
		ans[i] = num %10 #getting remainder to append to ans
		ans.append((int(num/10))) #adding answer
	
	ans = ans[::-1] #returning output to original index
	ans = int(''.join([str(i) for i in ans]) )#removing space and converting to int
	print(str(ans)) #printing answer as a string

approach2(A,B)
