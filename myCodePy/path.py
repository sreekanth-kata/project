from os import walk
#from os.path import join
#, chdir, listdir, getcwd

tic=time.time()
i=count=0

rootDir = 'D:\Skata\Sreekanth_pc'
path = rootDir + '\messung'
fname_= path+ '\\temp_daten3.csv'


def fold_File():
    dirName = []
    fname = []
    for dirName_, subDir, fList in walk(path):
        for fname_ in fList:
            if fname_.endswith('.xls'):   
                dirName.append(dirName_)
                fname.append(fname_) 
                #print('\nFound Cur dir: %s\nFound File: %s' %(dirName, fname))
  #             print('Curdir is:%s'%getcwd()) 
                #fullpath = join(path, dirName)
                #chdir(fullpath)                          
    return dirName, fname

dirName =  fold_File()[0]       #print dirName
fname =  fold_File()[1]         
