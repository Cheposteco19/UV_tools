from maya import cmds
import maya.mel as mm

def auto_unwrap(*args):
    selected_items=cmds.ls(selection=True)
    for item in selected_items:
        cmds.polyAutoProjection(item)

def camera_based(*args):
    selected_items = cmds.ls(selection=True)
    for item in selected_items:
        cmds.polyProjection(item,type='Planar', mapDirection='p', constructionHistory=True)

def unfold(*args):
    selected_items=cmds.ls(selection=True)
    for item in selected_items:
        cmds.u3dUnfold(item,ite=True,p=False,bi=True,tf=True,ms=1024,rs=False)
    mm.eval("texOrientShells;")
    cmds.u3dLayout(selected_items)

def set_cut_sew_tool(*args):
    cmds.SetCutSewUVTool()

def set_tileable_size(density,map_size):
    mm.eval("texSetTexelDensity {} {};".format(density,map_size))
    mm.eval("texOrientShells;")
    mm.eval("texUnstackShells 1;")
    cmds.DeleteHistory()
    cmds.FreezeTransformations()