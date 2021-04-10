import os
import sys
import argparse

def main():
  parse_cmd_args(sys.argv[1:])
  command = sys.argv[1:][0]
  print(command)

def parse_cmd_args(cmd_args):
  parser = argparse.ArgumentParser(prog='jstn', usage='%(prog)s [command]')
  parser._positionals.title = 'commands'
  parser.add_argument('init', help="init")
  if len(cmd_args) < 0:
      parser.print_help()
      sys.exit(1)

if __name__ == '__main__':
  main()