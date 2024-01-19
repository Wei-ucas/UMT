_base_ = [
    '../_base_/models/umt_base.py','../_base_/plugins/hd.py',
    '../_base_/datasets/nba_large.py', '../_base_/schedules/500e.py','../_base_/plugins/no_query.py',
    '../_base_/runtime.py'
]

norm_cfg = dict(type='LN')

model = dict(
    type='UMT',
    video_enc=dict(
        type='UniModalEncoder',
        dims=[1024, 256],
        pos_cfg=dict(type='PositionalEncoding'),
        enc_cfg=dict(type='TransformerEncoderLayer')),
    audio_enc=dict(
        type='UniModalEncoder',
        dims=[960, 256],
        pos_cfg=dict(type='PositionalEncoding'),
        enc_cfg=dict(type='TransformerEncoderLayer')),
    cross_enc=dict(
        type='CrossModalEncoder',
        dims=256,
        pos_cfg=dict(type='PositionalEncoding'),
        enc_cfg=dict(type='BottleneckTransformer'),
        norm_cfg=norm_cfg),
    # query_gen=dict(
    #     type='QueryGenerator',
    #     dims=[256, 256],
    #     enc_cfg=dict(type='MultiHeadAttention'),
    #     last_norm=True,
    #     norm_cfg=norm_cfg),
    query_dec=dict(
        type='QueryDecoder',
        dims=256,
        pos_cfg=dict(type='PositionalEncoding'),
        dec_cfg=dict(type='TransformerDecoderLayer'),
        norm_cfg=norm_cfg))