from maya import cmds
import maya.mel as mm

def auto_unwrap(*args):
    selected_items=cmds.ls(selection=True)
    for item in selected_items:
        cmds.polyAutoProjection(item)

def camera_based(*args):
    selected_items = cmds.ls(selection=True)
    new_selection=[]
    for item in selected_items:
        object=item.split('.')[0]
        face_index=cmds.polyEvaluate(item,face=True)-1
        new_selection.append('{}.f[0:{}]'.format(object,face_index))
    print(new_selection)
    cmds.select(new_selection,replace=True)
    cmds.polyProjection(type='Planar', mapDirection='p', constructionHistory=True)

def unfold(*args):
    selected_items=cmds.ls(selection=True)
    for item in selected_items:
        cmds.u3dUnfold(item,ite=True,p=False,bi=True,tf=True,ms=1024,rs=False)
    mm.eval("texOrientShells;")
    cmds.u3dLayout(selected_items)

def set_cut_sew_tool(*args):
    cmds.SetCutSewUVTool()

def set_tileable_size(density,map_size):
    selected_items = cmds.ls(selection=True)
    print(selected_items)
    new_selection = []
    objects=[]
    for item in selected_items:
        if objects.append(item.split('.')[0]) not in objects:
            objects.append(item.split('.')[0])
    print(objects)
    for item in objects:
        map_index = cmds.polyEvaluate(item, uvcoord=True) - 1
        new_selection.append('{}.map[0:{}]'.format(item, map_index))
        print(map_index)
    cmds.select(clear=True)
    cmds.select(objects,replace=True)
    cmds.hilite(objects)
    cmds.select(new_selection, replace=True)

    mm.eval("texSetTexelDensity {} {};".format(density,map_size))
    mm.eval("texOrientShells;")

    mm.eval("texUnstackShells 1;")
    cmds.DeleteHistory()
    cmds.FreezeTransformations()