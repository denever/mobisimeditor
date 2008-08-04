#! /usr/bin/env python
# -*- Python -*-

from xml.etree.ElementTree import ElementTree, Element, SubElement, dump, parse

class Position:
    def __init__(self):
        self.graph_instance_name = None
        self.random = 'false'
        self.x = None
        self.y = None

    def set_graph_iname(self, val):
        self.graph_instance_name = val
        
    def set_random(self, val):
        self.random = val
        
    def set_x(self, val):
        self.x = val
        
    def set_y(self, val):
        self.y = val
        
    def get_graph_iname(self):
        return self.graph_instance_name
    
    def get_random(self):
        return self.random
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

class Vertex:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        
    def set_id(self, val):
        self.id = val
        
    def set_x(self, val):
        self.x = val
        
    def set_y(self, val):
        self.y = val

    def get_id():
        return self.id

    def get_x():
        return self.x
    
    def get_y():
        return self.y

class Graph:
    def __init__(self):
        self.vertexs = []
        self.edges = []

    def add_vertex(self, vertex):
        self.vertexs.append(vertex)

    def add_edge(self, edge):
        self.edges.append(edge)

    def get_vertexes(self):
        return self.vertexs
    
    def get_edges(self):
        return self.edges            

class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.speed = None

    def set_v1(self, val):
        self.v1 = val
        
    def set_v2(self, val):
        self.v2 = val
        
    def set_speed(self, val):
        self.speed = val

    def get_v1(self):
        return self.v1

    def get_v2(self):
        return self.v2

    def get_speed(self):
        return self.speed

class NumberLane:
    def __init__(self):
        self.full = 'false'
        self.max = None
        self.dir = 'false'
        self.size = 1

    def set_full(self, val):
        self.full = val
        
    def set_max(self, val):
        self.max = val
        
    def set_dir(self, val):
        self.dir = val
        
    def set_size(self, val):
        self.size = val
        
    def get_full(self, val):
        return self.full
    
    def get_max(self, val):
        return self.max
    
    def get_dir(self, val):
        return self.dir
    
    def get_size(self, val):
        return self.size

class Universe:
    def __init__(self):
        self.universe = Element('universe')

    def add_dims(self,x,y):
        dimx = SubElement(self.universe, 'dimx')
        dimx.text = x
        dimy = SubElement(self.universe, 'dimy')
        dimy.text = y

    def add_step(self):
        step = SubElement(self.universe, 'step')

    def add_seed(self):
        seed = SubElement(self.universe, 'seed')

    def add_extension(self, class_name, instance_name = None):
        ext = SubElement(self.universe, 'extension')
        ext.set('class',class_name)
        if instance_name != None:
            ext.set('name', instance_name)

    def add_spatial_env(self, minx, miny, maxx, maxy, instance_name='SpatialModel', traffic_light=None):
        ext = SubElement(self.universe, 'extension')
        ext.set('name', instance_name)
        ext.set('class','de.uni_stuttgart.informatik.canu.spatialmodel.core.SpatialModel')

        if traffic_light != None:
            ext.set('traffic_light',trafficlight)
            
        ext.set('min_x',minx)
        ext.set('min_y',miny)
        ext.set('max_x',maxx)
        ext.set('max_y',maxy)

        if mtls != None:
            max_traffic_lights = SubElement(ext, 'max_traffic_lights')
            max_traffic_lights.text = mtls

        if nl != None:
            number_lane = SubElement(ext, 'number_lane')
            number_lane.set('full',nl.get_full())
            number_lane.set('max',nl.get_max())
            number_lane.set('dir',nl.get_dir())
            number_lane.text = nl.get_size()

        if rd != None:
            reflect_dir = SubElement(ext, 'reflect_directions')
            reflect_dir.text = 'true'

    def add_traffic_light(self, step, instance_name='TrafficLight', sp = None):
        ext = SubElement(self.universe, 'extension')
        ext.set('name',instance_name)
        ext.set('class','eurecom.spatialmodel.extensions.TrafficLight')

        if sp != None:
            ext.set('spatial_model',sp)
        ext.set('step',step)

    def add_graph(self, graph, instance_name = 'Graph'):
        ext = SubElement(self.universe, 'extension')
        ext.set('name',instance_name)
        ext.set('class','eurecom.usergraph.UserGraph')

        for ver in graph.get_vertexes():
            vertex = SubElement(ext, 'vertex')
            id = SubElement(vertex, 'id')
            id.text = ver.get_id()
            x = SubElement(vertex,'x')
            x.text = ver.get_x()
            y = SubElement(vertex,'y')
            y.text = ver.get_y()

        for edg in graph.get_edges():
            edge = SubElement(ex, 'edge')
            v1 = SubElement(edge, 'v1')
            v1.text = edg.get_v1()
            v2 = SubElement(edge, 'v2')
            v2.text = edg.get_v2()
            
            if edg.speed != None:
                speed = SubElement(edge, 'speed')
                speed.text = edg.get_speed()

    def add_spacegraph(self, graph, instance_name = 'SpaceGraph', spatial_model = None, max_obstacle = None, cluster = None, clus = None):
        ext = SubElement(self.universe, 'extension')
        ext.set('name',instance_name)
        ext.set('class','eurecom.spacegraph.SpaceGraph')

        if spatial_model != None:
            ext.set('spatial_mode',spatial_model)

        if traffic_light != None:
            ext.set('traffic_light', traffic_light)

        if max_obstacle != None:
            ext.set('max_obstacle', max_obstacle)

        if cluster != None:
            ext.set('cluster', 'true')        

        clusters = SubElement(ext, 'clusters')
        clusters.set('density', clus.density)
        
        for clu in clus.clusters:
            cluster = SubElement(clusters, 'cluster')
            cluster.set('name',clu.name)

            density = SubElement(cluster,'density')
            density.text = clu.density

            ratio = SubElement(cluster,'ratio')
            ratio.text = clu.ratio

            if clu.speed != None:
                speed = SubElement(cluster, 'speed')
                speed.text = clu.speed

    def add_output(self,filename, step=None):
        ext = SubElement(self.universe, 'extension')
        ext.set('class','de.uni_stuttgart.informatik.canu.spatialmodel.extensions.ReportNodeMobility')
        ext.set('output',filename)

        if step != None:
            st = SubElement(ext, 'step')
            
    def add_node(self, id, class_name = None, pos = None):
        node = SubElement(self.universe, 'node')
        node.set('id',id)

        if class_name != None:
            node.set('class',class_name)
            
        if pos != None:
            position = SubElement(node,'position')

            if pos.get_random() == True:
                position.set('random','true')

            if pos.get_graph_iname() != None:
                position.set('graph',pos.graph)

            if pos.get_x() != None and pos.get_y() != None:
                posx = SubElement(position,'x')
                posy = SubElement(position,'y')
                posx.text = pos.get_x()
                posy.text = pos.get_y()

        if type != None:
            type = SubElement(node,'type')

        if ext != None:
            extension = SubElement(node, 'extension')
        
    def add_nodegroup(self, id, numnodes, class_name = None):
        nodegroup = SubElement(self.universe, 'nodegroup')
        nodegroup.set('n', numnodes)

        if class_name != None:
            nodegroup.set('class',class_name)
            
        nodegroup.set('id', id)
        
        if pos != None:
            position = SubElement(nodegroup,'position')

            if pos.get_random() == True:
                position.set('random','true')

            if pos.get_graph_iname() != None:
                position.set('graph',pos.graph)

            if pos.get_x() != None and pos.get_y() != None:
                posx = SubElement(position,'x')
                posy = SubElement(position,'y')
                posx.text = pos.get_x()
                posy.text = pos.get_y()

    def save_file(self, filename):
        ElementTree(self.universe).write(filename)

if __name__ == '__main__':
    prova = Universe()
    prova.add_dims('10','10')
    prova.add_step()
    prova.add_seed()
    prova.save_file('prova.xml')
    
