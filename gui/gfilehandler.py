from filehandler import Universe
import gobject

class GFileHandler(gobject.GObject):
    __gsignals__ = {
        'engine-started' : (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE, (gobject.TYPE_FLOAT))
          }


    def __init__(self):
        gobject.GObject.__init__(self)
        self.univ = Universe()

    def add_dims(self,x,y):
        self.univ.add_dims(x,y)
        emit('notify::dims')
        
    def add_step(self, val):
        self.univ.add_step(val)
        emit('notify::step')
        
    def add_seed(self, val):
        self.univ.add_seed(val)
        emit('notify::step')
        
    def add_spatial_env(self, minx, miny, maxx, maxy, instance_name='SpatialModel', traffic_light=None):
        self.univ.add_spatial_env()
        emit('notify::spatial_env')
        
    def add_traffic_light(self, step, instance_name='TrafficLight', sp = None):
    def add_graph(self, graph, instance_name = 'Graph'):
    def add_spacegraph(self, graph, instance_name = 'SpaceGraph', spatial_model = None, max_obstacle = None, cluster = None, clus = None):
    def add_output(self,filename, step=None):
    def add_node(self, id, class_name = None, pos = None):
    def add_nodegroup(self, id, numnodes, class_name = None):
    def save_file(self, filename):
