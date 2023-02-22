#! /usr/bin/python3
#import built-in python modules
import sys
import os
import argparse
import time



start_time = time.time()



#where we specify input parameters
parser = argparse.ArgumentParser(prog='cryp')


parser.add_argument('-v',dest='verbose',action="store_true",help="add verbose func")


subparsers = parser.add_subparsers(help='help for subcommand', dest="subcommand")

#arguments pertaining to only mol2csv
command_lido_rewards = subparsers.add_parser('lido_rew', help='input csv file to convert lido rewards csv')
command_lido_rewards.add_argument('-i',dest='input',required=True, help="input a csv")
command_lido_rewards.add_argument('-o',dest='name_csv', help="feed output file name")
command_lido_rewards.add_argument('--null',dest='not_none', action="store_true",help="output in the csv to have NULL, instead of being empty")


#make args object
args = parser.parse_args()


#preparing kwargs with args 
kwargs = {}
kwargs = vars(args)


if args.verbose:
    print("############################")
    print("Parameters used:")
    print("############################")
    for key,val in kwargs.items():
        print(str(key)+": " + str(val))
    print("############################")


if (args.subcommand == "lido_rew"):
    input_mol2  = kwargs['input']
    output_name = kwargs['name_csv']
    #read in the input csv file
    



end_time = time.time()
print('duration: ' + str(end_time - start_time)+ " seconds")
