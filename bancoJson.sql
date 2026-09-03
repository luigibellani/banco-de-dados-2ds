-- 1. Cria a tabela usando o tipo nativo JSON para armazenar dados complexos
CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    detalhes JSON
);

-- 2. Insere um registro salvando a estrutura de chaves e arrays no campo JSON
INSERT INTO produtos (nome, detalhes)
VALUES ('Camiseta', '{"cores": ["vermelho", "azul"], "tamanhos": ["P", "M", "G"]}');
-- 3. Extrai e exibe apenas a lista de cores contida na chave "cores" do JSON
SELECT JSON_EXTRACT(detalhes, '$.cores') AS cores FROM produtos;

-- 4. Filtra a tabela exibindo apenas produtos que possuem a cor "vermelho" no JSON
SELECT * FROM produtos 
WHERE JSON_CONTAINS(detalhes, '"vermelho"', '$.cores');


