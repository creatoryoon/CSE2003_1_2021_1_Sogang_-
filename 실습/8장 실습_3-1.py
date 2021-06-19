major = {'computer' : [9, 'R'], 'math' : [2, 'AS'], 'elec' : [11, 'R'], 'psy' : [1, 'X']}
dpt = input('Enter the major : ')
information = major.get(dpt, 'NoData')

if information in list(major.values()):
    major[dpt][0] += 1
    print('{} is floor {} in {}.'.format(dpt, major[dpt][0], major[dpt][1]))
    
else:
    major[dpt] = [1, 'GN']
    print('{} has no data. The arrangement is floor {} in {} .'.format(dpt,major[dpt][0], major[dpt][1]))

print()
print('sorting :', sorted(major.items()))






