#!/usr/bin/env python
# coding: utf-8

# In[1]:


fp_r = open('input.txt', 'r')
fp_w = open('st_out.txt', 'w')

for i, s in list(enumerate(fp_r)):
    hour, minute, time = s.split()
    hour = int(hour); minute = int(minute); time = int(time)
    time_add = hour * 60 + minute + time
    
    if time_add >= 0:
        real_hour = time_add // 60 % 24
        real_minute = (hour * 60 + minute + time) % 60
        print('{}: time = {}:{}'.format(i+1, real_hour, real_minute), file = fp_w, end = '')
        
    else:        
        time_add_hour = abs(time) // 60
        time_add_minute = abs(time) % 60        
        if (minute - time_add_minute) < 0:   
            real_hour = (abs(hour - time_add_hour) % 24)
            real_minute = 60 + minute - time_add_minute          
            print('{}: time = {}:{}'.format(i+1, 24 - real_hour - 1, real_minute), file = fp_w, end = '')
                       
        else:
            real_hour = abs(hour - time_add_hour) % 24
            real_minute = minute - time_add_minute
            print('{}: time = {}:{}'.format(i+1, 24 - real_hour, real_minute), file = fp_w, end = '')                   
                       
        
    fp_w.write('\n')
     

fp_r.close();fp_w.close()


# In[ ]:




