import os, shutil
import numpy as np

coeff_map = {
    0: float(1 / 3),
    1: float(1 / 2),
    2: float(1),
    3: float(2),
    4: float(3),
}

path_to_models = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")
os.makedirs(path_to_models, exist_ok=True)
for i in range(5):
    for j in range(5):
        for k in range(5):
            model_path = os.path.join(
                path_to_models,
                f"maskedDQN_{np.round(coeff_map[i],2)}_{np.round(coeff_map[j],2)}_{np.round(coeff_map[k],2)}",
            )
            try:
                shutil.copy(
                    os.path.join(path_to_models, "maskedDQN_1.0_1.0_1.0.zip"),
                    model_path + ".zip",
                )
            except shutil.SameFileError:
                pass
