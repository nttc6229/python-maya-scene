import os
from maya import cmds

def load_object(name):
    scene_objects = cmds.ls()
    cmds.file(os.path.join(os.path.dirname(__file__), "models/{}.obj".format(name)), i=True, prompt=True)
    new_scene_objects = cmds.ls()
    new = set(new_scene_objects) - set(scene_objects)
    return list(new)

def ranGernerator(_):    
    vertexlist = cmds.ls(selection = True, fl= True)
    for i in vertexlist:
        myselposition = cmds.xform(i, query=True, worldSpace=True, translation=True)
        obj = load_object("carrot")[0]
        print(obj)
        cmds.move(myselposition[0], myselposition[1], myselposition[2], obj)

def init():
    if cmds.window("creatwin",exists = True):
        cmds.deleteUI("creatwin")

    myWindow = cmds.window("creatwin", t ="TreeHouse", w = 300, h= 300)
    cmds.columnLayout(adj = True)
    cmds.separator(h=10)
    cmds.button(l="Fir_Tree", h=50, command=ranGernerator)
    cmds.separator(h=10)
    #cmds.button(l="Oak_Tree", h=50, c="ranGernerator()")
    cmds.showWindow(myWindow)