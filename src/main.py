import functions

data = functions.read_json("../operations.json")
executed_data = functions.check_executed(data)
sorted_and_executed = functions.sorted_operation(executed_data)

for item in sorted_and_executed:
    print(functions.program_output(item))