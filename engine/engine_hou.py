import hou

hardcoded_path = "D:/GAUTHIER_Nathan/MOVIE/test.hipnc"

class Houdini_engine():
    def openfile(self,filepath):
        hou.hipFile.load(filepath)


    def savefile(self,*arg):
       hou.hipFile.saveAndIncrementFileName()

    def ref_merge(self,*arg):
        pass

    def create_pighead(self):
        pass

    implement = ["openfile", "savefile", "ref_merge", "create_pighead"]


if __name__ == '__main__':
    Houdini_engine.openfile(hardcoded_path)


    '''import sys



package_path = ("C:/Users/etudiant/PycharmProjects/FirstProject/venv/Lib/site-packages")
project_path = ('C:/Users/etudiant/PycharmProjects/FirstProject')

sys.path.append(package_path)
sys.path.append(project_path)

import Qt
import pathlib
import clear
clear.do('tools')
clear.do('engine')

from tools.ui.tool_window import ToolWindow


t = ToolWindow()
t.show()





'''