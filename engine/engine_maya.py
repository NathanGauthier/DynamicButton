import pymel.core as pm

hardcoded_path = "D:/GAUTHIER_Nathan/MOVIE/ASSETS/CAR/RIG/PUBLISH/CAR_RIG_v001.mb"

class Maya_engine():
    def openfile(self,filepath):
        pm.openFile(filepath, force=True)


    def savefile( self,*arg):
        pm.saveFile(force=True)

    def ref_merge(self,*arg):
        pm.system.createReference(pm.fileDialog2(fileMode=1, caption="reference"))


    implement = ["openfile","savefile", "ref_merge"]

if __name__ == '__main__':
    Maya_engine.openfile(hardcoded_path)