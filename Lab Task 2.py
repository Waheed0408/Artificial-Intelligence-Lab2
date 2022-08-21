from random import randint #Randomly takes integer from given input

play = [] # play is all player names
avg = [] # avg is average runs of players
arr = []
flag = False
counter = 0

inp = open('input1.txt', 'r')

for i in inp:
    arr.append(i.replace('\n', ''))

b,r = arr[0].split() 
b= int(b)   ##b is batsman
r = int(r)  #r is run target

for i in arr[1:]:
    n, run = i.split()
    #avg=run+i
    #p=n+i
    avg.append(run)
    play.append(n)

inp.close()
#input taking finish
def cross(p, q):        #crossover function
    a = len(p) // 2
    f_b = q[:a] + p[a:]
    f_a = p[:a] + q[a:]
    #returning crossover
    return f_a, f_b


def fitness(p, q): #fitness checking function
    c1 = 0
    c = 0

    for i in range(b):
        if p[i] == 1:
            c1 += int(avg[i])

        if q[i] == 1:
            c += int(avg[i])
            
    if c > r - 60 and c < r + 70:
        ft2 = c
    else:
        ft2 = -1

    if c1 > r - 60 and c1 < r + 70:
        ft = c1
    else:
        ft = -1

   
#return fitness
    return ft, ft2


#for generating population
def generate(b):        
    p = [0] * b
    q = [0] * b
    

    for i in range(b):
        #taking random values
        
        p[i] = randint(0, 1) 
        q[i] = randint(0, 1)

    return p, q


#checker function
def checking(x, y, p, q):
    #check if returning nothing
    if x == -1 and y == -1:
        return False
    

#check returning true otherwise
    elif y == r:
        print(q)
        return True
    
    elif x == r:
        print(p)
        return True
    
    else:
        return False


#mutation function
def mutation(p, q):
    
    #taking a random till p
    
    a = randint(0, len(p) - 1)
    
    if q[a] == 0:
        p[a] = 1
    else:
        q[a] = 0

    if p[a] == 0:
        p[a] = 1
    else:
        p[a] = 0

    return p, q


#count variable to set limit on iteration

while not flag:                 #main loop
    p, q = generate(b)
    ft, ft2 = fitness(p, q)
                                   #run when not found 
    if ft == -1 or ft2 == -1:
        continue
    else:
        #cross first
        f_a, f_b = cross(p, q)
        
        #mutate next
        temp_a, temp_b = mutation(f_a, f_b)
        
        #fitness function afterwards
        x, y = fitness(temp_a, temp_b)
        
        #finally flag check and append
        flag = checking(x, y, temp_a, temp_b)


#break when after multiple search, desired output was not found
    counter += 1
    if counter == 200000:                    
        print(-1)
        break

