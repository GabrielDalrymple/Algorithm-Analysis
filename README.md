# Algorithm Analysis
 CSS 340 Assignment 3: Algorithm Analysis

    Purpose:
        This assignment will focus on algorithm analysis (Big O). It will have both a written part as well
        as a programming part. The goal is to clearly show the impact of algorithms with different
        complexity.   

    Programming Problem:
        Create a module called bigo which has four functions, find1(list, val), find2(list, val),
        find3(list, val), and find4(list, val). Each of the functions will take as arguments a list followed by
        a value. The functions will return a boolean as to whether the val is a member of the list.
        
        The specification for each of the functions is as follows:
            find1(list, val): The unsorted list is searched linearly to see if the val is in the list
            find2(list, val): A deep copy is made of the list then sort w/built-in functionality and binary searched
            find3(list, val): The in built-in is used to determine if the val is in the unsorted list
            find4(list, val): A binary search is performed on the pre-sorted list to find val.
        
        Code the four functions in module as described above. 
        
    Grade:
        45 / 50
            -5: Manual report problems
