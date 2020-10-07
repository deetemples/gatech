import subprocess
import os
import sys
from shutil import copyfile

def main():
    inputpath=sys.argv[1]
    inputpath = inputpath + "/" if inputpath[-1] != "/" else inputpath
    outputpath=sys.argv[2]
    outputpath = outputpath + "/" if outputpath[-1] != "/" else outputpath
    input_dir = os.listdir(inputpath)

    if len(input_dir) == 0:
        print("No files present in the directory.")

    for na in ['n','a']:
        try:
            fxa_path = filter(lambda x: x.find("f" + na + "a") >= 0, input_dir)
            fxa_input = inputpath + fxa_path[0] + "/all.f" + na + "a"
            fxa_output = outputpath + "f" + na + "a_rep_seq.f" + na + "a"
            print("Running CD-HIT for " + fxa_input)
            if na == 'a':
                command = "cd-hit -i " + fxa_input + " -o " + fxa_output
            else:
                command = "cd-hit-est -i " + fxa_input + " -o " + fxa_output
            os.system(command)
        except subprocess.CalledProcessError as err:
            print("Error running CD-HIT. Check the input files")
            print("Error thrown: " + err.output)

        print("Completed running CD-HIT for " + fxa_input)

        matching = {}

        for filename in os.listdir(inputpath + fxa_path[0]):
            if filename[0] == 'C':
                filename = inputpath + fxa_path[0]+'/'+filename
                with open(filename) as fnaa_file:
                    for line in fnaa_file:
                        if line[0] == '>':
                            in_matching = line.split()[0]
                            matching[in_matching] = filename

        copyfile(fxa_output, outputpath+'f'+na+'a_cluster_membership.txt')

        with open(outputpath+'f'+na+'a_cluster_membership.txt','r') as clstr:
            c_lines = clstr.readlines()
            w_lines = []

            for c_line in c_lines:
                if c_line[0] == '>':
                    c_line = c_line.split()
                    w_lines.append(matching[c_line[0]] + '\n')

        with open(outputpath+'f'+na+'a_cluster_membership.txt','w') as clstr:
            clstr.writelines(w_lines)

        print("Matched all cluster representatives to specific f"+na+"a file")

if __name__ == "__main__":
	main()
