def get_word_count(text):
  text_array = text.split()
  return len(text_array)

def get_character_counts(text):
  data = {} 
  for char in text:
    if char.lower() in data:
      data[char.lower()] += 1
    else:
      data[char.lower()] = 1
  return data

def sort_on(items):
  return items["num"]

def get_character_counts_sorted(text):
  data_dict = {}
  data_list = []

  for char in text:
    if char.lower() in data_dict:
      data_dict[char.lower()] += 1
    else:
      data_dict[char.lower()] = 1

  for key in data_dict:
    data_list.append({"name": key, "num": data_dict[key]})

  data_list.sort(reverse=True, key=sort_on)

  return data_list

def get_num_words(text):
  text_array = text.split()
  return len(text_array)

def get_alpha_character_counts_sorted(text):
  data_dict = {}
  data_list = []

  for char in text:
    if char.isalpha():
      if char.lower() in data_dict:
        data_dict[char.lower()] += 1
      else:
        data_dict[char.lower()] = 1

  for key in data_dict:
    data_list.append({"name": key, "num": data_dict[key]})

  data_list.sort(reverse=True, key=sort_on)

  return data_list