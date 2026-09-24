DROP TABLE IF EXISTS produtos;

CREATE TABLE produtos (
    id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    detalhes JSON NOT NULL
);

INSERT INTO produtos (id, nome, categoria, preco, detalhes)
VALUES
(
    1,
    'Notebook Pro 14',
    'Informática',
    4599.90,
    '{
        "marca": "TechMais",
        "cor": "cinza",
        "memoria_gb": 16,
        "armazenamento_gb": 512,
        "sistema": "Linux"
    }'
),
(
    2,
    'Smartphone X',
    'Telefonia',
    2199.00,
    '{
        "marca": "Conecta",
        "cor": "azul",
        "memoria_gb": 8,
        "armazenamento_gb": 256,
        "resistencia_agua": true
    }'
),
(
    3,
    'Teclado Mecânico',
    'Acessórios',
    349.90,
    '{
        "marca": "GameTech",
        "cor": "preto",
        "layout": "ABNT2",
        "conexao": "USB",
        "iluminacao": "RGB"
    }'
),
(
    4,
    'Monitor UltraWide',
    'Informática',
    1899.90,
    '{
        "marca": "TechMais",
        "cor": "preto",
        "polegadas": 29,
        "resolucao": "2560x1080",
        "frequencia_hz": 100
    }'
);
-- Consulta 1: visualizar os dados relacionais e o documento JSON completo
SELECT
    id,
    nome,
    categoria,
    preco,
    detalhes
FROM produtos;

-- Consulta 2: extrair propriedades específicas do JSON
SELECT
    nome,
    detalhes->>'$.marca' AS marca,
    detalhes->>'$.cor' AS cor,
    detalhes->>'$.memoria_gb' AS memoria_gb
FROM produtos;

-- Consulta 3: filtrar produtos pela marca armazenada no JSON
SELECT
    id,
    nome,
    preco,
    detalhes->>'$.marca' AS marca
FROM produtos
WHERE detalhes->>'$.marca' = 'TechMais';

-- Consulta 4: localizar produtos com pelo menos 8 GB de memória
SELECT
    id,
    nome,
    detalhes->>'$.memoria_gb' AS memoria_gb
FROM produtos
WHERE CAST(detalhes->>'$.memoria_gb' AS UNSIGNED) >= 8;

-- Consulta 5: verificar se o documento contém uma propriedade específica
SELECT
    id,
    nome,
    detalhes
FROM produtos
WHERE JSON_CONTAINS(detalhes, 'true', '$.resistencia_agua');

-- Consulta 6: atualizar uma propriedade do documento JSON
UPDATE produtos
SET detalhes = JSON_SET(detalhes, '$.garantia_meses', 12)
WHERE id IN (1, 2);

-- Conferir o resultado da atualização
SELECT
    id,
    nome,
    detalhes->>'$.garantia_meses' AS garantia_meses,
    detalhes
FROM produtos
WHERE id IN (1, 2);
