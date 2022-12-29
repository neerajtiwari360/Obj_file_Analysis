from random import randint
import random
import os

def create_vertices():
  fin= 'v 0 0 0' + '\n' + 'v 1 0 0'  + '\n' 'v 0 1 0'
  return fin

def create_normals():
  fin= 'vn 0 0 1' + '\n' + 'vn 1 1 1'  + '\n' 'vn 1 1 1'
  return fin

def create_texture():
  fin= 'vt -1 -1' + '\n' + 'vt 1 1 '  + '\n' 'vt 0 1'
  return fin  

def create_faces():
  v1=1
  v2=2
  v3=3
  vt1=1
  vt2=2
  vt3=3
  vn1=1
  vn2=2
  vn3=3
  s= 'f '+ str(v1)+'/'+str(vt1)+'/'+str(vn1) + ' ' + str(v2)+'/'+str(vt2)+'/'+str(vn2) + ' '+ str(v3)+'/'+str(vt3)+'/'+str(vn3)
  return s 

def create_obj():
  v=create_vertices()
  v_n=create_normals()
  v_t=create_texture()
  f=create_faces()
  s=v+'\n'+v_t+'\n'+v_n+'\n'+ f
  #f = open("triangle.obj", "a")
  file = open('triangle.obj', 'w+')
  file.write(s)
  file.seek(0, os.SEEK_SET)
  #f.write(s)

create_obj()  