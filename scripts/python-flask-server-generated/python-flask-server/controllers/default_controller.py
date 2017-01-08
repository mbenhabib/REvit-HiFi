from os import listdir
from os.path import isfile, join, splitext
from os import walk
from pprint import pprint
import csv

def modeldata_get() -> str:

    watch_path = "D:\\test"

    filenames = [filename_ext.split(".")[0] for filename_ext in listdir(watch_path)]
    # print(filenames)
    unique_names = set(filenames)
    model_data = {
        "files" : {},
        "rootPath" : watch_path
    }

    coordinates_extension = '.coordinates'

    for f in unique_names:
        with open(join(watch_path, f) + coordinates_extension) as coordinate_file:
            # print(coordinate_file.read())
            coordinates = coordinate_file.read().split(',')
            print(coordinates)
            model_data['files'][f] = {'x': coordinates[0],
                                      'y': coordinates[1],
                                      'z': coordinates[2]}

            # coordinates = coordinate_file.split(',')
            # print(coordinates)
        # f = {}
        # # f['x'] = coordinates[0]
        # # f['y'] = coordinates[1]
        # # f['z'] = coordinates[2]
        # model_data['files'][f] = {'x': coordinates[0],
        #                           'y': coordinates[1],
        #                           'z': coordinates[2]}

    # {"files": {
    #     "dongs1": {"x":, "y":, "z":},
    # "dongs2": {"x":, "y":, "z":},
    # "dongs3": {"x":, "y":, "z":}
    # },
    # "rootPath": "D\\test"
    # }

    # for root, directories, filenames in walk(watch_path):
    #     for filename in filenames:
    #         # create new JS object for each model
    #
    #
    #         # split filename and file_extension
    #         filename, file_extension = splitext(filename)
    #
    #         # # if file extension is .fbx
    #         if file_extension == model_extension:
    #             model_data[filename].append()
    #             # model_data[str(file_id)]['modelName'] = filename + file_extension
    #             parsed_model = True
    #
    #         if file_extension == model_offset_extension:
    #             # model_data[str(file_id)]['modelOffset'] = filename + file_extension
    #             parsed_offset = True
    #
    #
    #         model_data['modelPath'] = watch_path
    #         file_id += 1

    return model_data

def writemodel_post(modelDelta = None) -> str:
    return 'do some magic!'