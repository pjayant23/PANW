B = '236788'
A = '40000023'


#Approach 1 -Naive implementation
naive = str(int(A)+int(B))
print(naive)

#Approach 2 - using reverse string and indexing to add without typecasting
#Time Complexity: O(n+m)
def approach2(A,B):
        list_ints = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        num1 = [str(i) for i in num1]
        num1 = num1[::-1] #reversing the string
        num2 = [str(j) for j in num2]
        num2 = num2[::-1] #reversing string 
        res_A = 0 #to cover scenario when input size varies
        res_B = 0 #to cover scenario when input size varies
        for i in range(len(num1)):
	        curr_num_A = list_ints.index(num1[i]) #mapping index to number in list_ints
	        res_A += curr_num_A * 10 ** i #multiplying value from list_ints to 10 to the power of index 
        for j in range(len(num2)):
	        curr_num_B = list_ints.index(num2[j]) #mapping index to number in list_ints
	        res_B += curr_num_B * 10 ** j #multiplying value from list_ints to 10 to the power of index
        res = res_B + res_A
        return str(res)


#Approch3 - using list reversal, size of list (the logic I was trying to implement on call)
#Time Complexity: O(n)
def approach3(A,B):
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
		ans[i] = num %10 #getting remainder to append to ans useful for 2 digit sum
		ans.append((int(num/10))) # number caary forward identifier
	
	ans = ans[::-1] #returning output to original index
	ans = int(''.join([str(i) for i in ans]) )#removing space and converting to int
	print(str(ans)) #printing answer as a string

approach2(A,B)
approach3(A,B)
