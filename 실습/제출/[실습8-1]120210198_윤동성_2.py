em = {'kim', 'lee', 'park', 'choi', 'jung', 'kang', 'jo', 'yoon', 'jang',  'lim'}
late = {'yoon', 'park' }
absence = {'jung', 'yoon', 'park', 'lim' }

print("The whole employee :", em)
print("late : ", late)
print("absence : ", absence)
print("The list of the employees that get bonus : ", em.difference(late.union(absence)))
print("The list of the employees that must work overtime :", late.intersection(absence))
new = set(input("Enter the new employees : ").split())
if new.intersection(em) :
    print("the names of the new and existing employees is same.")


print("The list of entire employees :", em.union(new))

