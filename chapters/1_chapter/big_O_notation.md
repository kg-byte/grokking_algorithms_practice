Key takeaways:
1. Algorithm speed isn't measured in seconds, but in growth of the number of operations.
2. Instead, we talk about how quickly the run time of an algorithm increases as the size of the input increases.
3. Run time of algorithms is expressed in Big O notation.
4. O(log n) is faster than O(n), but it gets a lot faster as the list of items you're searching grows.



Following are the key time and space complexities:

Constant: O(1), example: data_list[0], 2*3
Log time: O(log n), example: for loop 
Linear time: O(n), example: binary search
Logarithmic time: O(n log n)
Quadratic time: O(n^2),  example: for i in range(size)... for j in range(size)...
Exponential time: 2 ^(n)
Factorial time: O(n!), example: fibonacci(n)

https://misc-flexiple.s3.amazonaws.com/bon_cheat_sheet.jpg


BASIC
---
Search Algorithms	        Space Complexity	            Time Complexity
                                                     Best Case     Average Case 	Worst Case
Linear Search	                O(1)	                O(1)	     O(n)	        O(n)
Binary Search	                O(1)	                O(1)	     O(log n)    	O(log n)



COMMON
---
Sorting Algorithms	        Space Complexity	            Time Complexity
                                                    Best Case	   Average Case	    Worst Case
Selection Sort	                O(1)	                O(n^2)  	O(n^2)	        O(n^2)
Insertion Sort	                O(1)	                O(n)	    O(n^2)	        O(n^2)
Bubble Sort	                    O(1)	                O(n)	    O(n^2)	        O(n^2)
Quick Sort	                    O(log n)	            O(log n)	O(n log n)  	O(n log n)
Merge Sort	                    O(n)	                O(n)	    O(n log n)  	O(n log n)
Heap Sort	                    O(1)	                O(1)	    O(n log n)  	O(n log n)


ADVANCED
---
Data Structures	            Space Complexity	            Average Case Time Complexity
                                                        Access	        Search	    Insertion	Deletion
Skip List	                    O(n log n)	            O(log n)	    O(log n)	O(log n)	O(log n)
Cartesian Tree              	O(n)	                N/A	O(log n)	O(log n)	O(log n)
B-Tree                      	O(n)                	O(log n)	    O(log n)	O(log n)	O(log n)
Red-Black Tree	                O(n)	                O(log n)    	O(log n)	O(log n)	O(log n)
Splay Tree	                    O(n)	                N/A	            O(log n)	O(log n)	O(log n)
AVL Tree                    	O(n)	                O(log n)	    O(log n)	O(log n)	O(log n)
KD Tree                     	O(n)                	O(log n)	    O(log n)	O(log n)	O(log n)
