# -*- coding: utf-8 -*-
#
# Copyright 2011 James Thornton (http://jamesthornton.com)
# BSD License (see LICENSE for details)
#
from bulbs.element import Vertex, Edge

class Registry(object):
    
    def __init__(self, config):
        self.config = config
        self.class_map = dict(vertex=Vertex,edge=Edge)
        self.proxy_map = dict()
        self.index_map = dict()
        self.scripts_map = dict()

    # Classes
    def add_class(self,*classes):
        for element_class in classes:
            # Vertex and Edge are always set by default
            if element_class not in (Vertex, Edge): 
                # TODO: may get into an issue with name clashes
                # a vertex has the same element_type as an edge's label;
                # for now "don't do that".
                element_key = element_class.get_element_key(self.config)
                self.class_map[element_key] = element_class

    def get_class(self,element_key):
        return self.class_map.get(element_key)

    # Proxies
    def add_proxy(self,key,proxy):
        self.proxy_map[key] = proxy

    def get_proxy(self,key):
        return self.proxy_map[key]

    # Indicies
    def add_index(self,key,index):
        self.index_map[key] = index
        
    def get_index(self,key):
        return self.index_map[key]
 
    # Scripts
    def add_scripts(self,key,scripts):
        self.scripts_map[key] = scripts

    def get_scripts(self,key):
        return self.scripts_map[key]

