import os
#import zipfile
from datetime import datetime
import shutil

now= datetime.now()
dt= now.strftime('%Y%m%d')
NAME = f'backup_{dt}'


PATH_raw = 'project_root/data/'
PATH_save = f"project_root/backups/{NAME}"

#
# Делаем архив каталога с вложенными каталогами модулем шатил, он удобнее  и проще чем  ZipFile
#
# 



shutil.make_archive(PATH_save, 'zip', PATH_raw)        



