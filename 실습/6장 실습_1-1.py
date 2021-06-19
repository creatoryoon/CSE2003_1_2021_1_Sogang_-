#!/usr/bin/env python
# coding: utf-8

# In[4]:


num1, num2, num3 = input('실수 세 개 입력 : ').split()
num1_f, num2_f, num3_f = float(num1), float(num2), float(num3)
print('********************************************')
if num1_f > num2_f > num3_f: 
    mid_ = num2_f
    
    
elif num1_f > num3_f > num2_f:
    mid_ = num3_f
    
    
elif num2_f > num1_f > num3_f:
    mid_ = num1_f
    
    
elif num2_f > num3_f > num1_f:
    mid_ = num3_f
    
    
elif num3_f > num1_f > num2_f:
    mid_ = num1_f     

    
elif num3_f > num2_f > num1_f:
    mid_ = num2_f

    
elif (num1_f == num2_f != num3_f or num3_f == num1_f != num2_f):
    mid_ = num1_f
    
    
elif (num2_f == num3_f != num1_f):
    mid_ = num2_f
    
    
else:
    mid_ = num1_f
    
print('중간 값 :', mid_)


# In[ ]:




