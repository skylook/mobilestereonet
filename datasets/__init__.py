from .dataset import SceneFlowDataset, KITTIDataset, DrivingStereoDataset, PicoStereoDataset

__datasets__ = {
    "sceneflow": SceneFlowDataset,
    "kitti": KITTIDataset,
    "drivingstereo": DrivingStereoDataset,
    "pico": PicoStereoDataset
}
