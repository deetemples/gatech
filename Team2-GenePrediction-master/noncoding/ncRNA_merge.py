#!/usr/bin/python3
import os

def ncRNA_merge_output(input_aragorn_path,input_rnammer_path,input_infernal_path,output_folder):
    # check the paths to directories provided contain prediction files:
    if not os.listdir(input_aragorn_path) :
        print("There are no aragorn gff files in the given directory path. Please check and try again.")
        return False
    if not os.listdir(input_rnammer_path) :
        print("There are no rnammer gff files in the given directory path. Please check and try again.")
        return False
    if not os.listdir(input_infernal_path) :
        print("There are no infernal files in the given directory path. Please check and try again.")
        return False
    
    # union gff
    ncRNA_merge_gff=output_folder+"/nc_merge_gff"    
    if os.path.exists(ncRNA_merge_gff) == False:
        os.mkdir(ncRNA_merge_gff)
    else:
        if os.listdir(ncRNA_merge_gff):
            print("Output gff folder exists please delete the files before continuing")
            return False

    ### All gff file names from aragorn/rnammer/infernal. Reading the corresponding three gff3 files of 1 sample.[The outputs of these 3 tools have the same names.]
    allresult=os.listdir(input_aragorn_path) 
    for x in allresult:
        l1=[]
        l2=[]
        l3=[]
        l_all=[]
        s1=[]
        s2=[]
        s3=[]
        with open(input_aragorn_path+"/"+x,'r') as f1:
            for line in f1:
                if not re.match("##",line):
                    l1.append(line)
                    p=[line.split("\t")[0],line.split("\t")[3],line.split("\t")[4]]
                    s1.append(';'.join(p))
        f1.close()
        with open(input_rnammer_path+"/"+x,'r') as f2:
            for line in f2:
                if not re.match("##",line):
                    l2.append(line)
                    p=[line.split("\t")[0],line.split("\t")[3],line.split("\t")[4]]
                    s2.append(';'.join(p))
        f2.close()
        with open(input_infernal_path+"/"+x,'r') as f3:
            for line in f3:
                if not re.match("##",line):
                    l3.append(line)
                    p=[line.split("\t")[0],line.split("\t")[3],line.split("\t")[4]]
                    s3.append(';'.join(p))
        f3.close()
        ara_infer=list(set(s1).difference(set(s3)))
        rna_infer=list(set(s2).difference(set(s3)))
        l_all=l3
        #print(len(l_all))
        if(len(ara_infer)!=0):
            find=[]
            for i in ara_infer:
                find.append(s1.index(i))
            for j in find:
                print(l1[j])
                l_all.append(l1[j])
        
        if(len(rna_infer)!=0):
                    find=[]
                    for i in rna_infer:
                            find.append(s2.index(i))
                    for j in find:
                            l_all.append(l2[j])
        
        #print(l_all)
        with open(ncRNA_merge_gff+x+".gff3","w") as fi:
            fi.write("##gff-version 3\n")
            for line in l_all:
                fi.write(line)
        fi.close()
        
    shutil.rmtree(input_aragorn_path)
    shutil.rmtree(input_infernal_path)
    shutil.rmtree(input_rnammer_path)


if __name__=="__main__":
    pass
