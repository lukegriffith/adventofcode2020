f = open('day2.txt', 'r')
content = f.read()
lines = content.split('\n')

valid = 0

for line in lines:

  pre, post = line.split(':')
  limits, character = pre.split(' ')
  lower, higher = limits.split('-')
  password = post.lstrip()
  

  char_count = 0
  for c in password:
    if c == character:
      char_count = char_count + 1

  if char_count >= int(lower) and char_count <= int(higher):
    valid = valid + 1

print(valid)