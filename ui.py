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

    cmds.gridLayout(autoGrow=True,numberOfRowsColumns=(3,2),cellWidthHeight=(200,60))
    cmds.button(label='1000000000000000000')
    cmds.button(label='1')
    cmds.button(label='1')
    cmds.text(label='100000000000000000')
    cmds.text(label='1')
    cmds.text(label='1')

    cmds.showWindow()