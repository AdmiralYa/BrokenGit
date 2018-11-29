import class_git
import os
import shutil

git = class_git.got_git()
#propose that we know this shet
repo = input()


if __name__ == '__main__':
    git.download(repo)
    git.remove_file('net.py', 'examples', 'doxygen.cfg', 'Makefile')

    #hmmmm mb write get fir
    dir_name = git.get_dir()


    hard_way = os.getcwd().replace("'", "")
    conf_name = "opy_config.txt"
    shutil.copy(hard_way + "/" + conf_name, hard_way + "/" + dir_name + "/" + conf_name)

    bash_command = "python opy.py " + hard_way + "/" + dir_name
    os.system(bash_command)
