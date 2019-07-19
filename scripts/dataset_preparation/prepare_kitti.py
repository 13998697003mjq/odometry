import argparse
import os

import __init_path__
import env

from odometry.preprocessing import prepare_dataset

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_root', type=str,
                        default=os.path.join(env.DATASET_PATH, 'KITTI_odometry_2012/dataset/sequences/'))
    parser.add_argument('--output_dir', type=str, required=True)
    parser.add_argument('--of_checkpoint', type=str,
                        default=os.path.join(env.DATASET_PATH, 'Odometry_team/weights/pwcnet.ckpt-84000'))
    parser.add_argument('--depth', action='store_true', default=True)
    parser.add_argument('--depth_checkpoint', type=str,
                        default=os.path.join(env.DATASET_PATH, 'Odometry_team/weights/model-199160'))
    args = parser.parse_args()

    prepare_dataset(dataset_type='KITTI',
                    dataset_root=args.dataset_root,
                    output_root=args.output_dir,
                    target_size=(96, 320),
                    optical_flow_checkpoint=args.of_checkpoint,
                    depth_checkpoint=args.depth_checkpoint if args.depth else None)

