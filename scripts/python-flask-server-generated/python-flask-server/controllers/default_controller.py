from os import listdir
from os.path import isfile, join
from os import walk
from pprint import pprint

def modeldata_get() -> str:

    watchPath = "D:\\test"
    fileID = 0
    modelData = {}



    # modelData['modelPath'] = watchPath.split('\\')
    dongs = watchPath
    print(dongs)

    for root, directories, filenames in walk(watchPath):
        for filename in filenames:
            modelData[str(fileID)] = {}
            # if file extension is .fbx
            modelData[str(fileID)]['modelName'] = filename
            modelData['modelPath'] = watchPath
            fileID += 1
            # print(join(root, filename))
            # # if file extension is .coordinates
            # modelData['modelOffset'] = filename

    return modelData

def writemodel_post(modelDelta = None) -> str:
    return 'do some magic!'