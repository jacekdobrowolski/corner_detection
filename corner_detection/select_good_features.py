import numpy as np


def select_good_features(corners: np.ndarray, max_corners: int, min_distance):
    sorted_corners = np.flip(np.argsort(corners.flatten()))
    x, y = np.unravel_index(sorted_corners, corners.shape)
    corners_coordinates = np.stack((x, y), axis=1)
    features = set()
    corners_count = 0
    for corner in corners_coordinates:
        neighbor_in_set = False
        for x in range(corner[1] - min_distance, corner[1] + min_distance):
            for y in range(corner[0] - min_distance, corner[0] + min_distance):
                if features.issuperset({(x, y)}):
                    neighbor_in_set = True
        if not neighbor_in_set:
            features.add(tuple((corner[1], corner[0])))
            corners_count += 1
            if corners_count >= max_corners:
                return features
