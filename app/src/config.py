#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

config_user = dict(
    bucket = "coderiodatalake",
    raw_schema = 'DLKRAW',
    stg_schema = 'DLKSTG',
    cur_schema = 'DLKCUR',
    wh_schema = 'WH',
    file_init = 'dataset_init',
    file_increment = 'dataset_increment'
)

### USER DUMMY
config_aws = dict(
    service_name='s3',
    aws_access_key_id='AKIAYKHAW5NFPIOLKAUC',
    aws_secret_access_key='4WkCZEuR/dYNVRRJqN7zQRdfRFMJsicjxlqFtbTg'
)


def engine_db():
    config_db = dict(
    drivername='postgresql+psycopg2',
    username='root',
    password='root',
    # host='pg_container',
    host='localhost',
    port='5432',
    database='coderio',
    )
    url = URL.create(**config_db)
    engine = create_engine(url, isolation_level="AUTOCOMMIT")

    return engine