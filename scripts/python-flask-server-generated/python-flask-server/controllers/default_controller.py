from os import listdir
from os.path import join
from flask import request
import csv

def modeldata_get() -> str:

    watch_path = "D:\\test"

    filenames = [filename_ext.split(".")[0] for filename_ext in listdir(watch_path)]
    unique_names = set(filenames)
    model_data = {
        "files" : {},
        "rootPath" : watch_path
    }

    coordinates_extension = '.coordinates'

    for f in unique_names:
        with open(join(watch_path, f) + coordinates_extension) as coordinate_file:
            coordinates = coordinate_file.read().split(',')
            print(f + ": " + str(coordinates))
            model_data['files'][f] = {'x': coordinates[0],
                                      'y': coordinates[1],
                                      'z': coordinates[2]}
    return model_data


def writemodel_post(modelDelta = None) -> str:
    upload_path = "D:\\upload"
    upload_name = "modelDeltas.csv"
    csv_header = "modelName, positiondeltaX, positiondeltaY, positiondeltaZ, rotationDeltaX, rotationDeltaY, rotationDeltaZ, scaleDeltaX, scaleDeltaY, scaleDeltaZ\n"

    data = request.get_json()
    model_names = list(data.keys())
    print(model_names)

    with open(join(upload_path, upload_name), "w") as file:
        file.write(csv_header)
        for item in data:
            item_string = str(item)
            # modelName, positiondeltaX, positiondeltaY, positiondeltaZ, rotationDeltaX, rotationDeltaY, rotationDeltaZ, scaleDeltaX, scaleDeltaY, scaleDeltaZ
            print(item + ', ', data[str(item_string)]['positionDelta']['x'] + ', ', data[item_string]['positionDelta']['y'] + ', ', data[item_string]['positionDelta']['z'] + ', ')
            row = (item + ', ' + 
                   data[str(item_string)]['positionDelta']['x'] + ', ' + data[item_string]['positionDelta']['y'] + ', ' + data[item_string]['positionDelta']['z'] + ', ' +
                   data[str(item_string)]['rotationDelta']['x'] + ', ' + data[item_string]['rotationDelta']['y'] + ', ' + data[item_string]['rotationDelta']['z'] + ', ' +
                   data[str(item_string)]['scaleDelta']['x'] + ', ' + data[item_string]['scaleDelta']['y'] + ', ' + data[item_string]['scaleDelta']['z'] + ', ' + '\n')
            print(row)
            file.write(row)

    return 'do some magic!'
