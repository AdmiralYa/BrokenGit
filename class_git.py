import os
from git import Repo
import shutil
import glob
import datetime


class got_git():
    def __init__(self):
        self.root_repo = 'gitrepo/'
        self.url = None
        self.dirs = None

    def download(self, url):
        self.url = url
        self.root_repo = 'gitrepo' + str(datetime.datetime.today().strftime("%H_%M_%S")) + '/'
        if not os.path.exists(self.root_repo):
            os.makedirs(self.root_repo)
        try:
            Repo.clone_from(self.url, self.root_repo, branch='master', depth=1)
        except:
            print("URL doesn't exist, please enter the valid link")
            down_link.download(url=input())


    def get_dir(self):
        return self.root_repo


    def remove_file(self, *args):
        dirs = (d for d in glob.iglob(os.path.join(self.root_repo, '*'))
                if os.path.isdir(d) and os.path.basename(d) not in args)
        for dir in dirs:
            shutil.rmtree(dir)
        names = os.listdir(self.root_repo)  # список файлов и поддиректорий в данной директории
        for name in names:
            if name not in args:
                fullname = os.path.join(self.root_repo, name)  # получаем полное имя
                if os.path.isfile(fullname):  # если это файл...
                    os.remove(fullname)  # удаляем


if __name__ == "__main__":
    down_link = got_git()
    print("Please, submit link to the Repo")
    down_link.download(url=input())
    print(down_link.get_dir())
    down_link.remove_file('net.py', 'examples','doxygen.cfg','Makefile')
