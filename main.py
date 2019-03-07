#!/usr/bin/env python3

from steem import Steem
from steem.account import Account
import datetime
import time
import mysql.connector as mariadb
import configparser
import os

steem = Steem()

def create_sql():
    
    
    create_claim_rewards = ("""
    CREATE TABLE claim_rewards (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    trx_id TEXT NULL,
    block TEXT NULL,
    trx_in_block TEXT NULL,
    op_in_trx TEXT NULL,
    virtual_op TEXT NULL,
    timestamp TEXT NULL,
    account TEXT NULL,
    reward_steem TEXT NULL,
    reward_sbd TEXT NULL,
    reward_vests TEXT NULL,
    link TEXT NULL,
    filled TEXT NULL
    );

    
    """)


    create_fill_order = ("""
    
    CREATE TABLE fill_order (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    trx_id TEXT NULL,
    block TEXT NULL,
    trx_in_block TEXT NULL,
    op_in_trx TEXT NULL,
    virtual_op TEXT NULL,
    timestamp TEXT NULL,
    current_owner TEXT NULL,
    current_orderid TEXT NULL,
    current_pays TEXT NULL,
    open_owner TEXT NULL,
    open_orderid TEXT NULL,
    open_pays TEXT NULL,
    link TEXT NULL,
    filled TEXT NULL
    );

    
    """)


    create_transfers = ("""
    
    CREATE TABLE transfers (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    trx_id TEXT NULL,
    block TEXT NULL,
    trx_in_block TEXT NULL,
    op_in_trx TEXT NULL,
    virtual_op TEXT NULL,
    timestamp TEXT NULL,
    from_ TEXT NULL,
    to_ TEXT NULL,
    amount TEXT NULL,
    memo TEXT NULL,
    link TEXT NULL,
    filled TEXT NULL
    );
    
    """)

    cursor = mariadb_connection.cursor()

    cursor.execute(create_claim_rewards)
    mariadb_connection.commit()

    cursor.execute(create_fill_order)
    mariadb_connection.commit()

    cursor.execute(create_transfers)
    mariadb_connection.commit()

    mariadb_connection.close()


    
    return




def get_claim_rewards():
    cursor = mariadb_connection.cursor()

    all_transactions = Account(steem_username, steem).get_account_history(-1, 100, filter_by='claim_reward_balance', raw_output=True)

    for data in all_transactions:
        DICT_details = data[1]

        trx_id = DICT_details.get("trx_id")
        block = DICT_details.get("block")
        trx_in_block = DICT_details.get("trx_in_block")
        op_in_trx = DICT_details.get("op_in_trx")
        virtual_op = DICT_details.get("virtual_op")
        timestamp = DICT_details.get("timestamp")

        human_time = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')
        
        LIST_op = DICT_details.get("op")

        DICT_op = LIST_op[1]
        account = DICT_op.get("account")
        reward_steem = DICT_op.get("reward_steem")
        reward_sbd = DICT_op.get("reward_sbd")
        reward_vests = DICT_op.get("reward_vests")


        # Generate link to block

        link = "https://steemworld.org/block/" + str(block) + "/" + str(trx_id)

        filled = ""

        sql_insert = ("""
        
        INSERT INTO claim_rewards (trx_id, block, trx_in_block, op_in_trx, virtual_op, timestamp, account,reward_steem, reward_sbd, reward_vests, link, filled)
        VALUES("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s", "%s");

        """) % (str(trx_id), str(block), str(trx_in_block), str(op_in_trx), str(virtual_op), str(human_time), str(account), str(reward_steem), str(reward_sbd), str(reward_vests), str(link), str(filled))


        cursor.execute(sql_insert)
        mariadb_connection.commit()

    mariadb_connection.close()

        
    return

def get_fill_order():
    cursor = mariadb_connection.cursor()

    all_transactions = Account(steem_username, steem).get_account_history(-1, 100, filter_by='fill_order', raw_output=True)

    for data in all_transactions:
        DICT_details = data[1]

        trx_id = DICT_details.get("trx_id")
        block = DICT_details.get("block")
        trx_in_block = DICT_details.get("trx_in_block")
        op_in_trx = DICT_details.get("op_in_trx")
        virtual_op = DICT_details.get("virtual_op")
        timestamp = DICT_details.get("timestamp")

        human_time = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')

        LIST_op = DICT_details.get("op")

        DICT_op = LIST_op[1]
        current_owner = DICT_op.get("current_owner")
        current_orderid = DICT_op.get("current_orderid")
        current_pays = DICT_op.get("current_pays")
        open_owner = DICT_op.get("open_owner")
        open_orderid = DICT_op.get("open_orderid")
        open_pays = DICT_op.get("open_pays")

        # Generate link to block

        link = "https://steemworld.org/block/" + str(block) + "/" + str(trx_id)

        filled = ""

        sql_insert = ("""
        
        INSERT INTO fill_order (trx_id,	block, trx_in_block, op_in_trx, virtual_op,	timestamp,	current_owner, current_orderid,	current_pays, open_owner, open_orderid, open_pays, link, filled)
        VALUES("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s", "%s", "%s", "%s");

        """) % (str(trx_id), str(block), str(trx_in_block), str(op_in_trx), str(virtual_op), str(human_time), str(current_owner), str(current_orderid), str(current_pays), str(open_owner), str(open_orderid), str(open_pays), str(link), str(filled))


        cursor.execute(sql_insert)
        mariadb_connection.commit()
    mariadb_connection.close()

    return


def get_transfers():
    cursor = mariadb_connection.cursor()

    all_transactions = Account(steem_username, steem).get_account_history(-1, 100, filter_by='transfer', raw_output=True)

    for data in all_transactions:
        DICT_details = data[1]

        trx_id = DICT_details.get("trx_id")
        block = DICT_details.get("block")
        trx_in_block = DICT_details.get("trx_in_block")
        op_in_trx = DICT_details.get("op_in_trx")
        virtual_op = DICT_details.get("virtual_op")
        timestamp = DICT_details.get("timestamp")

        human_time = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')

        LIST_op = DICT_details.get("op")

        DICT_op = LIST_op[1]
        
        from_ = DICT_op.get("from_")
        to = DICT_op.get("to")
        amount = DICT_op.get("amount")
        memo = DICT_op.get("memo")

        # Generate link to block

        link = "https://steemworld.org/block/" + str(block) + "/" + str(trx_id)

        filled = ""

        sql_insert = ("""
        
        INSERT INTO transfers (trx_id,	block, trx_in_block, op_in_trx, virtual_op,	timestamp, from_, to_, amount, memo, link, filled)
        VALUES("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s", "%s");

        """) % (str(trx_id), str(block), str(trx_in_block), str(op_in_trx), str(virtual_op), str(human_time), str(from_), str(to), str(amount), str(memo), str(link), str(filled))


        cursor.execute(sql_insert)
        mariadb_connection.commit()
    mariadb_connection.close()


    return


# Load config file

config = configparser.ConfigParser()
config_file = os.path.join(os.path.dirname(__file__), 'config.ini')
config.read(config_file)

address_db = config['database']['address']
user_db = config['database']['user']
password_db = config['database']['password']
database_db = config['database']['database_name']
port_db =config['database']['port']
INT_port_db = int(port_db)
steem_username = config['steem']['username']

# SQL Connection
mariadb_connection = mariadb.connect(user=user_db, password=password_db, database=database_db, host=address_db, port=INT_port_db)
