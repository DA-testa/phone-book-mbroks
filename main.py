# python3

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

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    
    book = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            new = {cur_query.number:cur_query.name}
            book.update(new)
        elif cur_query.type == 'del':
            if cur_query.number in book:
                del book[cur_query.number]
            
        else:
            response = 'not found'

            if cur_query.number in book:
                response = book.get(cur_query.number)

            result.append(response)

    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

