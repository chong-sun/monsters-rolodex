import numpy as np

input_csv = "lmt.csv"
input = "test-best200.arff"
input_combined = "test-best200-combined.arff"
output = "test-best200-combined.arff"


def combine_feature_vector():
    count = 0
    attribute_count = 0
    user_vector = dict()
    user_location = dict()

    with open(input, "r") as i:
        with open(output, "a") as o:
            for line in i:
                if line.upper().startswith('@RELATION') or line.upper().startswith('@DATA'):
                    o.write(line)
                    continue
                if line.upper().startswith('@ATTRIBUTE'):
                    o.write(line)
                    attribute_count += 1
                    continue
                if line == '\n':
                    continue
                attribute = line.split(',')
                user_id = attribute[1]
                user_v = np.array(list(map(int, attribute[2:-1])))
                user_c = attribute[-1]

                if user_id in user_vector:
                    user_vector[user_id] += user_v
                else:
                    user_vector[user_id] = user_v
                    user_location[user_id] = user_c

            for key, value in user_vector.items():
                value_string = ','.join(map(str, list(value)))
                count += 1
                string_to_write = str(count) + "," + str(key) + "," + value_string + "," + str(user_location[key])
                o.write(string_to_write)


def write_test_results():
    id_result = dict()
    inst_id = dict()
    inst_result = dict()
    counter = 0

    with open(input_csv, "r") as c:
        for line in c:
            if line == '\n':
                continue
            if counter == 0:
                counter += 1
                continue
            else:
                kv = line.split(',')
                print(kv[2])
                inst_result[kv[0]] = kv[2]

    with open(input_combined, "r") as i:
            for line in i:
                if line.upper().startswith('@RELATION') or line.upper().startswith('@DATA') or line.upper().startswith('@ATTRIBUTE'):
                    continue
                if line == '\n':
                    continue
                attribute = line.split(',')
                inst_id[attribute[0]] = attribute[1]

    for key in inst_result:
        if key in inst_id.keys():
            id_result[inst_id[key]] = inst_result[key].replace('1', '').replace('2', '').replace('3', '').replace(':', '')

    with open(input, "r") as i:
        with open(output, "a") as o:
            o.write("tweet-id,class\n")
            for line in i:
                if line.upper().startswith('@RELATION') or line.upper().startswith('@DATA') or line.upper().startswith('@ATTRIBUTE'):
                    continue
                if line == '\n':
                    continue
                attribute = line.split(',')
                user_id = attribute[1]
                o.write(str(attribute[0])+","+str(id_result[user_id])+"\n")
