import os
import sys
def listFile(path):
  fileList = []
  for root, dirs, files in os.walk(top = path):
    for dir in dirs:
      dirPath = os.path.join(root, dir)
      fileList = fileList + listFile(dirPath)
    for file in files:
      filePath = os.path.join(root, file)
      fileList.append(filePath)
  return fileList

def check(word, files):
  for file in files:
    index = 1
    with open(file, 'r', errors='ignore') as f:
      for line in f:
        if word in line:
          print(file + ' (' + str(index) + '): ' + line, end='')
        index = index + 1

def checkWord(word, dir):
  files = listFile(dir)
  check(word, files)

def checkWords(file, dir):
  files = listFile(dir)
  words = []
  with open(file, 'r', errors='ignore') as f:
    for line in f:
      words.append(line)
  for word in words:
    check(word, files)

def main(args):
  if len(args) < 4:
    print('Missing arguments')
    return
  
  mode = int(args[1])
  dir = args[3]

  if mode == 0:
    word = args[2]
    checkWord(word, dir)
  elif mode == 1:
    word_file = args[2]
    checkWords(word_file, dir)
  else:
    print('Invalidate mode')

if __name__ == '__main__':
  main(sys.argv)
