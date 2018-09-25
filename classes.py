

class Student:
    def __init__( self, fname, lname, grade):
        self.fname = fname
        self.lname = lname
        self.grade = grade


    def hello(self):
        print("Hello {f} {l}!  \nWelcome to the grade:{g}".format(f = self.fname, l = self.lname, g = self.grade))
    
    def gradecal(self, grades):

        gr = ['a', 'b', 'c', 'd', 'f']
        score = [ 90, 80, 70, 60, 50 ]

        lettergrades = []

        for g in grades:
            if g < 59:
                lettergrades.append('f')
            else:
                for i, j in enumerate(score):
                    if g > j:
                        lettergrades.append(gr[i])
                        break

        print(lettergrades)

student = Student('Warren', 'Wrate', 5)

grades = [63,92,98,88,75,85]

print(sum(grades)/len(grades))

student.hello()
student.gradecal(grades)

list1 = [5,1,2,3,4,5,6,7,8,9]

list2 = [x for ind, x in enumerate(list1) if 4 > ind > 0]

print(list2)

dl1 = [0,1,2,3]
dl2 = [4,5,6,7]

k = [1,2,3,4,5]

n = [1,2,3]

eggfloor = [[0 for x in k] for x in n]

eggfloor2 = [ t * 10 for t in [t for t in n]]

print(eggfloor)
print(eggfloor2)


nl = [ x**2 for x in  [ x**2 for x in range(1,5)]]
print(nl)

h = { 'name': 'warren',
      'favfood': 'padthai'
      }

h['lname'] = 'wrate'

print(h['name'], h['lname'])

part = {
    'pname': 'bob smith',
    'deps': [
        {
        'dname': 'mary smith',
        'age': 30,
        'spouse': True
        },
        {
        'dname': 'bily',
        'age': 4,
        'spouse': False
        },
        {
        'dname': 'tommy smith',
        'age': 6,
        'spouse': False
        }
    ]
}

part['depcount'] = len(part['deps'])



part['childcount'] = len([dep for dep in part['deps'] if dep['spouse'] == False])

part['eligible'] = len([dep for dep in part['deps'] if (dep['spouse'] == False and dep['age'] < 26 ) or dep['spouse'] == True ])


print(part['depcount'] )

print(part['childcount'] )

print(part['eligible'] )



