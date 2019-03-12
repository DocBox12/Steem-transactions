# Steem-transaction

This is script that download information about user transactions from Steem Blockchain. The following information is retrieved:

- author rewards
- fill orders
- transfers

# Requirements

- python 3
- database MariaDB
- steem library for Python 3
- mysql.connector from PIP
  
# How to use

- download latest stable version from [this website](https://github.com/DocBox12/Steem-transactions/releases)
- extract the archive
- execute command `chmod +x main.py`
- fill config.ini
- run `main.py --createdb`
- you can use the script

`main.py --help` return more information about script options.

# Config.ini

## Database

- **address** - server address with database
- **user** - database user
- **password** password database user
- **database_name** - database name
- **port** - database port

## Steem

- **username** - steem user whose information has will download
- **limit** - how many information has will download. More information you find [on this website](https://steem.readthedocs.io/en/latest/steem.html?highlight=get_account_history)

# Tables structure in database

The script create 3 table in database: **author_rewards**, **fill_order** and **transfers**.

## Elements common to all tables

Info! I'm not found official documentation which would contain an explanation of the this terms. This description has been created on base analyze work blockchain and information from the Internet.

- **trx_id** - transaction identifier in the whole blockchain
- **block** - block number
- **trx_in_block** - transaction in block
- **op_in_trx** - 
- **virtual_op** - virtual operations returned by full nodes
- **timestamp** - time created element in the Steem blockchain. Format: YYYY-MM-DD HH:MM:S
- **link** - a link to a website that shows information about transactions in graphical form - it does not come from blockchain, is generate by program.
 - **filled** - empty field for use - it does not come from blockchain, is generate by program.

## Author rewards

- **author** - user the prize went to
- **permlink** - link to post
- **sbd_payout** - reward in steem dollar
- **steem_payout** - reward in steem 
- **vesting_payout** - reward in VESTS

## Fill order

- **current_owner** - creator of the offer
- **current_orderid** -  
- **current_pays** - amount of the offer
- **open_owner** - user accepting the offer
- **open_orderid** - 
- **open_pays** - earned cryptocurrency on sales

## Transfers

- **from** - name of the sender
- **to** - the recipient's name
- **amount** - amount steem in transfer
- ***memo** - message in transaction