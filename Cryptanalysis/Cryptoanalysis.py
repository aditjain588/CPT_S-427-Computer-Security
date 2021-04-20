from collections import Counter

q2 = open("question2.txt", "r")
freq_dict = {}

while True:
  line = q2.readline()
  if not line:
    break
  for i in range(len(line)): # storing each letter in freq_dict dictionary.
    if line[i] in freq_dict.keys():
      freq_dict[line[i]] += 1
    else:
      freq_dict[line[i]] = 1

freq_dict.pop("?")
freq_dict.pop("\n")
total = 0
for k,v in freq_dict.items(): # calculating the total entries.
  total += v

for k,v in freq_dict.items(): # computing frequency for each letter.
  freq_dict[k] = v/total

print(freq_dict)

decoder = {'L':'q','K':'p','E':'g','C': 'k','J': 'o', 'H': 'n', 'P': 't', 'R': 'h', 'I': 'e', 'M': 'r', 'S': 'a', 'Y': 'y', 'V': 'f', 'F': 'l', 'A':'i', 'D': 'd', 'X':'x', 'U': 'b', 'Q': 'u', 'G': 'm', 'Z':'z','N':'c', 'W': 'w', 'O':'s', 'B':'j', 'T': 'v'}
# decoder dictionary

output = open('output.txt', 'w')

ans = open("question2.txt", "r")
while True:
  line1 = ans.readline()
  if not line1:
    break
  string = ""
  lineArr=line1.split('?') # converting each line to array by seprating each element by '?' keyword.
  for i in range(len(lineArr)): # traversing throught the array.
    for j in range(len(lineArr[i])): # going through each letter of the word.
        for k,v in decoder.items():
          if(lineArr[i][j] == k): # converting the ecrypted alphabet to the orignal alphabet using decoder dictionary.
            string += v
    lineArr[i] = string # converting an encrypted word to decrypted word.
    string = ""
  lineOutput = ' '.join(lineArr) # converting the array in a single string seprated by space.
  output.write(lineOutput)
  output.write("\n")
output.close()
 
