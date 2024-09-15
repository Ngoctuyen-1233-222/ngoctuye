# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:47:49 2024

@author: Student
"""

count=0
n=int(input("nhap vao so can lap:"))
while(count<n):
    print("lan lap thu:",count+1,"\Bien thien:",count)
    count = count+1
else:
    print("\n thuc hien lenh trong else, do:",
          "\ncount=",count,"\nn=",n,
          "\nbool(count<n)=",bool(count,n))
          
