import os
import sys
import csv
import hashlib

TYPES = [ "jpg"]

def organize_by_format(diretorio):
    check_sum = hashlib.sha256()
    with open(diretorio, "rb") as opened_file:
        content_file = opened_file.read()
        check_sum.update(content_file)
        content_hash = check_sum.hexdigest()
        print(content_hash)





# organize_by_format("/media/lucas/SSD/my-data/lucas/compactados/xz/jpg/lucasgf-20200805-3518.jpg")
# organize_by_format("/media/lucas/SSD/my-data/lucas/compactados/xz/jpg/lucasgf-20200805-3519.jpg")

arr = ['/media/lucas/SSD/my-data/stage/Outros/Sem Data/VID_29841017_223414_084.mp4', '/media/lucas/SSD/my-data/stage/Outros/Videos/Movie001.mp4', '/media/lucas/SSD/my-data/lucas/videos/MPG/M2U01291.MPG', '/media/lucas/SSD/my-data/lucas/videos/MP4/M4H00384.MP4', '/media/lucas/SSD/my-data/lucas/videos/mp4/lucasgf-20210119-214.mp4', '/media/lucas/SSD/my-data/lucas/videos/mp4/lucasgf-20210220-1275.mp4', '/media/lucas/SSD/my-data/lucas/videos/mp4/lucasgf-20210220-1277.mp4', '/media/lucas/SSD/my-data/lucas/videos/mp4/lucasgf-20210220-1288.mp4', '/media/lucas/SSD/my-data/lucas/videos/mp4/lucasgf-20210221-1298.mp4', '/media/lucas/SSD/my-data/lucas/videos/mp4/lucasgf-20210221-1299.mp4', '/media/lucas/SSD/my-data/lucas/videos/mp4/lucasgf-20210721-6053.mp4', '/media/lucas/SSD/my-data/lucas/videos/mp4/lucasgf-20210720-6051.mp4', '/media/lucas/SSD/my-data/lucas/videos/mp4/lucasgf-20210720-6052.mp4', '/media/lucas/SSD/my-data/lucas/videos/mp4/lucasgf-20210725-6068.mp4', '/media/lucas/SSD/my-data/lucas/videos/mp4/lucasgf-20210725-6091.mp4', '/media/lucas/SSD/my-data/lucas/videos/mp4/lucasgf-20220801-1602.mp4', '/media/lucas/SSD/my-data/lucas/videos/mp4/lucasgf-20221215-3214.mp4', '/media/lucas/SSD/my-data/lucas/videos/mp4/lucasgf-20230501-1153.mp4', '/media/lucas/SSD/my-data/lucas/videos/mp4/lucasgf-20230519-1230.mp4', '/media/lucas/SSD/my-data/lucas/videos/mp4/lucasgf-20230721-1742.mp4', '/media/lucas/SSD/my-data/lucas/videos/mp4/lucasgf-20230721-1747.mp4', '/media/lucas/SSD/my-data/lucas/videos/mp4/lucasgf-20230820-1918.mp4', '/media/lucas/SSD/my-data/lucas/compactados/zip/Compactados.zip', '/media/lucas/SSD/my-data/lucas/compactados/zip/audios.zip', '/media/lucas/SSD/my-data/lucas/compactados/zip/Trio de Cordas _ Cerimônia Casamento 22.01.22-20220128T183203Z-001.zip']
print(len(arr))