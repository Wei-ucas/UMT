_base_ = 'umt_small_200e_nba_large.py'


model = dict(query_dec=dict(dec_cfg=dict(_repeat_=3)))