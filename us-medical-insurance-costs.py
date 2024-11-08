#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs

# In[1]:


#Determine the differences in medical costs regionally, between male and females, non-smokers and smokers, between various age groups, and between those who have children and those who do not. Assumption is that charges are on based on U.S. dollar amounts.


# In[2]:


import csv

records = {}
# retreive data from CSV file and store in dictionary with id for each record
with open('insurance.csv') as csv_file:
    insurance_records = csv.DictReader(csv_file)
    id = 1
    for key in insurance_records:
        records[id] = key
        id += 1


# In[3]:


#dictionary and list based on regions in records
def records_by_region():
    for id in records:
        current_region = records[id]["region"]
        current_record = records[id]        
        if current_region not in records_region.keys():
            records_region[current_region] = {id: current_record}
        else:
            records_region[current_region].update({id: current_record})
    return records_region


# In[5]:


records_region = {}
records_by_region()
list_region = records_region.keys()
#print(record_region)


# In[8]:


#dictionary and list based on sex in records
def records_by_sex():
    for id in records:
        current_sex = records[id]["sex"]
        current_record = records[id]
        if current_sex not in records_sex.keys():
            records_sex[current_sex] = {id: current_record}
        else:
            records_sex[current_sex].update({id: current_record})
    return records_sex


# In[9]:


records_sex = {}
records_by_sex()
list_sex = records_sex.keys()
#print(records_by_sex())


# In[10]:


#dictionary based on smoker in records
def records_by_smoker():
    for id in records:
        current_smoker = records[id]["smoker"]
        current_record = records[id]
        if current_smoker not in records_smoker.keys():
            records_smoker[current_smoker] = {id: current_record}
        else:
            records_smoker[current_smoker].update({id: current_record})
    return records_smoker


# In[11]:


records_smoker = {}
records_by_smoker()
list_smoker = records_smoker.keys()
#print(records_by_smoker())


# In[12]:


#dictionary and list based on ranges of age in records
def records_by_age_range():
    for id in records:
        current_age = records[id]["age"]
        current_record = records[id]
        if int(current_age) in range(0, 18):
            current_age_range = '0-17'
        elif int(current_age) in range(18, 26):
            current_age_range = '18-25'
        elif int(current_age) in range(26, 40):
            current_age_range = '26-39'
        elif int(current_age) in range(40, 65):
            current_age_range = '40-64'
        elif int(current_age) in range(65, 100):
            current_age_range = '65-99'
        else:
            current_age_range = 'Other'
        if current_age_range not in records_age_range:
            records_age_range[current_age_range] = {id: current_record}
        else:
            records_age_range[current_age_range].update({id: current_record})
    return records_age_range


# In[13]:


records_age_range = {}
records_by_age_range()
list_age_range = records_age_range.keys()
#print(records_by_age_range())


# In[14]:


#dictionary based on those having children or not
def records_by_children():
    for id in records:
        current_child = records[id]["children"]
        current_record = records[id]
        if int(current_child) == 0:
            current_answer = 'no'
        elif int(current_child) > 0:
            current_answer = 'yes'
        else:
            current_answer = 'other'
        if current_answer not in records_children:
            records_children[current_answer] = {id: current_record}
        else:
            records_children[current_answer].update({id: current_record})
    return records_children


# In[15]:


records_children = {}
records_by_children()
list_children = records_children.keys()
#print(records_by_children())


# In[16]:


# determine medical costs by region
def costs_region(regions=list_region):
    for region in regions:
        total_cost = 0.0
        min_cost = float('inf')
        max_cost = 0.0
        num_records = len(records_region[region])
        for id in records_region[region]:
            cost = float(records_region[region][id]['charges'])
            total_cost += cost
            if cost < min_cost:
                min_cost = cost
            if cost > max_cost:
                max_cost = cost
        cost_region[region] = {'Cases': num_records
                               , 'Total': int(total_cost)
                               , 'Avg': int(total_cost / num_records)
                               , 'Min': int(min_cost)
                               , 'Max': int(max_cost)
                              }
    return cost_region


# In[17]:


#Enter region(s) as list to return medical cost information based on region
cost_region = {}
costs_region()
#print(list_region)

for region in cost_region:
    print("For the {region}, the number cases was {num} with total charges of ${total}. The average charge was ${avg}, the minumum was ${min}, and maximum was ${max}.".format(region=region, num=cost_region[region]['Cases'], total=cost_region[region]['Total'], avg=cost_region[region]['Avg'], min=cost_region[region]['Min'], max=cost_region[region]['Max']))
    


# In[18]:


#All four regions have close to the same amount of representation in the dataset. The southwest has the lowest average medical costs at $12,346, with the northwest close to it with about $100 higher in charges. The southeast is has the highest average medical costs at $14,375, which are $2,000 more than the southwest. The northeast is second highest, with about $900 less in charges than the southeast.


# In[19]:


# determine medical costs by sex
def costs_sex(sexes=list_sex):
    for sex in sexes:
        total_cost = 0.0
        min_cost = float('inf')
        max_cost = 0.0
        num_records = len(records_sex[sex])
        for id in records_sex[sex]:
            cost = float(records_sex[sex][id]['charges'])
            total_cost += cost
            if cost < min_cost:
                min_cost = cost
            if cost > max_cost:
                max_cost = cost
        cost_sex[sex] = {'Cases': num_records
                         , 'Total': int(total_cost)
                         , 'Avg': int(total_cost / num_records)
                         , 'Min': int(min_cost)
                         , 'Max': int(max_cost)
                        }
    return cost_sex


# In[20]:


#Enter sex(es) as list to return medical cost information based on sex
cost_sex = {}
costs_sex()
#print(list_sex)

for sex in cost_sex:
    print("For {sex}s, the number cases was {num} with total charges of ${total}. The average charge was ${avg}, the minumum was ${min}, and maximum was ${max}.".format(sex=sex, num=cost_sex[sex]['Cases'], total=cost_sex[sex]['Total'], avg=cost_sex[sex]['Avg'], min=cost_sex[sex]['Min'], max=cost_sex[sex]['Max']))
    


# In[21]:


#Fairly even number of males (676) and females (662) represented in the dataset. Males have higher average medical cost than females, at around 1,400 more.


# In[22]:


# determine medical costs by smoker status
def costs_smoker(smoker=list_smoker):
    for status in smoker:
        total_cost = 0.0
        min_cost = float('inf')
        max_cost = 0.0
        num_records = len(records_smoker[status])
        for id in records_smoker[status]:
            cost = float(records_smoker[status][id]['charges'])
            total_cost += cost
            if cost < min_cost:
                min_cost = cost
            if cost > max_cost:
                max_cost = cost
        cost_smoker[status] = {'Cases': num_records
                               , 'Total': int(total_cost)
                               , 'Avg': int(total_cost / num_records)
                               , 'Min': int(min_cost)
                               , 'Max': int(max_cost)
                              }
    return cost_smoker


# In[23]:


#Enter smoker status(es) as list to return medical cost information based on smoker status
cost_smoker = {}
costs_smoker()
#print(list_smoker)

for status in cost_smoker:
    print("For those who enter '{status}' for smoking, the number cases was {num} with total charges of ${total}. The average charge was ${avg}, the minumum was ${min}, and maximum was ${max}.".format(status=status, num=cost_smoker[status]['Cases'], total=cost_smoker[status]['Total'], avg=cost_smoker[status]['Avg'], min=cost_smoker[status]['Min'], max=cost_smoker[status]['Max']))
    


# In[24]:


#The average medical costs are significantly higher for smokers, almost 4 times more than non-smokers. Smokers also represent a significantly smaller portion of the medical records captured, 274 cases compared to 1,064 cases for non-smokers, yet their total cost is close to the same as non-smokers.


# In[25]:


# determine medical costs by age_range
def costs_age_range(age_range=list_age_range):
    for range in age_range:
        total_cost = 0.0
        min_cost = float('inf')
        max_cost = 0.0
        num_records = len(records_age_range[range])
        for id in records_age_range[range]:
            cost = float(records_age_range[range][id]['charges'])
            total_cost += cost
            if cost < min_cost:
                min_cost = cost
            if cost > max_cost:
                max_cost = cost
        cost_age_range[range] = {'Cases': num_records
                                 , 'Total': int(total_cost)
                                 , 'Avg': int(total_cost / num_records)
                                 , 'Min': int(min_cost)
                                 , 'Max': int(max_cost)
                                }
    return cost_age_range


# In[26]:


#Enter age range(s) as list to return medical cost information based on age range
cost_age_range = {}
costs_age_range()
#print(list_age_range)

for age in cost_age_range:
    print("For those {age} years of age, the number cases was {num} with total charges of ${total}. The average charge was ${avg}, the minumum was ${min}, and maximum was ${max}.".format(age=age, num=cost_age_range[age]['Cases'], total=cost_age_range[age]['Total'], avg=cost_age_range[age]['Avg'], min=cost_age_range[age]['Min'], max=cost_age_range[age]['Max']))
    


# In[27]:


#The average medical costs rise with each age range represented. There is a significant increase in the average for those in the third group of 40-64, at $16,430 it is almost $5,000 more than the 25-39 group. The difference between the first and second group is around $2,000. In the addition, the third has almost double the number of cases compared to the other two groups. Insterestingly, the minimum and maximum charges also increase with successive age range. As there is no one 65 and older in this dataset, presumably their costs are under Medicare.


# In[28]:


# determine medical costs by those having children or not
def costs_children(children=list_children):
    for status in children:
        total_cost = 0.0
        min_cost = float('inf')
        max_cost = 0.0
        num_records = len(records_children[status])
        for id in records_children[status]:
            cost = float(records_children[status][id]['charges'])
            total_cost += cost
            if cost < min_cost:
                min_cost = cost
            if cost > max_cost:
                max_cost = cost
        cost_children[status] = {'Cases': num_records
                                 , 'Total': int(total_cost)
                                 , 'Avg': int(total_cost / num_records)
                                 , 'Min': int(min_cost)
                                 , 'Max': int(max_cost)
                                }
    return cost_children


# In[29]:


cost_children = {}
costs_children()
#print(list_children)

for status in cost_children:
    print("For those who entered '{status}' for having any children, the number cases was {num} with total charges of ${total}. The average charge was ${avg}, the minumum was ${min}, and maximum was ${max}.".format(status=status, num=cost_children[status]['Cases'], total=cost_children[status]['Total'], avg=cost_children[status]['Avg'], min=cost_children[status]['Min'], max=cost_children[status]['Max']))
    


# In[30]:


#The average medical costs is higher for those who have children, at $13,949 it is approximately $1,600 more. In addition, there are about 200 more cases with those who have children than those who do not.
#It was not explored if, or how, the number of children may impact the medical cost amounts (i.e., fewer or more children).


# In[ ]:




