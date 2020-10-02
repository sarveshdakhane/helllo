from queue import PriorityQueue


q = PriorityQueue()

'''
customers.append((2,"Alia"))
customers.append((3,"roshan"))
customers.append((4,"Sham"))
'''

q.put((4, 'Read'))
q.put((2, 'Play'))
q.put((5, 'Write'))
q.put((1, 'Code'))
q.put((3, 'Study'))


while q.not_empty:
    print(q.get())
