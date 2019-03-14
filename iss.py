# ISS Project
import json
import turtle
import urllib.request
import pdb
import time

# Astronauts on ISS
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
people = result['people']

print("Astronauts in ISS: \n")
for p in people:
	print(p['name'])
print("\n")

# Where is the Space Station
url1 = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url1)
result = json.loads(response.read())
location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print("Latitude: ",lat)
print("Longitude: ",lon)
lat = float(lat)
lon = float(lon)
#pdb.set_trace()

screen = turtle.Screen()
screen.setup(720,480)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map.gif')

screen.register_shape('iss2.gif')
iss = turtle.Turtle()
iss.shape('iss2.gif')
iss.setheading(90)

iss.penup()
iss.goto(lon,lat)

# locating pass over NCU
lat = 28.503951
lon = 77.049138

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()

url2 = 'http://api.open-notify.org/iss-pass.json'
url2 = url2 + '?lat='+ str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url2)
result = json.loads(response.read())
print(result)
over = result["response"][1]['risetime']

style = ('Harrington',11,'bold')
location.write(time.ctime(over),font=style)


# locating pass over opera house, sydney
lat = -33.856785
lon = 151.215302

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()

url2 = 'http://api.open-notify.org/iss-pass.json'
url2 = url2 + '?lat='+ str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url2)
result = json.loads(response.read())
print(result)
over = result["response"][1]['risetime']

style = ('Harrington',11,'bold')
location.write(time.ctime(over),font=style)
turtle.done()

