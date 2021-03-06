# -*- coding: utf-8 -*-
# @Date    : 2019-07-25
# @Author  : Xinyu Gong (xy_gong@tamu.edu)
# @Link    : None
# @Version : 0.0

import argparse


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        type=str,
    )
    parser.add_argument(
        '--data_size',
        type=int,
        default=500000,
        help='number of epochs of training')
    parser.add_argument(
        '--max_epoch',
        type=int,
        default=200,
        help='number of epochs of training')
    parser.add_argument(
        '--max_iter',
        type=int,
        default=None,
        help='set the max iteration number')
    parser.add_argument(
        '-gen_bs',
        '--gen_batch_size',
        type=int,
        default=64,
        help='size of the batches')
    parser.add_argument(
        '-dis_bs',
        '--dis_batch_size',
        type=int,
        default=64,
        help='size of the batches')
    parser.add_argument(
        '--g_lr',
        type=float,
        default=0.0002,
        help='adam: gen learning rate')
    parser.add_argument(
        '--d_lr',
        type=float,
        default=0.0002,
        help='adam: disc learning rate')
    parser.add_argument(
        '--ctrl_lr',
        type=float,
        default=3.5e-4,
        help='adam: ctrl learning rate')
    parser.add_argument(
        '--lr_decay',
        action='store_true',
        help='learning rate decay or not')
    parser.add_argument(
        '--beta1',
        type=float,
        default=0.0,
        help='adam: decay of first order momentum of gradient')
    parser.add_argument(
        '--beta2',
        type=float,
        default=0.9,
        help='adam: decay of first order momentum of gradient')
    parser.add_argument(
        '--num_workers',
        type=int,
        default=8,
        help='number of cpu threads to use during batch generatioarch n')
    parser.add_argument(
        '--latent_dim',
        type=int,
        default=128,
        help='dimensionality of the latent space')
    parser.add_argument(
        '--img_size',
        type=int,
        default=32,
        help='size of each image dimension')
    parser.add_argument(
        '--channels',
        type=int,
        default=3,
        help='number of image channels')
    parser.add_argument(
        '--n_critic',
        type=int,
        default=1,
        help='number of training steps for discriminator per iter')
    parser.add_argument(
        '--val_freq',
        type=int,
        default=20,
        help='interval between each validation')
    parser.add_argument(
        '--print_freq',
        type=int,
        default=100,
        help='interval between each verbose')
    parser.add_argument(
        '--load_path',
        type=str,
        help='The reload model path')
    parser.add_argument(
        '--exp_name',
        type=str,
        help='The name of exp')
    parser.add_argument(
        '--d_spectral_norm',
        type=str2bool,
        default=False,
        help='add spectral_norm on discriminator?')
    parser.add_argument(
        '--g_spectral_norm',
        type=str2bool,
        default=False,
        help='add spectral_norm on generator?')
    parser.add_argument(
        '--dataset',
        type=str,
        default='cifar10',
        help='dataset type')
    parser.add_argument(
        '--data_path',
        type=str,
        default='./datasets',
        help='The path of data set')
    parser.add_argument('--cpu', help='use cpu',
                        action='store_true')
    parser.add_argument('--init_type', type=str, default='normal',
                        choices=['normal', 'orth', 'xavier_uniform', 'false'],
                        help='The init type')
    parser.add_argument('--gf_dim', type=int, default=64,
                        help='The base channel num of gen')
    parser.add_argument('--df_dim', type=int, default=64,
                        help='The base channel num of disc')
    parser.add_argument(
        '--gen_model',
        type=str,
        default='shared_gan',
        help='path of gen model')
    parser.add_argument(
        '--dis_model',
        type=str,
        default='shared_gan',
        help='path of dis model')
    parser.add_argument(
        '--controller',
        type=str,
        default='controller',
        help='path of controller')
    parser.add_argument('--eval_batch_size', type=int, default=100)
    parser.add_argument('--num_eval_imgs', type=int, default=50000)
    parser.add_argument(
        '--bottom_width',
        type=int,
        default=4,
        help="the base resolution of the GAN")
    parser.add_argument('--random_seed', type=int, default=12345)

    # search
    parser.add_argument('--shared_epoch', type=int, default=15,
                        help='the number of epoch to train the shared gan at each search iteration')
    parser.add_argument('--grow_step1', type=int, default=25,
                        help='which iteration to grow the image size from 8 to 16')
    parser.add_argument('--grow_step2', type=int, default=55,
                        help='which iteration to grow the image size from 16 to 32')
    parser.add_argument('--max_search_iter', type=int, default=90,
                        help='max search iterations of this algorithm')
    parser.add_argument('--ctrl_step', type=int, default=30,
                        help='number of steps to train the controller at each search iteration')
    parser.add_argument('--ctrl_sample_batch', type=int, default=1,
                        help='sample size of controller of each step')
    parser.add_argument('--hid_size', type=int, default=100,
                        help='the size of hidden vector')
    parser.add_argument('--baseline_decay', type=float, default=0.9,
                        help='baseline decay rate in RL')
    parser.add_argument('--rl_num_eval_img', type=int, default=5000,
                        help='number of images to be sampled in order to get the reward')
    parser.add_argument('--num_candidate', type=int, default=10,
                        help='number of candidate architectures to be sampled')
    parser.add_argument('--topk', type=int, default=5,
                        help='preserve topk models architectures after each stage')
    parser.add_argument('--entropy_coeff', type=float, default=1e-3,
                        help='to encourage the exploration')
    parser.add_argument('--dynamic_reset_threshold', type=float, default=1e-3,
                        help='var threshold')
    parser.add_argument('--dynamic_reset_window', type=int, default=500,
                        help='the window size')
    parser.add_argument('--arch', nargs='+', type=int,
                        help='the vector of a discovered architecture')


    # # dataset parameters
    # parser.add_argument('--dataset_mode', type=str, default='unaligned',
    #                     help='chooses how datasets are loaded. [unaligned | aligned | single | colorization]')
    # parser.add_argument('--direction', type=str, default='AtoB', help='AtoB or BtoA')
    # parser.add_argument('--serial_batches', action='store_true',
    #                     help='if true, takes images in order to make batches, otherwise takes them randomly')
    # parser.add_argument('--num_threads', default=4, type=int, help='# threads for loading data')
    # parser.add_argument('--batch_size', type=int, default=1, help='input batch size')
    # parser.add_argument('--load_size', type=int, default=286, help='scale images to this size')
    # parser.add_argument('--crop_size', type=int, default=256, help='then crop to this size')
    # parser.add_argument('--max_dataset_size', type=int, default=float("inf"),
    #                     help='Maximum number of samples allowed per dataset. If the dataset directory contains more than max_dataset_size, only a subset is loaded.')
    # parser.add_argument('--preprocess', type=str, default='resize_and_crop',
    #                     help='scaling and cropping of images at load time [resize_and_crop | crop | scale_width | scale_width_and_crop | none]')
    # parser.add_argument('--no_flip', action='store_true',
    #                     help='if specified, do not flip the images for data augmentation')
    # parser.add_argument('--display_winsize', type=int, default=256, help='display window size for both visdom and HTML')
    # parser.add_argument('--phase', type=str, default='train', help='train, val, test, etc')
    #
    # parser.add_argument('--model', type=str, default='cycle_gan',
    #                     help='chooses which model to use. [cycle_gan | pix2pix | test | colorization]')
    # parser.add_argument('--input_nc', type=int, default=3,
    #                     help='# of input image channels: 3 for RGB and 1 for grayscale')
    # parser.add_argument('--output_nc', type=int, default=3,
    #                     help='# of output image channels: 3 for RGB and 1 for grayscale')
    # parser.add_argument('--pool_size', type=int, default=50,
    #                     help='the size of image buffer that stores previously generated images')

    opt = parser.parse_args()

    return opt
