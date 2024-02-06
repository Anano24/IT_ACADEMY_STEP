

with open("test1.txt", "w") as file, open("test2.txt", "w") as file2:
    file.write("hello test1")
    file2.write("hello test2")


with open("test1.txt", "r") as file1, open("test2.txt", "r") as file2:
    content_file1 = file1.read()
    content_file2 = file2. read()


combined_txt = content_file1 + "\n" + content_file2

with open("combined.txt", "w") as combined_output:
    combined_file = combined_output.write(combined_txt)


with open("combined.txt", "r") as combined_output:
        print(combined_output.read())

        
