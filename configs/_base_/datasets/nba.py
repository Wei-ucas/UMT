_base_ = 'datasets'
# dataset settings
dataset_type = 'NBA'
data_root = '/mnt/workspace/wangwei/sports-highlight/data/'
data = dict(
    train=dict(
        type=dataset_type,
        label_path=data_root + 'train_annotations.jsonl',
        video_path=[
            # data_root + 'slowfast_features', data_root + 'clip_features'
            "/mnt/workspace/wangwei/sports-highlight/data/features/umt_base_features"
        ],
        audio_path="/mnt/workspace/wangwei/sports-highlight/data/features/eat_features",
        query_path=data_root + 'clip_text_features',
        loader=dict(batch_size=32, num_workers=4, shuffle=True)),
    val=dict(
        type=dataset_type,
        label_path=data_root + 'test_annotations.jsonl',
        video_path=[
            "/mnt/workspace/wangwei/sports-highlight/data/features/umt_base_features"
        ],
        audio_path="/mnt/workspace/wangwei/sports-highlight/data/features/eat_features",
        query_path=data_root + 'clip_text_features',
        loader=dict(batch_size=1, num_workers=4, shuffle=False)))
