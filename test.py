from velodyne_pointcloud_viz import VelodynePointsViz

velo_viz = VelodynePointsViz('../self-driving-viz/kitti_data/2011_09_26/2011_09_26_drive_0001_sync/velodyne_points/data')
# velo_viz.plot_velo_frame_mayai('0000000000.bin')
# velo_viz.plot_velo_frame_matplotlib('0000000000.bin')
velo_viz.kitti_velo_animat('0000000000.bin')