# python3
import array as arr


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries2(queries):
    result = []
    phone_book = [None]*10000000
    # print(phone_book)

    for curr_queries in queries:
        if curr_queries.type == "add":
            phone_book[curr_queries.number] = curr_queries.name

        elif curr_queries.type == "del":
            phone_book[curr_queries.number] = None

        elif curr_queries.type == "find":
            if phone_book[curr_queries.number] == None:
                result.append("not found")
            else:
                result.append(phone_book[curr_queries.number])
                # print(result)
    return result


def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else:  # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result


if __name__ == '__main__':
    write_responses(process_queries2(read_queries()))
