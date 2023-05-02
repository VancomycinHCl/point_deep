import open3d as o3d
import open3d.cuda.pybind.io


class PlyReader():
    def __init__(self):
        pass
    def read(self):
        pass

if __name__ == "__main__":
    print("asdf")
    pcd = open3d.cuda.pybind.io.read_point_cloud("../orig_instance/Measurement_1_2_merged.ply",
                                           format='auto',
                                           remove_nan_points=True,
                                           print_progress=True)
    voxel_size = 0.001  # 设置体素大小为0.1
    down_pcd = pcd.voxel_down_sample(voxel_size=voxel_size)
    o3d.visualization.draw_geometries([down_pcd])
    # o3d.cuda.pybind.visualization.draw_geometries([pcd])
    # print(a)
    pass