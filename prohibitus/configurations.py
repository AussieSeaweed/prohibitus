from abc import ABC
from math import inf


class Configuration(ABC):
    # Data settings
    training_dataset_pathname = None
    test_dataset_pathname = None
    dataset_shuffle_count = None
    max_training_dataset_size = None
    max_test_dataset_size = None

    # Model settings
    attention_drop_percentage = None
    residual_drop_percentage = None
    embedding_drop_percentage = None
    token_count = None
    chunk_size = None
    embedding_dim = None
    feedforward_dim = None
    head_count = None
    layer_count = None

    # Trainer settings
    learning_rate = None
    betas = None
    weight_decay = None
    max_epoch_count = None
    batch_size = None
    grad_norm_clip = None
    decay_learning_rate = None
    warmup_token_count = None
    final_token_count = None
    autosave_pathname = None
    checkpoint_pathname = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise ValueError(f'Unknown attribute: {key}')

        assert self.embedding_dim % self.head_count == 0


class ABCConfiguration(Configuration):
    # Data settings
    training_dataset_pathname = './resources/abc/*.abc'
    test_dataset_pathname = None
    dataset_shuffle_count = 1000000
    max_training_dataset_size = inf
    max_test_dataset_size = inf

    # Model settings
    attention_drop_percentage = 0.1
    residual_drop_percentage = 0.1
    embedding_drop_percentage = 0.1
    token_count = 128
    chunk_size = 128
    embedding_dim = 512
    feedforward_dim = 1024
    head_count = 8
    layer_count = 8

    # Trainer settings
    learning_rate = 6e-4
    betas = 0.9, 0.95
    weight_decay = 0.1
    max_epoch_count = 20
    batch_size = 256
    grad_norm_clip = 1.0
    decay_learning_rate = True
    warmup_token_count = 1e5
    final_token_count = 1e9
    autosave_pathname = './saves/abc/autosave.pt'
    checkpoint_pathname = './saves/abc/checkpoint.pt'


class MidiConfiguration(Configuration):
    # Data settings
    training_dataset_pathname = './resources/midi/training/**/*.mid'
    test_dataset_pathname = './resources/midi/test/**/*.mid'
    dataset_shuffle_count = 5000000
    max_training_dataset_size = 800000
    max_test_dataset_size = 200000

    # Model settings
    attention_drop_percentage = 0.1
    residual_drop_percentage = 0.1
    embedding_drop_percentage = 0.1
    token_count = 12
    chunk_size = 128
    embedding_dim = 512
    feedforward_dim = 1024
    head_count = 8
    layer_count = 8

    # Trainer settings
    learning_rate = 6e-4
    betas = 0.9, 0.95
    weight_decay = 0.1
    max_epoch_count = 500
    batch_size = 256
    grad_norm_clip = 1.0
    decay_learning_rate = True
    warmup_token_count = 1e6
    final_token_count = 1e10
    autosave_pathname = './saves/midi/autosave.pt'
    checkpoint_pathname = './saves/midi/checkpoint.pt'
