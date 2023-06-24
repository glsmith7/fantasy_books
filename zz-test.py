import yaml

# use faster C code if available, otherwise pure python code
try:
    from yaml import CSafeLoader as SafeLoader

except ImportError:
    from yaml import SafeLoader

with open("fantasy_book_settings.yaml") as f:     
    config = yaml.load(f, Loader=SafeLoader)

print (config['book_variables_in_chosen_order'])