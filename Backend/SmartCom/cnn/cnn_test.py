from keras.preprocessing import image
import keras
import numpy as np
import pickle
import os



class face_check():
    def __init__(self) -> None:
        abspath = os.path.dirname(os.path.abspath(__file__))
        cnn_model = keras.models.load_model(
            os.path.join(abspath, "face_detect.keras"))
        res_map_file = os.path.join(abspath, "ResultsMap.pkl")
        res_map = {}
        with open(res_map_file, 'rb') as file:
            unpickler = pickle.Unpickler(file)
            res_map = unpickler.load()

        self.model = cnn_model
        self.res_map = res_map

    def check_has_face(self, imgfile):
        test_image = image.load_img(imgfile, target_size=(64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = self.model.predict(test_image, verbose=0)
        predict = self.res_map[np.argmax(result)]
        print('res', result)
        return predict
        return True if (predict == 1) else False


# path_to_test_image = "./Face Images/TestUnknown/biden.jpg"

# test_image = image.load_img(path_to_test_image, target_size=(64, 64))
# test_image = image.img_to_array(test_image)

# test_image = np.expand_dims(test_image, axis=0)

# result = cnn_model.predict(test_image, verbose=0)

# print('Prediction is: ', res_map[np.argmax(result)])
