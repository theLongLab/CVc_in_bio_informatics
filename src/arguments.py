import argparse


def get_args():
    parser = argparse.ArgumentParser()
    # the environment setting
    parser.add_argument('--SNP_file',
                        type=str,
                        default='data/SNP_in_200GENE_chr1.csv',
                        help="SNP file Path")
    # path related arguments
    parser.add_argument('--save_path',
                        type=str,
                        default='simulation_output/frequentist_CVc',
                        help="Save path to simulation error output")
    parser.add_argument(
        '--bimbam_path',
        type=str,
        default='./bimbam_data/bimbam_10000_full_false_major_minor.txt')
    parser.add_argument('--bslmm_save_path',
                        type=str,
                        default='./simulation_output/bslmm_CVc')

    # phenotype generation related arguments
    parser.add_argument('--num_large_effect', type=int, default=100)
    parser.add_argument('--large_effect', type=float, default=400.0)
    parser.add_argument('--small_effect', type=float, default=2.0)

    # simulation related arguments
    parser.add_argument(
        '--num_fixed_snps',
        type=int,
        default=500,
        help=
        "Number of fixed terms (SNPs). Set -1 means using all SNPs as fixed terms. "
    )
    parser.add_argument('--simulation_times', type=int, default=1000)
    parser.add_argument('--n_folds', type=int, default=10)
    parser.add_argument(
        '--correcting',
        action='store_true',
        help='a boolean flag to indicate if correction is needed')
    parser.add_argument(
        '--method',
        type=str,
        default='blup',
        help=
        'The method to be used for predicting the phenotype in cross-validation.'
    )
    parser.add_argument(
        '--alpha',
        type=float,
        default=0,
        help=
        'alpha is the hyper-paramter for the regurization and must be non-negative.'
    )
    parser.add_argument(
        '--l1_ratio',
        type=float,
        default=0,
        help=
        'l1_ratio is the hyper-paramter in Elastic Net indicating the ratio using l1 regularization. Setting 0 means no l1 regularization.'
    )

    args = parser.parse_args()
    print(args)
    return args


if __name__ == '__main__':
    args = get_args()
    print(args.simulation_times)
