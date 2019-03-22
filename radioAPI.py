import time
import microbit
import mcpi.minecraft as minecraft
import mcpi.block as block
from objects.meter import meter
from objects.thermometer import thermometer
from objects.block_light import block_light
import microbit_radio.radio_receive as radio_receive

#functions to create by default values
def createMeter(name):
    m = meter(name, 10, 0, 0, 5 ,10, 5)
    m.build_meter()
    return m

def createBlock(name):
    b = block_light(name, 3, 0, 0, 1 ,1, 1)
    b.build_block()
    return b

def createThermometer(name):
    t = thermometer(name, 10, 0, 0) #position from palyer pos
    t.build_ther()
    return t

def error(name):
    print("%s cannot be created", name)
    return name

def createFunctions(argument, name):
    switcher = {
        1: createMeter,
        2: createBlock,
        9: createThermometer,
        0: lambda: error
    }
    func = switcher.get(argument)
    return func(name)

#functions to resize
def resizeMeter(objects, x, y, z):
    objects.meter_delete()
    objects.size_update(x, y, z)
    objects.build_meter()

def resizeBlock(objects, x, y, z):
    objects.block_delete()
    objects.size_update(x, y, z)
    objects.build_block()

def error(name):
    print("%s cannot be resized", name)
    return name

def resizeFunctions(argument, objects, x, y, z):
    switcher = {
        1: resizeMeter,
        2: resizeBlock,
        0: lambda: error
    }
    func = switcher.get(argument)
    return func(objects, x, y, z)

#functions to reposition
def moveMeter(objects, x, y, z):
    objects.meter_delete()
    objects.pos_update(x, y, z)
    objects.build_meter()

def moveBlock(objects, x, y, z):
    objects.block_delete()
    objects.pos_update(x, y, z)
    objects.build_block()

def moveThermometer(objects, x, y, z):
    objects.ther_delete()
    objects.pos_update(x, y, z)
    objects.build_ther()

def error(name):
    print("%s cannot be moved", name)
    return name

def moveFunctions(argument, objects, x, y, z):
    switcher = {
        1: moveMeter,
        2: moveBlock,
        9: moveThermometer,
        0: lambda: error
    }
    func = switcher.get(argument)
    return func(objects, x, y, z)

#functions to update value
def updateMeter(objects, r):
    objects.meter_update(r)

def changeBlock(objects, r):
    objects.change_state()

def updateThermometer(objects, r):
    objects.temp_update(r)

def error(name):
    print("%s cannot be updated", name)
    return name

def updateFunctions(argument, objects, r):
    switcher = {
        1: updateMeter,
        2: changeBlock,
        9: updateThermometer,
        0: lambda: error
    }
    func = switcher.get(argument)
    return func(objects, r)

#functions to post to chat by objects
def chatMeter(objects, msg):
    objects.postToChat(msg)

def chatBlock(objects, msg):
    objects.postToChat(msg)

def chatThermometer(objects, msg):
    objects.postToChat(msg)

def error(name):
    print("%s cannot be moved", name)
    return name

def chatFunctions(argument, objects, msg):
    switcher = {
        1: chatMeter,
        2: chatBlock,
        9: chatThermometer,
        0: lambda: error
    }
    func = switcher.get(argument)
    return func(objects, msg)


#configure the channel
microbit.radio.config("group=0")
microbit.radio.on()
objects = {}

while True:

    msg = radio_receive.receive_msg()

    if msg is not None:
        print(msg)
        #get name length then name
        length = int(msg[2])
        name = msg[3:3+length]
        if msg[0] == "0":
            #create object
            objects[name] = createFunctions(int(msg[1]), name)
        elif msg[0] == "1":
            #get size XXYYZZ
            sizeX = int(msg[3+length: 3+length+2])
            sizeY = int(msg[3+length+2: 3+length+4])
            sizeZ = int(msg[3+length+4: 3+length+6])
            resizeFunctions(int(msg[1]), objects[name], sizeX, sizeY, sizeZ)
        elif msg[0] == "2":
            #get pos XXYYZZ
            posX = int(msg[3+length: 3+length+2])
            posY = int(msg[3+length+2: 3+length+4])
            posZ = int(msg[3+length+4: 3+length+6])
            moveFunctions(int(msg[1]), objects[name], posX, posY, posZ)
        elif msg[0] == "3":
            #get value XXYYZZ
            value = int(msg[3+length: 3+length+2])
            updateFunctions(int(msg[1]), objects[name], value)
        elif msg[0] == "4":
            #find "/"
            index = msg.find("/")
            text = msg[3+length: index]
            chatFunctions(int(msg[1]), objects[name], text)
        else:
            print("error code received")
            

#END
