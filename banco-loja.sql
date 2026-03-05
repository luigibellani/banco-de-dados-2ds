CREATE TABLE Produtos (
    Codigo_Produto INT PRIMARY KEY,
    Nome_Produto VARCHAR(100) NOT NULL,
    Preco_Unitario_Kg DECIMAL(10, 2) NOT NULL,
    Comentarios TEXT
);
select * from Produtos;
