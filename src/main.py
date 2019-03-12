#!/usr/bin/env python3

from steem import Steem
from steem.account import Account
import datetime
import time
import mysql.connector as mariadb
import configparser
import os
import argparse

steem = Steem()

def create_sql():
    
    
    create_author_rewards = ("""
    CREATE TABLE author_rewards (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    trx_id TEXT NULL,
    block TEXT NULL,
    trx_in_block TEXT NULL,
    op_in_trx TEXT NULL,
    virtual_op TEXT NULL,
    timestamp TEXT NULL,
    author TEXT NULL,
    permlink TEXT NULL,
    sbd_payout TEXT NULL,
    steem_payout TEXT NULL,
    vesting_payout TEXT NULL,
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

    cursor.execute(create_author_rewards)
    mariadb_connection.commit()

    cursor.execute(create_fill_order)
    mariadb_connection.commit()

    cursor.execute(create_transfers)
    mariadb_connection.commit()
    
    return




def get_author_rewards():
    all_transactions = Account(steem_username, steem).get_account_history(-1, INT_steem_limit, filter_by='author_reward', raw_output=True)

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
        author = DICT_op.get("author")
        permlink = DICT_op.get("permlink")
        sbd_payout = DICT_op.get("sbd_payout")
        steem_payout = DICT_op.get("steem_payout")
        vesting_payout = DICT_op.get("vesting_payout")


        # Generate link to block

        link = "https://steemworld.org/block/" + str(block)

        filled = ""

        value = check_exists_transaction("author_rewards", permlink, "permlink")

        if value is True:
            continue

        sql_insert = ("""
        
        INSERT INTO author_rewards (trx_id, block, trx_in_block, op_in_trx, virtual_op, timestamp, author, permlink, sbd_payout, steem_payout, vesting_payout, link, filled)
        VALUES("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");

        """) % (str(trx_id), str(block), str(trx_in_block), str(op_in_trx), str(virtual_op), str(human_time), str(author), str(permlink), str(sbd_payout), str(steem_payout), str(vesting_payout), str(link), str(filled))


        cursor.execute(sql_insert)
        mariadb_connection.commit()

        
    return

def get_fill_order():
    all_transactions = Account(steem_username, steem).get_account_history(-1, INT_steem_limit, filter_by='fill_order', raw_output=True)

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

        value = check_exists_transaction("fill_order", trx_id, "trx_id")

        if value is True:
            continue

        sql_insert = ("""
        
        INSERT INTO fill_order (trx_id,	block, trx_in_block, op_in_trx, virtual_op,	timestamp,	current_owner, current_orderid,	current_pays, open_owner, open_orderid, open_pays, link, filled)
        VALUES("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s", "%s", "%s", "%s");

        """) % (str(trx_id), str(block), str(trx_in_block), str(op_in_trx), str(virtual_op), str(human_time), str(current_owner), str(current_orderid), str(current_pays), str(open_owner), str(open_orderid), str(open_pays), str(link), str(filled))


        cursor.execute(sql_insert)
        mariadb_connection.commit()

    return


def get_transfers():
    all_transactions = Account(steem_username, steem).get_account_history(-1, INT_steem_limit, filter_by='transfer', raw_output=True)

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
        
        from_ = DICT_op.get("from")
        to = DICT_op.get("to")
        amount = DICT_op.get("amount")
        memo = DICT_op.get("memo")

        # Generate link to block

        link = "https://steemworld.org/block/" + str(block) + "/" + str(trx_id)

        filled = ""

        value = check_exists_transaction("transfers", trx_id, "trx_id")

        print(value)
        if value is True:
            continue

        sql_insert = ("""
        
        INSERT INTO transfers (trx_id,	block, trx_in_block, op_in_trx, virtual_op,	timestamp, from_, to_, amount, memo, link, filled)
        VALUES("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s", "%s");

        """) % (str(trx_id), str(block), str(trx_in_block), str(op_in_trx), str(virtual_op), str(human_time), str(from_), str(to), str(amount), str(memo), str(link), str(filled))


        cursor.execute(sql_insert)
        mariadb_connection.commit()


    return


def check_exists_transaction(table, trx_id, cell):

    sql_search = ("""
    
    select * FROM %s
    where %s="%s";
    """) % (str(table), str(cell), str(trx_id))

    print(sql_search)

    cursor.execute(sql_search)

    raw_search = cursor.fetchall()

    if len(raw_search) == 0:
        return False
    else:
        return True

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
steem_limit = config['steem']['limit']
INT_steem_limit = int(steem_limit)

# SQL Connection
mariadb_connection = mariadb.connect(user=user_db, password=password_db, database=database_db, host=address_db, port=INT_port_db)

# Arguments / flags

parser = argparse.ArgumentParser()

parser.add_argument("--createdb", help="Create tables in database", action="store_true")

parser.add_argument("--run", help="Download all informations from blockchain", action="store_true")

parser.add_argument("--get_author_rewards", help="Download only information from blockchain marked as author reward", action="store_true")

parser.add_argument("--get_fill_order", help="Download only information from blockchain marked as fill_order", action="store_true")

parser.add_argument("--get_transfers", help="Download only information from blockchain marked as transfers", action="store_true")

args = parser.parse_args()

if args.createdb:
    cursor = mariadb_connection.cursor()
    create_sql()
    mariadb_connection.close()

if args.run:
    cursor = mariadb_connection.cursor()
    get_author_rewards()
    get_fill_order()
    get_transfers()
    mariadb_connection.close()

if args.get_author_rewards:
    cursor = mariadb_connection.cursor()
    get_author_rewards()
    mariadb_connection.close()

if args.get_fill_order:
    cursor = mariadb_connection.cursor()
    get_fill_order()
    mariadb_connection.close()

if args.get_transfers:
    cursor = mariadb_connection.cursor()
    get_transfers()
    mariadb_connection.close()