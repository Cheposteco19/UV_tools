from maya import cmds
from uv_editing_tool import core

WINDOW_NAME='uv_editing_tool_ui'
CAMERA_BASED_BUTTON_NAME='camera_based_button'
CUT_SEW_BUTTON_NAME='cut_sew_button'
UNFOLD_BUTTON_NAME='unfold_button'
AUTO_UNWRAP_BUTTON_NAME='auto_unwrap_button'
LAYOUT_BUTTON_NAME='layout_button'
TILEABLE_1M_BUTTON_NAME='tileable_1m_button'
TILEABLE_2M_BUTTON_NAME='tileable_2m_button'
TILEABLE_CUSTOM_BUTTON_NAME='tileable_custom_button'
CUSTOM_DENSITY_TEXTBOX_NAME='custom_density_textbox'
CUSTOM_MAP_SIZE_TEXTBOX_NAME='custom_map_size_textbox'

def show_ui():
    if cmds.window(WINDOW_NAME,query=True,exists=True):
        cmds.deleteUI(WINDOW_NAME)

    cmds.window(WINDOW_NAME, title='UV Editing Tool', widthHeight=(500,100))

    cmds.rowLayout(numberOfColumns=3,adjustableColumn3=3)
    cmds.text(label='\n1 [base]\n\n2 [edit]\n\n\n\n3 [size]\n\n\n')

    cmds.columnLayout(adjustableColumn=True)
    cmds.button(CAMERA_BASED_BUTTON_NAME,label='Camera-based')

    cmds.rowLayout(numberOfColumns=2)
    cmds.button(CUT_SEW_BUTTON_NAME,label='Cut/Sew\nTool',recomputeSize=True)
    cmds.button(UNFOLD_BUTTON_NAME,label='Unfold',recomputeSize=True)
    cmds.setParent('..')

    cmds.button(LAYOUT_BUTTON_NAME,label='Layout',recomputeSize=True)
    cmds.text(label='\n\n\n')

    cmds.setParent('..')

    cmds.columnLayout(adjustableColumn=True)

    cmds.button(AUTO_UNWRAP_BUTTON_NAME,label='Automatic',recomputeSize=True)

    cmds.text(label='\n\n')
    cmds.rowLayout(numberOfColumns=2)
    cmds.button(TILEABLE_1M_BUTTON_NAME, label='Tileable 1M\n(10.24|1024)',recomputeSize=True)
    cmds.button(TILEABLE_2M_BUTTON_NAME, label='Tileable 2M\n(10.24|2048)',recomputeSize=True)
    cmds.setParent('..')
    cmds.rowLayout(numberOfColumns=3,adjustableColumn3=1)
    cmds.textField(CUSTOM_DENSITY_TEXTBOX_NAME)
    cmds.textField(CUSTOM_MAP_SIZE_TEXTBOX_NAME)
    cmds.button(TILEABLE_CUSTOM_BUTTON_NAME, label='Set Custom\nTexel Density',recomputeSize=True)

    cmds.showWindow()