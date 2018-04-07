from pymongo import MongoClient, ASCENDING

client = MongoClient('localhost', 27017)
db = client['ub_learning_tree']

'''
init database by files from file
'''
def init_from_tree_files():
    # TODO
    # class.create_index([('index', ASCENDING)])
    for i in db.list_collection_names():
        db.drop_collection(i)
    import json
    print('[server.db/init_from_tree_files]: open file ./data/classes.json')
    with open('./data/classes.json') as f:
        classes = json.load(f)
        for n in classes['classNames']:
            print('[server.db/init_from_tree_files]: open file ./data/{0}.json'.format(n))
            with open('./data/{0}.json'.format(n)) as fn:
                node = json.load(fn)
                db[n].insert_many(node['content'])
                db[n].create_index([('index', ASCENDING)], unique=True)

'''
get all class (collection) names
rtype: list[str]
'''
def get_all_class_names():
    return db.collection_names()

'''
get node names of a class named {class_name}
{class_name}: str
rtype: list[str]
'''
def get_nodes_of_class(class_name):
    cl = db[class_name]
    return [i['name'] for i in list(cl.find())]

'''
get single node named {node_name}, in class {class_name}
{title}: str
{class_name}: str
rtype: dict
'''
def get_node_info(node_name, class_name):
    cl = db[class_name]
    node = cl.find_one({'name': node_name})
    del node['_id']
    return node


if __name__ == '__main__':
    init_from_tree_files()

    all_classes = get_all_class_names()
    print('{0}:{1}'.format(type(all_classes), all_classes))

    all_nodes = get_nodes_of_class(all_classes[0])
    print('{0}:{1}'.format(all_classes[0], all_nodes))

    node_inf = get_node_info(all_nodes[0], all_classes[0])
    print('{0}:{1}:\n{2}'.format(all_classes[0], all_nodes[0], node_inf))
