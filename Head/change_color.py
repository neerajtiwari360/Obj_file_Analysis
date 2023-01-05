def change_color(file,file_mtl):
  f=open(file, 'a')
  f.write('\nusemtl MyTexture')  
  for line in open(file, 'r'):
    if line.startswith('#'): continue
    values = line.split()
    if not values: continue
    if values[0] == 'f':
      flag=0
      for v in values[1:4]:
        w = v.split('/')
        if int(w[0])==2:
          flag=1
          break
      if flag==1:
        str='\nf '
        values = line.split()
        for v in values[1:4]:
          w = v.split('/')
          str=str+w[0]+'/4 '
        f.write(str)
  f=open(file_mtl,'a')
  f.write('newmtl MyTexture\nmap_Kd my_new.png')
  image = Image.new('RGB', (2, 2))
  pixels = image.load()

  pixels[0,0]=(0, 255, 0)
  pixels[0,1]=(0, 255, 0)
  pixels[1,0]=(0, 255, 0)
  pixels[1,1]=(0, 255, 0)
  image.save('my_new.png', 'PNG')
  #print(f.read())
                    