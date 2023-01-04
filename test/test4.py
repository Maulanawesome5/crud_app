import json


# Buka file berekstensi JSON
f = open("test/test3_result.json", mode='r', encoding='utf8')

# Returns JSON sebagai Dictionary
data = json.load(f)

# Loop isi di dalam file
for i in data['data']:
    print(i)

# Close file
f.close()
