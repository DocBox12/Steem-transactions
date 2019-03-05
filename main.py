#!/usr/bin/env python3

from steem import Steem
from steem.account import Account
import datetime
import time

steem = Steem()

def get_claim_rewards():

    all_transactions = Account('docbox', steem).get_account_history(-1, 100, filter_by='claim_reward_balance', raw_output=True)

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

        
    return

