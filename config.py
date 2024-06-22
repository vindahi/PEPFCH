import argparse

class DefaultConfig(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser()

        # Data parameters
        self.parser.add_argument('--dataset', type=str, default='FashionVC', help='Dataset name')
        self.parser.add_argument('--data_path', type=str, default='./data/FashionVC/', help='Data path')
        self.parser.add_argument('--pretrain_model_path', type=str, default='./data/imagenet-vgg-f.mat', help='Pretrained model path')
        self.parser.add_argument('--training_size', type=int, default=16862, help='Training data size')
        self.parser.add_argument('--query_size', type=int, default=3000, help='Query data size')
        self.parser.add_argument('--database_size', type=int, default=16862, help='Database data size')
        self.parser.add_argument('--batch_size', type=int, default=256, help='Batch size')

        # Local arguments
        self.parser.add_argument('--num_class', type=int, default=27, help='Number of classes')
        self.parser.add_argument('--num_users', type=int, default=10, help='Number of users')
        self.parser.add_argument('--ways', type=int, default=15, help='Number of ways')
        self.parser.add_argument('--shots', type=int, default=20, help='Number of shots')
        self.parser.add_argument('--train_shots_max', type=int, default=20, help='Maximum number of shots for training')
        self.parser.add_argument('--stdev', type=int, default=2, help='Standard deviation')
        self.parser.add_argument('--train_ep', type=int, default=5, help='Number of local episodes')

        # Hyperparameters
        self.parser.add_argument('--hn_lr', type=float, default=0.001, help='Learning rate')
        self.parser.add_argument('--embedding_dim_img', type=int, default=32, help='Image embedding dimension')
        self.parser.add_argument('--embedding_dim_txt', type=int, default=32, help='Text embedding dimension')
        self.parser.add_argument('--hidden_dim_img', type=int, default=32, help='Image hidden dimension')
        self.parser.add_argument('--hidden_dim_txt', type=int, default=32, help='Text hidden dimension')
        self.parser.add_argument('--max_epoch', type=int, default=80, help='Maximum number of epochs')
        self.parser.add_argument('--alpha', type=float, default=0.9, help='Alpha')
        self.parser.add_argument('--beta', type=float, default=0.1, help='Beta')
        self.parser.add_argument('--s_param', type=int, default=0, help='S parameter')
        self.parser.add_argument('--gamma', type=float, default=10, help='Gamma')
        self.parser.add_argument('--eta', type=int, default=100000, help='Eta')
        self.parser.add_argument('--bit', type=int, default=16, help='Final binary code length')
        self.parser.add_argument('--lr', type=float, default=0.0001, help='Learning rate')

        self.parser.add_argument('--iid',  action='store_true', help='IID')
        self.parser.add_argument('--unequal', action='store_true', help='Unequal')
        self.parser.add_argument('--use_gpu',  action='store_true', help='Use GPU')
        self.parser.add_argument('--valid',  action='store_true', help='Validation')
        self.parser.add_argument('--print_freq', type=int, default=2, help='Print frequency')

        self.parser.add_argument('--result_dir', type=str, default='result', help='Result directory')
        self.parser.add_argument('--weight_dir', type=str, default='clients_weight/', help='Clients weight directory')

        self.opt = self.parser.parse_args()

        print('User config:')
        for k, v in self.opt.__dict__.items():
            if not k.startswith('__'):
                print(k, v)


opt = DefaultConfig()