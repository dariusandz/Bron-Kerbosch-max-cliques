from os import path

filename1 = 'results.csv'
filename2 = 'results2.csv'

result_header1 = 'vertices,time\n'
result_header2 = 'edges,cliques_count\n'

def write_results(results):
    file_exists = path.exists(filename1)
    file = open(filename1, "a+")
    file2 = open(filename2, "a+")

    # if not file_exists:
        # file.write(result_header)

    delimeter = ","
    res1 = delimeter.join(results[:len(results)//2])
    res2 = delimeter.join(results[len(results)//2:])
    file.write(res1 + "\n")
    file2.write(res2 + "\n")
    file.close()
    file2.close()