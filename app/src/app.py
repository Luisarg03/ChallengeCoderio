#!/usr/bin/env python
# -*- coding: utf-8 -*-
from config import config_aws, config_user, engine_db
from modules.model import model_create
from modules.extractaws import extract, create_tables_work
from modules.pipeline import clear_duplicated, create_fct_table, create_dim
from modules.querys import exect_querys
import time


print('SCRIPT FUNCIONANDO')


def timenote(value):

    valueD = (((value/365)/24)/60)
    Days = int (valueD)

    valueH = (valueD-Days)*365
    Hours = int(valueH)

    valueM = (valueH - Hours)*24
    Minutes = int(valueM)

    valueS = (valueM - Minutes)*60
    Seconds = int(valueS)

    print(Days,";",Hours,":",Minutes,";",Seconds)


if __name__ == '__main__':
    start = time.time()
    engine_db = engine_db()
    # print('CREATE MODEL...')
    # model_create(engine_db)

    # print('EXTRACT FILES FROM S3 AND CREATE TABLES...')
    # extract(
    #     engine_db,
    #     config_aws,
    #     config_user['raw_schema'],
    #     config_user['bucket'],
    #     config_user['file_init']
    # )
    
    # print('CREATE TABLES WORK...')
    # create_tables_work(
    #     engine_db,
    #     config_user['stg_schema'],
    #     config_user['raw_schema'],
    #     config_user['file_init']
    # )

    # print('REMOVING DUPLICATES...')
    # clear_duplicated(engine_db, config_user['stg_schema'])

    # print('CREATE FCT CUR TABLE...')
    # create_fct_table(
    #     engine_db,
    #     config_user['stg_schema']
    #     config_user['cur_schema'],
    #     config_user['file_init'])
    
    # print('CREATE DIM CUR ...')
    # create_dim(engine_db, config_user['cur_schema'])

    # print('EXECT QUERYS ...')
    # exect_querys(engine_db)

    # end = time.time()  
    # timenote(end-start)

    # print('EXTRACT FILES INCREMENT FROM S3 AND CREATE TABLES...')
    # extract(
    #     engine_db,
    #     config_aws,
    #     config_user['raw_schema'],
    #     config_user['bucket'],
    #     config_user['file_increment']
    # )

    # print('CREATE TABLES WORK INCREMENT...')
    # create_tables_work(
    #     engine_db,
    #     config_user['stg_schema'],
    #     config_user['raw_schema'],
    #     config_user['file_increment']
    # )

    # print('REMOVING DUPLICATES...')
    # clear_duplicated(
    #     engine_db,
    #     config_user['stg_schema'],
    #     config_user['file_increment']
    # )

    # print('CREATE FCT CUR TABLE...')
    # create_fct_table(
    #     engine_db,
    #     config_user['stg_schema'],
    #     config_user['cur_schema'],
    #     config_user['file_increment'])
    
    print('CREATE DIM CUR ...')
    create_dim(
        engine_db,
        config_user['cur_schema'],
        config_user['file_increment']
    )