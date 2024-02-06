
special_lines = {
    2 : "two",
    8 : "eight",
    10 : "ten",
    13 : "thirteen",
    17 : "seventeen"
}


with open("test.txt", "w") as file:
    for i in range(1, 20):
        line_content = f"{i}. This is line {special_lines.get(i, str(i))}\n"

        file.write(line_content)



            
