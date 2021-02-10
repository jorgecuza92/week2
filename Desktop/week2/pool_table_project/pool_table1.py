# Tables
import datetime

tables = []


class PoolTable:
    def __init__(self, table_number, availability=True):
        self.table_number = table_number
        self.availability = True
        self.minutes_played = 0
        self.start_time = None
        self.end_time = None


    def add_table(self, table_list):
        table_list.append(self)
        # for table in table_list:
        #     # print(self.availability)
        #     # print(table_list)

    def checkin(self):
        self.availability = False
        self.start_time = datetime.datetime.now()

    def checkout(self):
        self.availability = True
        self.end_time = datetime.datetime.now()

    def get_time_played(self):
        return self.end_time - self.start_time


def print_table(table_list):
    tableindex = 0
    tableindex += 1
    for table in table_list:
        print(f"TABLE {tableindex} -- Availability: {table.availability}; minutes used: {table.minutes_played}")
        


def make_list_of_twelve_tables(table_list):
    for i in range(0, 12):
        new_table = PoolTable(i)
        table_list.append(new_table)



make_list_of_twelve_tables(tables)
print_table(tables)




# def available_pool_tables(PoolTable):
#     if table.availability == True:
#         for pool_table in tables:




# def print_table(table_list):
#     tableindex = 1
#     for table in table_list:
#         print(f"TABLE {tableindex} -- {table.availability}; {table.minutes_played}")


# pool_table = PoolTable('1', True)
# pool_table.add_table(tables)

# def available_pool_tables(PoolTable):
#     if table.availability == True:
#         for pool_table in tables:
#             print(f"TABLE: {pool_table.table_number}")


# view added table to tables list
# def print_table():
#     for pool_table in tables:
#         return f"TABLE: {pool_table.table_number}\nAVAILABLE: {pool_table.availability}"

  

# for index in range(0, len(tables)):
#     pool_table = tables[index]
#     print(f" TABLE: {pool_table.table_number}  \n AVAILABILITY: {pool_table.availability}")


