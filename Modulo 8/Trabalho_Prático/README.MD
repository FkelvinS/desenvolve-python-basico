**Documento Descritivo - FK Estética**

# Introdução

A empresa FK Estética atua no ramo automotivo, oferecendo uma ampla variedade de acessórios para a estética de carros, como ceras, produtos de limpeza, adesivos personalizados, envelopamento e muito mais.

O sistema desenvolvido tem como objetivo gerenciar o controle de usuários e produtos da empresa, garantindo uma administração eficiente. Há dois tipos principais de usuários:

- **Gerente**: Possui acesso completo ao sistema, podendo cadastrar, atualizar e remover usuários e produtos.
- **Funcionário**: Possui acesso limitado, podendo apenas visualizar produtos e cadastrar vendas.

# Implementação

### **Usuários**

1. **Estrutura de Dados:**

   - Os usuários são armazenados em uma lista de dicionários.
   - Cada dicionário contém as chaves: `login`, `senha`, `nome` e `nivel`.

2. **Arquivo de Registro:**

   - Os dados dos usuários são armazenados em um arquivo CSV, onde cada linha representa um usuário com seus atributos separados por vírgula.

3. **Funcionalidades CRUD:**

   - **Create (Criar):** Cadastro de novos usuários.
   - **Read (Ler):** Listagem de todos os usuários cadastrados.
   - **Update (Atualizar):** Permite atualizar informações como nome, senha e nível de acesso.
   - **Delete (Remover):** Permite excluir um usuário pelo login.

### **Produtos**

1. **Estrutura de Dados:**

   - Os produtos são armazenados em uma lista de dicionários.
   - Cada dicionário contém as chaves: `codigo`, `nome`, `preco` e `quantidade`.

2. **Arquivo de Registro:**

   - Os produtos são armazenados em um arquivo CSV, onde cada linha representa um produto cadastrado.

3. **Funcionalidades CRUD:**

   - **Create (Criar):** Cadastro de novos produtos.
   - **Read (Ler):** Listagem de todos os produtos cadastrados.
   - **Update (Atualizar):** Permite modificar nome, preço ou quantidade.
   - **Delete (Remover):** Permite excluir um produto pelo código.
   - **Busca:** Possibilita pesquisar produtos por nome ou código.
   - **Ordenação:** Exibe os produtos ordenados por nome ou preço.

# Conclusão

Durante o desenvolvimento do sistema, encontramos alguns desafios, como o tratamento adequado dos arquivos de dados e a estruturação correta das permissões dos usuários. O principal aprendizado foi a importância da organização do código e da depuração para corrigir erros.

O sistema atendeu aos requisitos propostos, e no futuro poderíamos melhorar a interface, adicionando um painel visual mais intuitivo. Também poderíamos implementar a divisão do código em módulos para maior organização.

No geral, o projeto foi um sucesso e proporcionou uma boa experiência no desenvolvimento de um sistema CRUD completo!