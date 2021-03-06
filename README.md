# store

Module to fast create zip-file as backup

![main_pic](https://www.lucidchart.com/publicSegments/view/4caf2a87-e390-401c-9ec9-502595fc07cd/image.png)

## Using

`python store.py file1 dir2 file3 file4`

## Results

```bash
STORE_PATH/YYYYMMDD_hhmmss_file1.zip
STORE_PATH/YYYYMMDD_hhmmss_dir2.d.zip
STORE_PATH/YYYYMMDD_hhmmss_file3.zip
STORE_PATH/YYYYMMDD_hhmmss_file4.zip
```

## Optional

A. Specify environment variable `STORE_PATH` (default is `/STORED`)

B. Add `.PY` to `PathExt` envvar for Windows

C. Add store location to `PATH`

After this you can use the module as:

`store file1 dir2 file3 file4`

and getting archives at your backup directory

## Future dev

All the plans are here: [todo.txt](todo.txt)
