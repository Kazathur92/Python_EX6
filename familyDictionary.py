my_family = {
    'sister': {
        'name': 'Stephanie',
        'age': 31
    },
    'mother': {
        'name': 'Josefina',
        'age': 59
    }
}

# print(my_family["sister"]["name"], "is my sister, and is", my_family["sister"]["age"], "years old.")

for family_member, member_values in my_family.items():
  # print("family_member", family_member)
  # print("member_keys", member_keys)

  print(f"{member_values['name']} is my {family_member} and is {member_values['age']} years old.")
  # for member_property, values in member_values.items():
  #   print(values)
