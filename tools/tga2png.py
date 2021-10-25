from PIL import Image

def tga2gpg(class_names):
    '''tga2png'''
    for class_name in class_names:
        for i in range(12):
            file_path = 'E:/大三/计算机视觉/作业/光度立体视觉/学习资料/photometric-stereo-master/psmImages/'+class_name+'/'+class_name+'.'+str(i)+'.tga'
            im = Image.open(file_path)
            output_path = 'E:/大三/计算机视觉/作业/光度立体视觉/code/data_processed/'+class_name+'/'+class_name+'.'+str(i)+'.png'
            im.save(output_path)
        mask_path = 'E:/大三/计算机视觉/作业/光度立体视觉/学习资料/photometric-stereo-master/psmImages/'+class_name+'/'+class_name+'.mask.tga'
        im = Image.open(mask_path)
        output_path = 'E:/大三/计算机视觉/作业/光度立体视觉/code/data_processed/'+class_name+'/'+class_name+'.mask.png'
        im.save(output_path)
        
def main():
    classes = ['buddha','cat','gray','horsr','owl','rock']
    tga2gpg(classes)

if __name__ == "__main__":
    main()
