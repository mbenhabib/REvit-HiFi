from os import listdir
from os.path import join


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
    return 'do some magic!'
