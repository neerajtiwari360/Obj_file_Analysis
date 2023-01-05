def increase_height(vertices,h,indices,size,file):
  new_vertices=copy.copy(vertices)
  new_vertices2=[]
  for v in new_vertices:
    y = list(v)
    y[2] = y[2]+h
    v = tuple(y)
    new_vertices2.append(v)
  f=open(file,'a')
  #f.write('g group1\n')
  for v in new_vertices2:
    print(v)
    f.write('v %f %f %f\n' % (v[0], v[1],v[2]))
  new_indices=[size+1,size+2,size+3]
  #f.write('f 17/1 19/1 18/1\nf 19/1 20/1 18/1\n')
  f.write('f %d/1 %d/1 %d/1\n' % (new_indices[0], new_indices[2],new_indices[1]))
  f.write('f %d/1 %d/1 %d/1\nf %d/1 %d/1 %d/1\n' % (new_indices[1], indices[1],indices[0],new_indices[1],indices[0],new_indices[0]))
  f.write('f %d/1 %d/1 %d/1\nf %d/1 %d/1 %d/1\n' % (new_indices[2], indices[2],indices[1],new_indices[2],indices[1],new_indices[1]))

  f.write('f %d/1 %d/1 %d/1\nf %d/1 %d/1 %d/1\n' % (new_indices[0], indices[0],indices[2],new_indices[0],indices[2],new_indices[2]))
  