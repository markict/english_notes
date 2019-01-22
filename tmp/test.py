#! --*-- coding:utf-8 --*--
import os
import time
import argparse

def main():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--all', help='Push all notes to github', action='store_true')
    parser.add_argument('-d', '--dir', help='The target Dir you want to push', default='.')
    parser.add_argument('comment', help='The git commit comments', nargs='?', default=f'{current_time}')
    args = parser.parse_args()

    print(f" -a is {args.all} \n  -d is {args.dir} \n  -comment is {args.comment}")

if __name__ == '__main__':
    main()
