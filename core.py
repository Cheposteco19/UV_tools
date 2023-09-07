from maya import cmds

def auto_unwrap(*args):
    selected_objects=cmds.ls(selection=True)
    for obj in selected_objects:
        cmds.polyAutoProjection(obj)

def camara_based(*args):
    selected_objects = cmds.ls(selection=True)
    for obj in selected_objects:
        cmds.polyProjection(obj,type='Planar', mapDirection='p', constructionHistory=True)

def unfold(*args):
    selected_objects=cmds.ls(selection=True)
    for obj in selected_objects:
        cmds.u3dUnfold(obj,ite=True,p=False,bi=True,tf=True,ms=1024,rs=False)

def set_cut_sew_tool(*args):
    cmds.SetCutSewUVTool()

