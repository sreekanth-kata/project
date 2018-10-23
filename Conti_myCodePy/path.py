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
--------------------------------------------------------------------------------

rootDir = 'D:\Skata\Sreekanth_pc'
path = rootDir + '\messung'
fname_= path+ '\\temp_daten3.csv'

for dirName, subDir, fList in walk(path):
    print ('-'*80)                                    
    for fname in fList:
        if fname.endswith('.xls'):
            fullpath = join(path, dirName)
            chdir(fullpath)            
            print('\nMoved to CurDir: %s\nFile Found --> %s' %(dirName, fname))
#            print('Curdir is:%s'%getcwd())      
            
            f = open(fname)
            r = csv.reader(f)
            data = list(r)
#            print(data)              print('\n')
            header=data[1][0].split("\t")
#            unit=data[2][0].split("\t") #print(unit) #print(unit) #print(len(header))
            print(header)
            
            for i in range(0,len(data)):
                if [len(j) for j in [s.replace('\t', '') for s in data[i]]][0]:
                    numofrow=i
#                    print(numofrow) # count= count+1
        
            daten=[[0 for i in range(len(header))] for j in range(0,numofrow-2)]
            for i in range(0,numofrow-2):
                for j in range(len(header)):                    
                    daten[i][j]=data[i+3][0].split("\t")[j]
                    #print(daten[i][j])
            f.close        













