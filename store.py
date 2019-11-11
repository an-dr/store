import shutil
import zipfile
import pathlib
import datetime
import sys
import os

STORE_PATH = pathlib.Path(os.getenv("STORE_PATH", "/STORED"))


def _get_time_stamp():
    now = datetime.datetime.now()
    return (now.strftime("%Y%m%d_%H%M%S"))


def _archive(path_in: pathlib.Path, path_out: pathlib.Path):
    path_out_str = (str(path_out)).rstrip('.zip')
    path_out = pathlib.Path(path_out_str)
    if path_in.is_dir():
        shutil.make_archive(path_out, 'zip', path_in)
    else:
        zipfile.ZipFile((str(path_out) + ".zip"), mode='w').write(path_in)


def _archive2store(path_in: pathlib.Path):
    print("Storing...", end='', flush=True)
    suff = ""
    if path_in.is_dir():
        suff = ".d"
    arch_name = _get_time_stamp() + "_" + path_in.name + suff

    out_p = STORE_PATH.joinpath(arch_name)
    try:
        _archive(path_in, out_p)
        print('\rStored as %s' % out_p)
    except Exception as e:
        print(' Error: %s' % e)


def test_arc():
    in_p = pathlib.Path("./New Folder")
    out_p = pathlib.Path("./test1.zip")
    _archive(in_p, out_p)
    in_p = pathlib.Path("./README.md")
    out_p = pathlib.Path("./test2.zip")
    _archive(in_p, out_p)


def test_arc2s():
    in_p = pathlib.Path("./New Folder")
    _archive2store(in_p)
    in_p = pathlib.Path("./README.md")
    _archive2store(in_p)


def main():
    a_num = len(sys.argv)
    if a_num > 1:
        i = 1
        while (i < a_num):
            _archive2store(pathlib.Path(sys.argv[i]))
            i += 1


if __name__ == '__main__':
    main()
