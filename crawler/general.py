import os

# cada website que você aplica o crawler tem de estar em diferents projetos

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)

create_project_dir('thenewcrawler')

# criando os arquivos para queue e crawled data

def create_data_files(project_name, base_url):
    queue = project_name + '/queue.csv'
    crawled = project_name + "/crawled.csv"
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

#crate a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

# adicionar a um arquivo ja existente
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

#deletar o coteúdo de um aqruivo
def delete_file_content(path):
    with open(path, 'w'):
        pass #não faz nada

# ler arquivo e converter a linha em itens
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

# cada item é a nova linha de um arquivo
def set_to_file(links, file):
    delete_file_content(file)
    for link in sorted(links):
        append_to_file(file,link)