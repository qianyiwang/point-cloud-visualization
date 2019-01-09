
import os
import numpy as np
import mayavi.mlab
class VelodynePointsViz():
	"""docstring for VelodynePointsViz"""

	def __init__(self, path):
		self.velo_path = path
		self.points = []
		self.map = None

	def __load_kitti_velo_points(self, file_name, chunksize=4): # this is a private function

		path = os.path.join(self.velo_path, file_name)
		self.points = np.fromfile(path, dtype=np.float32).reshape(-1, chunksize)
		
	def plot_velo_frame_mayai(self, file_name, points = 0.2):

	    if len(self.points) == 0 and file_name != None:
	    	self.__load_kitti_velo_points(file_name)

	    fig = mayavi.mlab.figure(bgcolor=(0, 0, 0), size=(640, 360))
	    mayavi.mlab.points3d(
	        self.points[:, 0],   # x
	        self.points[:, 1],   # y
	        self.points[:, 2],   # z
	        self.points[:, 2],   # Height data used for shading
	        mode="point", # How to render each point {'point', 'sphere' , 'cube' }
	        colormap='spectral',  # 'bone', 'copper',
	        #color=(0, 1, 0),     # Used a fixed (r,g,b) color instead of colormap
	        scale_factor=100,     # scale of the points
	        line_width=10,        # Scale of the line, if any
	        figure=fig,
	    )
	    # velo[:, 3], # reflectance values
	    mayavi.mlab.show()

	def plot_velo_frame_matplotlib(self, file_name=None):
	    import matplotlib.pyplot as plt
	    from mpl_toolkits.mplot3d import Axes3D

	    if len(self.points) == 0 and file_name != None:
	    	self.__load_kitti_velo_points(file_name)

	    skip = 100   # Skip every n points

	    fig = plt.figure()
	    ax = fig.add_subplot(111, projection='3d')
	    point_range = range(0, self.points.shape[0], skip) # skip points to prevent crash
	    ax.scatter(self.points[point_range, 0],   # x
	               self.points[point_range, 1],   # y
	               self.points[point_range, 2],   # z
	               c=self.points[point_range, 2], # height data for color
	               cmap='gray',
	               marker="o")
	    ax.axis('scaled')  # {equal, scaled}
	    plt.show()

	@mayavi.mlab.animate(delay = 200) # todo: change for to while
	def __update_animation(self):
		for f in os.listdir(self.velo_path):
			self.map.mlab_source.set(self.__load_kitti_velo_points(f))
			yield

	def kitti_velo_animat(self, start_file):
		self.__load_kitti_velo_points(start_file)
		fig = mayavi.mlab.figure(bgcolor=(0, 0, 0), size=(640, 360))
		self.map = mayavi.mlab.points3d(
			self.points[:, 0],   # x
			self.points[:, 1],   # y
			self.points[:, 2],   # z
			self.points[:, 2],   # Height data used for shading
			mode="point", # How to render each point {'point', 'sphere' , 'cube' }
			colormap='spectral',  # 'bone', 'copper',
			#color=(0, 1, 0),     # Used a fixed (r,g,b) color instead of colormap
			scale_factor=100,     # scale of the points
			line_width=10,        # Scale of the line, if any
			figure=fig,
		)
		self.__update_animation()
		mayavi.mlab.show()

	    