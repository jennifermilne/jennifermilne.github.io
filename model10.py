# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib
import tkinter
matplotlib.use('TkAgg')
import requests
import bs4
import random
#import operator
import matplotlib.pyplot
#import time
import AgentFramework
import csv
import matplotlib.animation 
import matplotlib.backends.backend_tkagg

"""
############################################################################
################## Beginning of the time block #############################
############################################################################
start = time.clock()
"""

#############################################################################
############# Work out the distance between two sets of agents ##############
#############################################################################
def distance_between(agents_row_a, agents_row_b):
    dist = (((agents_row_a._x - agents_row_b._x)**2) + ((agents_row_a._y - agents_row_b._y)**2))**0.5
    return dist

"""
############################################################################
################### Previous tests for distance ############################
############################################################################
for i in range (0, num_of_agents):
    for j in range (0, i):
        distance = distance_between(agents[i], agents[j])
        distances.append(distance)
       
print(distances)
len(distances)

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        print(distance)
"""

############################################################################
############################### Add variables ##############################
############################################################################
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

############################################################################
######################## Create empty lists ################################
############################################################################
agents = []
distances = []

############################################################################
######################## Importing environement ############################
############################################################################
f = open('in.txt', 'r', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

environment = []
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)    
#          print(value) #Floats

f.close()
# Don't close until you are done with the reader; the data is read on request.

############################################

random_seed = 1

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#ax.set_autoscale_on(False)

#############################################################################
############################# Scrape the data ###############################
#############################################################################
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

"""
#############################################################################
##################### Test to see if scrape works ###########################
#############################################################################
print(td_ys)
print(td_xs)
"""

#############################################################################
########################### Make the agents #################################
#############################################################################
for i in range(num_of_agents):
    random_seed += 1000
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
#    print("random seed",random_seed)
    agents.append(AgentFramework.Agent(environment,agents, y, x))

carry_on = True

def update(frame_number):
    
    fig.clear() 

############################################################################
########################## Set the boundaries ##############################
############################################################################
    matplotlib.pyplot.ylim(299, 0)
    matplotlib.pyplot.xlim(0, 299)

############################################################################
########################## Plot the environment ############################
############################################################################
# Plot original environment
    #matplotlib.pyplot.imshow(environment)
    #matplotlib.pyplot.show()
    
# Plot current environemnt
    matplotlib.pyplot.imshow(environment)
    global carry_on

############################################################################
########################## Move the agents #################################
############################################################################
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

############################################################################
##################### Plot the agents on top ###############################
############################################################################
    for i in range(num_of_agents):
         matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
#     matplotlib.pyplot.show()

#############################################################################
############################## Eat the agents ###############################
#############################################################################
#for j in range(num_of_iterations):
#    for i in range(num_of_agents):
#        agents[i].move()
#        agents[i].eat()

#operator.itemgetter(1)


if random.random() < 0.1:
        carry_on = False
        print("stopping condition")

#m = max(agents, key=operator.itemgetter(1))
#matplotlib.pyplot.scatter(m[1],m[0], color='red')

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 1000) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

"""
############################################################################
################## Previous animated display for console ###################
############################################################################

animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
matplotlib.pyplot.show()

animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)
matplotlib.pyplot.show()
"""

############################################################################
############################# Run the model ################################
############################################################################
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()

#############################################################################
######################### Build the main window #############################
#############################################################################
root = tkinter.Tk() 

############################################################################
########################### Add a title ####################################
############################################################################
root.wm_title("Model")

############################################################################
#### Creates and lay out a matplotlib canvas embedded within the window ####
############################################################################
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#############################################################################
############################## Make a menu ##################################
#############################################################################
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

"""
#############################################################################
############### Print the maximum and minimum distances #####################
#############################################################################
high = max(distances)
low = min(distances)
print ("max =" + str(high) +  " min =" + str(low))
"""

#a = AgentFramework.Agent(environment, agents) 
#print(a.gety(), a.getx())
#a.move()
#print(a.gety(), a.getx())

############################################################################
#################### Set the GUI waiting for events ########################
############################################################################
tkinter.mainloop()

"""     
#############################################################################
########################## End of the time block ############################
#############################################################################
end = time.clock()
print ("time =" + str(end - start))
"""