# store

Module to fast create zip-file as backup

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
B. Add `.PY` to `PathExt` envvar wor Windows
C. Add store location to `PATH`

After this you can use the module as:
`store file1 dir2 file3 file4`

and getting archives at your backup directory
