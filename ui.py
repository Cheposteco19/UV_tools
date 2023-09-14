from maya import cmds
from uv_editing_tool import core

WINDOW_NAME='uv_editing_tool_ui'
CAMERA_BASED_BUTTON_NAME='camera_based_button'
CUT_SEW_BUTTON_NAME='cut_sew_button'
UNFOLD_BUTTON_NAME='unfold_button'
AUTO_UNWRAP_BUTTON_NAME='auto_unwrap_button'
TILEABLE_1M_BUTTON_NAME='tileable_1m_button'
TILEABLE_2M_BUTTON_NAME='tileable_2m_button'
TILEABLE_CUSTOM_BUTTON_NAME='tileable_custom_button'
CUSTOM_DENSITY_TEXTBOX_NAME='custom_density_textbox'
CUSTOM_MAP_SIZE_TEXTBOX_NAME='custom_map_size_textbox'

def show_ui():
    if cmds.window(WINDOW_NAME,query=True,exists=True):
        cmds.deleteUI(WINDOW_NAME)

    cmds.window(WINDOW_NAME, title='UV Tools', widthHeight=(250,185))

    cmds.columnLayout(adjustableColumn=True)
    cmds.rowLayout(numberOfColumns=2)
    cmds.columnLayout(adjustableColumn=True, backgroundColor=(.1, .1, .2))
    cmds.text(label='BAKED',font='boldLabelFont')
    cmds.button(CAMERA_BASED_BUTTON_NAME,label='Camera-based')
    cmds.button(CUT_SEW_BUTTON_NAME,label='Cut/Sew\nTool',height=38)
    cmds.button(UNFOLD_BUTTON_NAME,label='Unfold',height=47)
    cmds.text(label='',height=35)
    cmds.setParent('..')

    cmds.columnLayout(adjustableColumn=True,backgroundColor=(.1,.2,.1))
    cmds.text(label='TILED', font='boldLabelFont')
    cmds.button(AUTO_UNWRAP_BUTTON_NAME,label='Automatic')
    cmds.rowLayout(numberOfColumns=2)

    cmds.columnLayout(adjustableColumn=True)
    cmds.button(TILEABLE_1M_BUTTON_NAME, label='Tileable 1M\n(10.24|1024)')
    cmds.text(label='Texel density\n(px/inch)')
    cmds.textField(CUSTOM_DENSITY_TEXTBOX_NAME,width=10,text='10.24')
    cmds.text(label='Map size')
    cmds.textField(CUSTOM_MAP_SIZE_TEXTBOX_NAME,width=10,text='4096')
    cmds.setParent('..')

    cmds.columnLayout(adjustableColumn=True)
    cmds.button(TILEABLE_2M_BUTTON_NAME, label='Tileable 2M\n(10.24|2048)')
    cmds.button(TILEABLE_CUSTOM_BUTTON_NAME, label='Custom\nTexel\nDensity',height=80)
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')

    cmds.text(label='GD67_JoseMunguia   ', align='right')

    cmds.showWindow()