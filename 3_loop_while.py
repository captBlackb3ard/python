#!/usr/bin/python3

"""
While loops repeatedly execute a statement or code block as long as a condition is tue.
It requires a setting and manually managing an indexing variable to avoid infinite loops.
"""
i = 1 #Indexing variable
print("Looping from 1 to 5 using a 'while' loop")
while i < 6: #Looping condition evaluation
    print(i)
    i+=1 

#Use the 'break' statement to stop and exit a 'while' loop even if the condition is true
print("\nUsing the 'break' statement to stop and exit a while loop.")
j = 1
while j < 6: #Looping condition evaluation
    print(j)
    if j == 3:
        break;
    j+=1 

#Use the 'continue' statement to skip the current iteration and move onto the next
print("\nUsing the 'continue' statement to skip the current 'while' loop iteration.")
k = 0
while k < 8:
    k+=1
    if k == 4:
        continue
    print(k)

#Use the 'else' statement to execute code once when the conditition is no longer true
print("\nUsing the 'else' statement once the while condition is no longer true.")
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")