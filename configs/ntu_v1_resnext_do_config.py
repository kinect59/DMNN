{
    # Datasets: HumanEvaI, Human36, NTURGBD
    'data_set': 'NTURGBD',
    'data_set_version': 'v1',
    # Backend of the data source: hdf5, tfrecord, ram
    'data_source': 'ram',
    'only_3dpos': True,

    # Network settings
    'inference_model': 'conv3d_resnext',
    'resnet_blocks': [
        {'size': 32, 'stride': 1},
        {'size': 128, 'bottleneck': 32, 'cardinality': 16, 'stride': 1},
        {'size': 256, 'bottleneck': 64, 'cardinality': 16, 'stride': 2},
        {'size': 512, 'bottleneck': 128, 'cardinality': 16, 'stride': 2}],
    'num_layers': 3,
    'cell_model': None,
    'keep_prob': 0.5,

    ## Training Options
    # It's the batch size
    'batch_size': 32,
    # Final epoch
    'max_max_epoch': 80,
    # How fast should we learn?
    'learning_rate': 1.0e-4,
    # Train using learning rate decay
    'lr_decay': False,
    # Custom learning rate schedule
    'custom_lr': True,
    # List for the custom schedule
    'custom_lr_list': [(500, 1.0e-3), (50000, 1.0e-4), (75000, 1.0e-5)],

    ## Data Augmentation (or Modification)
    # Duplicate skeleton in classes with only one
    'dup_input': True,
    # Swap skeletons randomly
    'swap_input': True,
    # Jitter skeleton height
    'jitter_height': True,
    # Normalize distance matrixes by BatchNorm
    'norm_dms_bn': True,
    # learn a linear combination over the joints
    'learn_comb_unc': False,
}
