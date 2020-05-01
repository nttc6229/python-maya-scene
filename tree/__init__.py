import os
from maya import cmds

def tree_a(name):
    foo = cmds.file(
        os.path.join(os.path.dirname(__file__), "./models/Fir_Tree.obj"),
        i=True,
        groupName=name,
        groupReference=True,
    )
    print("foooooo {}".format(foo))
    return foo

def ranGernerator(_):    
    vertexlist = cmds.ls(selection = True, fl= True)
    for i in vertexlist:
        myselposition = cmds.xform(i, query=True, worldSpace=True, translation=True)
        name = "foo"
        tree_a(name)
        cmds.move(myselposition[0], myselposition[1], myselposition[2], name)



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