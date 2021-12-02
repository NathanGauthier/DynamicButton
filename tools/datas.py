import glob


def get_files():
   # hard_coded_path = 'D:/GAUTHIER_Nathan/MOVIE/ASSETS/CAR'
    hard_coded_path = "D:/GAUTHIER_Nathan/MOVIE"
    files = glob.glob(hard_coded_path + "/*/*/*/*/*.*")
    return files


if __name__ == '__main__':

    for f in get_files():
        print(f)
        #print(get_files())
